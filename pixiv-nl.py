import requests 
import os
def calc(size):
    size /=1048576
    return size
id = str(input("请输入pid:"))
url = 'https://www.pixiv.nl/'+ id+'.png'
res = requests.get(url)
i=0
pic = res.content
size = calc(len(pic))
name = id+'_' + str(i) + '.png' 
with open(name,'wb') as f:
    f.write(pic)
if(size<0.01):
    print("Too Small!ERROR!仅 %.2fMb!!!" % size)
    os.system('del /s /q '+name)
else:
    print("Done! %.2fMb" % size)
    