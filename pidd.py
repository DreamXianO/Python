import requests 
import os
import re
id = str(input("请输入pid:"))
url = 'https://www.pixiv.net/artworks/'+ id
print(url)
res = requests.get(url)
re = re.findall('https://i.pximg.net/img-original/img/.+?jpg',res.text)
i=0
for x in re:
    x = x.replace('pximg.net', 'pixiv.cat')
    print(x)
    pic = requests.get(x)
    name = id+'_' + str(i) + '.jpg' 
    i+=1
    with open(name,'wb') as f:
        f.write(pic.content)