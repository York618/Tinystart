# Tiny_start
# A easy tool to know this world when you open the computer. 一个让你在打开电脑时了解这个世界的简单工具
# No ADs,Just weather and news. 没有广告，只有天气和新闻
# Before running this program,you should check these softwares: 在运行之前，你需要检查这些软件
# Python >=3.5 Python版本必须大于或等于3.5
# pip >=20 pip版本必须大于或等于20
# requests >= 2.23 requests版本必须大于或等于2.23
# interval >=1.0 interval版本必须大于或等于1.0
import requests,linecache,time,getpass
from interval import Interval

user_now = getpass.getuser()
hour_now = int(time.strftime("%H", time.localtime()))
if hour_now in Interval(4, 9):
    print('早上好，'+ user_now)
elif hour_now in Interval(10, 12):
    print('中午好，'+ user_now)
elif hour_now in Interval(13, 17):
    print('下午好，'+ user_now)
elif hour_now in Interval(18, 21):
    print('晚上好，'+ user_now)
elif hour_now in Interval(22, 3):
    print('记得早点睡呀，'+ user_now)
print('现在时间是：'+ time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
file_path = 'E:\运生\新建文件夹\\tiny_start\config.conf'
line_number = 1
def get_line_context(files_path, lines_number):
     return linecache.getline(files_path, lines_number).strip()
key = get_line_context(file_path, line_number)
line_number += 1
lon = get_line_context(file_path, line_number)
line_number += 1
lat = get_line_context(file_path, line_number)
