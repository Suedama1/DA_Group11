# Importing appropriate libraries
import requests
# Perform a "get" request on the given website
url = 'https://www.thedamngoodshop.com/collections/found-boxes'
r = requests.get(url)
print(r.text)
# Display an "OK" return status
print('Status Code')
print('\t *', r.status_code)
# Display the Website header
h = requests.head(url)
print('Header:')
print("*********")
# Modify the Header user-agent to display “Mobile”
headers = {
    'User-Agent': 'Mobile'
}
url2 = 'http://httpbin.org/headers'
rh = requests.get(url2, headers=headers)
print(rh.text)
import scrapy
from scrapy.http.request import Request
# Use Scrapy web-crawler with appropriate parser “response.css”
class TDGSSpider(scrapy.Spider):
    name = "?"
    start_urls = ['?']
    def start_requests(self):
        headers = {'User-Agent':'Mozilla/5.0 (Android 7.0; Mobile; rv:54.0) Gecko/54.0 Firefox/54.0'}
        for url in self.start_urls:
            yield Request(url, headers=headers)
    def parse(self, response):
        css_selector = 'img'
        for x in response.css(css_selector):
            newsel = '@src'
            yield {
                'Image Link': x.xpath(newsel).extract_first(),
            }

# Task 7
        Page_selector = '.next a ::attr(href)'
        next_page = response.css(Page_selector).extract_first()
        if next_page:
            yield scrapy.Request(
                response.urljoin(next_page),
                callback=self.parse
            )
# Importing appropriate libraries
import unittest
# Task 8
class TestingHeader(unittest.TestCase):
    headers = {'User-Agent': 'Mobile'}
    url2 = 'http://httpbin.org/headers'
    rh = requests.get(url2, headers=headers)
    print(rh.text)
    def test_headers(self):
        self.assertTrue(TestingHeader.headers, 'Mobile')
if __name__ == '__main__':
    unittest.main()