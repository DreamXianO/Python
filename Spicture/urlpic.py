import requests
import datetime
def calc(size):
    size /=1048576
    return size
i = int(input("输入次数:"))
url = 'https://iw233.cn/API/Random.php'
for i in range(1,i+1):
    print("正在下载……第%d张" % i)
    time = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    res = requests.get(url)
    size = calc(len(res.content))
    with open("%s-%d.jpg" % (time,i),'wb') as f:
        f.write(res.content)
    print("Done! %.2fMb" % size)
print("下载了%d张图片" % i)