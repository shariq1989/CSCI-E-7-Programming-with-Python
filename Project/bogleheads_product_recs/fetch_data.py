import scrapy
from urllib.parse import urlparse


class BogleheadsRecsSpider(scrapy.Spider):
    name = 'bogleheads_recs'
    start_urls = [
        'http://bogleheads.org',
    ]
    count = 0
    domains = {}

    # Collects all threads on the Bogleheads front page
    # Calls parse_posts to process thread objects
    def parse(self, response):
        # fetch the thread ID of each thread on the front page
        threads = self.collect_threads(response)
        print('Number of threads on front page ' + str(len(threads)))
        for thread in threads:
            # call parse_posts on each thread page
            yield scrapy.Request('https://www.bogleheads.org/forum/viewtopic.php?t=' + thread,
                                 callback=self.parse_posts)

    # collect threads on the Bogleheads.org front page
    def collect_threads(self, response):
        threads_list = []
        # get each link on the front page
        for link in response.css("tr[style*=vertical-align] td a::attr('href')").getall():
            # if the link leads to a thread
            if '&t=' in link:
                # get thread ID
                link = link.split("&t=", 1)[1]
                break_char = 0
                # if there is other info after the thread ID
                for i, char in enumerate(link):
                    if char not in '0123456789':
                        break_char = i
                        break
                # remove extra info
                if break_char != 0:
                    link = link[0:break_char]
                # collect thread list
                threads_list.append(link)
        # convert list to set, remove duplicates at O(1) speed
        thread_set = list(set(threads_list))
        return thread_set

    # Given thread object, crawl through posts. Access thread info using 'thread.url'
    def parse_posts(self, thread):
        # number of posts in thread
        num_posts = self.extract_num_posts(thread)
        # more than 50 posts, means that we need to crawl multiple pages
        if num_posts > 50:
            # each page contains 50 posts, finding number of pages
            num_pages = num_posts / 50
            # iterate through each page
            for page_num in range(1, int(num_pages)):
                # build url for specific page
                page_url = thread.url + '&start=' + str(50 * page_num)
                # call parse_posts on each thread page
                yield scrapy.Request(page_url, callback=self.process_posts_from_page)
            # if there are leftover posts, process the last page
            if num_pages > int(num_pages):
                page_url = thread.url + '&start=' + str(50 * (int(num_pages) + 1))
                yield scrapy.Request(page_url, callback=self.process_posts_from_page)
        else:
            # get all post bodies in a page
            self.process_posts_from_page(thread)

    def process_posts_from_page(self, thread):
        # get links if they are in a post
        links = thread.css('div.content a::attr(href)').getall()

        for link in links:
            if 'http://' in link or 'https://' in link and 'bogleheads' not in link:
                self.count += 1
                f = open('links.csv', 'a')
                f.write(link + '\n')
                f.close()
                domain = urlparse(link).netloc
                if domain in self.domains:
                    self.domains[domain] += 1
                else:
                    self.domains[domain] = 1
        print('Processed links', self.count)
        print('Domains', self.domains)

    def extract_num_posts(self, thread):
        # get pagination info so that URL's for pages can be generated
        pagination_info = thread.css('div.pagination::text').get()
        pagination_info = pagination_info.strip()
        number_of_posts = ''
        for char in pagination_info:
            # convert '### posts' to '###'
            if char not in '0123456789':
                break
            number_of_posts += char
        return int(number_of_posts)
