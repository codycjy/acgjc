import re
import threading
import time
import requests
from lxml import etree
import threadpool

cookie = '__cfduid=dc8603d98c1b7027705a38d798f593e9c1605241305; _ga=GA1.2.1659073861.1605241306; ' \
         '_gid=GA1.2.1335797918.1605886691; Hm_lvt_ed618df76d54605d45b765fc0ce862e6=1605254430,1605508838,1605528938,' \
         '1605886691; Hm_lpvt_ed618df76d54605d45b765fc0ce862e6=1605886697 '
ua = 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
headers = {'cookie': cookie, 'user-agent': ua}

lock = threading.Lock()
i = 201


def getIndex():
    global i
    while i < 401:  # 获取目录内容
        url = "http://www.acgjc.com/yy/page/{}/".format(i)
        mainpage = requests.get(url=url).text
        print(i)
        a = re.findall("(http://www.acgjc.com/yy/\d*.html?)", mainpage)
        lock.acquire()
        with open("index3.txt", "a+", encoding="utf-8") as f:
            for j in a[::2]:
                f.write(j)
                f.write("\n")
        i += 1
        lock.release()


t = threading.Thread(target=getIndex)
t2 = threading.Thread(target=getIndex)
t3 = threading.Thread(target=getIndex)
t4 = threading.Thread(target=getIndex)


def x1(line):
    line = line.strip()
    page = requests.get(url=line).text
    html0 = etree.HTML(page)
    b = re.findall('(http://www.acgjc.com/storage-download/.*)" target="_blank', page)
    return b[0]


def x2(url3):
    time.sleep(5)
    links = requests.get(url3).text
    html = etree.HTML(links)
    tiqu = html.xpath('//*[@id="theme_custom_storage-0-download-pwd"]/@value')
    print(tiqu)
    # print(links)
    link = html.xpath('/html/body/div[4]/div/div[3]/fieldset/div/div[2]/a/@href')
    print(link)
    name = html.xpath('/html/body/div[4]/div/div[1]/h2/a/text()')
    print(name)

    return link[0], tiqu[0], name[0]


def x3(url3):
    with open('final_test2.csv', "a+", encoding="utf-8-sig") as f2:
        l, t, n = x2(url3)
        f2.write("{},{},{}".format(n, l, t))
        f2.write("\n")


def getIndex_multi():
    t.start()
    t2.start()
    t3.start()
    t4.start()


if __name__ == "__main__":
    #getIndex_multi()
    pass

"""    with open("index2.txt", "r") as f:
        c = 0
        for line2 in f:
            c += 1
            try:
                x3(x1(line2.strip()))
            except:
                print(c, "f")
            print(c)
"""
