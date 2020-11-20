import requests
from lxml import etree
import re
import time
"""cookie='__cfduid=dc8603d98c1b7027705a38d798f593e9c1605241305; _ga=GA1.2.1659073861.1605241306; _gid=GA1.2.1028594813.1605508838; Hm_lvt_ed618df76d54605d45b765fc0ce862e6=1605250661,1605254430,1605508838,1605528938; Hm_lpvt_ed618df76d54605d45b765fc0ce862e6=1605528941'
ua='User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
headers={'cookie':cookie,'user-agent':ua}
for i in range(178, 201):
    url = "http://www.acgjc.com/yy/page/{}/".format(i)
    mainpage = requests.get(url=url,headers=headers).text
    # with open("id1.html","w+",encoding="utf-8") as f:
    #    f.write(mainpage.text)

    # print(mainpage.text)

    a = re.findall("(http://www.acgjc.com/yy/\d*.html?)", mainpage)
    with open("index2.txt", "a+", encoding="utf-8") as f:
        for j in a[::2]:
            f.write(j)
            f.write("\n")
    print(i)
    time.sleep(5)"""
def x1(line):


    line=line.strip()
#url2="http://www.acgjc.com/yy/112585.html"
    page=requests.get(url=line).text
    html0=etree.HTML(page)
    #link0=html0.xpath('//*[@id="post-7594"]/div/div[3]/a[1]')
    b=re.findall('(http://www.acgjc.com/storage-download/.*)" target="_blank',page)
    print(b[0])
    with open("p.txt", "a+", encoding="utf-8") as f:
        f.write(b[0])
        f.write("\n")
    time.sleep(2)


with open("index2.txt") as f:
    x=0
    for line in f:
        try:
            x1(line)
            x+=1
            print(x)
        except:
            x += 1
            print(x,"failed")

url3='http://www.acgjc.com/storage-download/?code=OTdmMVFDeWZLZ1RnbDV5RUNWbTJGeHB0amdmTU9FL3FPVmRQTmQ4Y0RuL0JydW9lVk5DN0Q4L0Z5TVRUMVVr'

"""links=requests.get(url3).text
html=etree.HTML(links)
tiqu=html.xpath('//*[@id="theme_custom_storage-0-download-pwd"]/@value')
print(tiqu)
#print(links)
link=html.xpath('/html/body/div[4]/div/div[3]/fieldset/div/div[2]/a/@href')
print(link)"""
