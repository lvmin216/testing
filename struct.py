import requests
from lxml import etree

url = 'http://tieba.baidu.com/p/2166231880'
header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
r = requests.get(url,headers=header).content
s = etree.HTML(r)
print(s.xpath('//div/img/@src'))