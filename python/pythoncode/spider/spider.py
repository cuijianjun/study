from urllib import request
import ssl
import gzip
import re

context = ssl._create_unverified_context()

class Spider():
    url = 'https://www.douyu.com/g_LOL'
    root_pattern = '<main class="layout-Main">([\s\S]*?)</main>'
    main_pattern = '<div class="DyListCover-info">[\s\S]*?</div>'
    name_pattern = '<div class="DyListCover-userName is-template">([\s\S]*?)</div>'
    number_pattern = '</svg>([\s\S]*?)</span>'
    def __fetch_content(self):
        r = request.urlopen(Spider.url, context=context)
        htmls = r.read()
        htmls = gzip.decompress(htmls).decode("utf-8")
        return htmls

    def __analysis(self, htmls):
        anchors = []
        root_html = re.findall(Spider.root_pattern, htmls)
        main_html = re.findall(Spider.main_pattern, root_html[0])
        for html in main_html:
            name = re.findall(Spider.name_pattern, html)
            number = re.findall(Spider.number_pattern, html)
            if name != []:
                anchor = {'name': name, 'number': number}
                anchors.append(anchor)
        return anchors
    def __sort(self, anchors):
        anchors = sorted(anchors, key=self.__sort_seed, reverse=True)
        return anchors

    def __sort_seed(self, anchor):
        r = re.findall('(\d+\.?\d+)', anchor['number'])
        print(r)
        number = float(r[0])
        if '万' in anchor['number']:
            number *= 10000
        return number

    def __show(self, anchors):
        for rank in range(0, len(anchors)):
            print('rank' + str(rank + 1) + '  :  ' + anchors[rank]['name'] + '      ' + anchors[rank]['number'])

    def __refine(self, anchors):
        l = lambda anchor: {
            'name': anchor['name'][0].strip(),
            'number': anchor['number'][0]
            }
        return map(l, anchors)

    def go(self):
        htmls = self.__fetch_content()
        anchors = self.__analysis(htmls)
        anchors = list(self.__refine(anchors))
        anchors = self.__sort(anchors)
        self.__show(anchors)


sprider = Spider()
sprider.go()
