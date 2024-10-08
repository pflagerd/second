# See also requests_listcomp.py
# This file was copied verbatim from requests_listcomp.py
import requests

urls = ('http://headfirstlabs.com', 'http://oreilly.com', 'http://twitter.com')

for resp in [requests.get(url) for url in urls]:
    print(len(resp.content), '->', resp.status_code, '->', resp.url)
