#python3
import requests
from lxml import etree
import urllib.request
import os

url = 'http://tieba.baidu.com/p/2166231880'
header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
r = requests.get(url,headers=header).content
s = etree.HTML(r)
img_url = s.xpath('//div/img/@src')

for i in img_url:
    file_name = i.split("/")[-1]
    download_path = "E:\\Python\\tieba"
    dist = os.path.join(download_path, file_name)
    urllib.request.urlretrieve(i, dist, None)
