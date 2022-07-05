from urllib import request
import ssl
import gzip

context = ssl._create_unverified_context()

class Spider():
    url = 'https://www.douyu.com/g_LOL'

    def __fetch_content(self):
        r = request.urlopen(Spider.url, context=context)
        htmls = r.read()
        htmls = gzip.decompress(htmls).decode("utf-8")
        print(htmls)

    def go(self):
        self.__fetch_content()

sprider = Spider()
sprider.go()
