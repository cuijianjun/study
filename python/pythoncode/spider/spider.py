from urllib import request
import ssl
import gzip
import re

context = ssl._create_unverified_context()

class Spider():
    url = 'https://www.douyu.com/g_LOL'
    root_pattern = '<main class="layout-Main">[\s\S]*?</main>'
    main_pattern = '<div class="DyListCover-info">[\s\S]*?</div>'
    def __fetch_content(self):
        r = request.urlopen(Spider.url, context=context)
        htmls = r.read()
        htmls = gzip.decompress(htmls).decode("utf-8")
        print(htmls)
        return htmls

    def __analysis(self, htmls):
        root_html = re.findall(Spider.root_pattern, htmls)
        main_html = re.findall(Spider.main_pattern, root_html[0])
        a = 1
       
    def go(self):
        htmls = self.__fetch_content()
        self.__analysis(htmls)

sprider = Spider()
sprider.go()
