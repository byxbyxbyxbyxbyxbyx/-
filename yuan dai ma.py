#  源代码未经允许禁止转载！！！，只有Github有源代码！！！

from datetime import datetime as t
import time as timer
from PIL import Image                                           #导入所需要的库

while True:
    time = t.now()                                               #获取系统时间并处理时间
    h = time.strftime('%H')
    m = time.strftime('%M')
    s = time.strftime('%S')

    time = h+m+s                                                       #整合数据
    if time == '060000':
        print("yes")
        Img = Image.open('无标题.png')
        Img.show()
        timer.sleep(1)
    if time == '090000':
        print("no")                                                 #某个时间发生的事
        Img = Image.open('差.png')
        Img.show()
        timer.sleep(1)
    if time == '170000':
        print("Yes yes")
        Img = Image.open('无标题.png')
        Img.show()
        timer.sleep(1)
    if time == '200000':
        print("No No")
        Img = Image.open('差.png')
        Img.show()
        timer.sleep(1)
    print(time)                                                     #打印现在系统时间，不需要请告诉我们