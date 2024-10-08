import pprint
import requests


def gen_from_urls(urls: tuple) -> tuple:
    for response in (requests.get(url) for url in urls):
        yield len(response.content), response.status_code, response.url


# def gen_from_urls(urls: tuple) -> tuple:
#     for resp in (requests.get(url) for url in urls):
#         yield len(resp.content), resp.status_code, resp.url
#

# from url_utils import gen_from_urls
urls = ('http://headfirstlabs.com', 'http://oreilly.com', 'http://twitter.com')

for resp_len, status, url in gen_from_urls(urls):
    print(resp_len, '->', status, '->', url)

urls_res = {url: size for size, _, url in gen_from_urls(urls)}

pprint.pprint(urls_res)
