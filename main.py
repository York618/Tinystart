# Tiny_start
# A easy tool to know this world when you open the computer. 一个让你在打开电脑时了解这个世界的简单工具
# No ADs,Just weather and news. 没有广告，只有天气和新闻
# Before running this program,you should check these softwares: 在运行之前，你需要检查这些软件
# Python >=3.5 Python版本必须大于或等于3.5
# pip >=20 pip版本必须大于或等于20
# requests >= 2.23 requests版本必须大于或等于2.23
# interval >=1.0 interval版本必须大于或等于1.0
import requests,linecache,time,getpass

import ext

ext.greet_with_time()
file_path = 'config.conf'
line_number = 1
a_type = ext.get_line_context(file_path, line_number)
line_number += 1
a_key = ext.get_line_context(file_path, line_number)
line_number += 1
a_lon = ext.get_line_context(file_path, line_number)
line_number += 1
a_lat = ext.get_line_context(file_path, line_number)

if a_type == '1':
    weather_url = 'https://devapi.heweather.net/v7/weather/now?location='+ str(a_lon)+ ','+ str(a_lat)+ '&key='+ str(a_key)
    weather_query = requests.get(weather_url)
    weather_dict = weather_query.json()
    weather_now = weather_dict['now']
    print('\n现在天气：'+ weather_now['text'])
    print('气温：'+ weather_now['temp'])
    print('体感温度：'+ weather_now['feelsLike'])
    print('风向：'+ weather_now['windDir'])
    print('风速：'+ weather_now['windSpeed']+ 'km/s')
    print('相对湿度：'+ weather_now['humidity']+ '%')
    print('详细链接：'+ weather_dict['fxLink'])
elif a_type == '2':
    weather_url = 'https://api.heweather.net/v7/weather/now?location='+ str(a_lon)+ ','+ str(a_lat)+ '&key='+ str(a_key)
    weather_query = requests.get(weather_url)
    weather_dict = weather_query.json()
    weather_now = weather_dict['now']
    print('现在天气：'+ weather_now['text'])
    print('气温：'+ weather_now['temp'])
    print('体感温度：'+ weather_now['feelsLike'])
    print('风向：'+ weather_now['windDir'])
    print('风速：'+ weather_now['windSpeed']+ 'km/s')
    print('相对湿度：'+ weather_now['humidity']+ '%')
    print('详细链接：'+ weather_dict['fxLink'])

