# Tiny_start config and install tool
# Before running this config tool,you should check these softwares: 在运行配置工具之前，你需要检查这些软件
# Python >=3.5 Python版本必须大于或等于3.5
# requests >= 2.23 requests版本必须大于或等于2.23
import urllib,os

os.system('pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pip -U')
os.system('pip install -i https://pypi.tuna.tsinghua.edu.cn/simple requests')
os.system('pip install -i https://pypi.tuna.tsinghua.edu.cn/simple interval')

import requests
url = "https://sourl.cn/FxkJXd"
f=requests.get(url)
with open("config.py","wb") as code:
    code.write(f.content)

configname = 'config.conf'
print('Tiny_start 配置向导')
# 获取本机IP
try:
    city_ip_url = 'http://ip-api.com/json/?lang=zh-CN'
    city_ip_query = requests.get(city_ip_url)
    city_ip_dict = city_ip_query.json()
    city_ip = city_ip_dict['query']
except:
    print('哟唷！出错了，请浏览器访问“'+ city_dict_url +'”尝试')
    print('如果出错请检查网络 \n如果浏览器可以访问请重试 \n如果不行请上报issue')

# 获取IP归属地
try:
    city_dict_url = "http://ip-api.com/json/" + city_ip + "?lang=zh-CN"
    city_dict_query = requests.get(city_dict_url)
    city_dict = city_dict_query.json()
    local_city = city_dict['city']
except:
    print('哟唷！出错了，请浏览器访问“'+ city_dict_url +'”尝试')
    print('如果出错请检查网络，环境 \n如果浏览器可以访问请重试 \n如果不行请上报issue')

key = input('请输入和风天气应用api的key，没有请按照注册：')
lx = str(input('1.普通用户 \n2.付费用户 \n请选择：'))


if lx == '1':
    local_url = 'https://geoapi.heweather.net/v2/city/lookup?location=' + local_city + '&key=' + key
    local_query = requests.get(local_url)
    local_dict = local_query.json()
    local_list = local_dict['location']
    for list in local_list:
        print('区名：' + list['name'])
        print('经度：' + list['lon'])
        print('纬度：' + list['lat'])
    get_lon = str(input('请输入你所在区的经度：'))
    get_lat = str(input('请输入你所在区的纬度：'))
    test_weather_url = 'https://devapi.heweather.net/v7/weather/now?location='+ get_lon+ ','+ get_lat+'&key='+ key
    test_weather_query = requests.get(test_weather_url)
    test_weather_dict = test_weather_query.json()
    test_weather_now_dict = test_weather_dict["now"]
    print('测量时间：'+test_weather_now_dict['obsTime'])
    print('实际温度：'+test_weather_now_dict['temp'])
    print('体感温度：'+test_weather_now_dict['feelsLike'])
    print('天气实况：'+test_weather_now_dict['text'])
    jz = str(input('这是否正确？(y/n):'))
    if jz == 'y':
        with open(configname, 'w') as file_object:
            file_object.write(key +'\n')
            file_object.write(get_lon +'\n')
            file_object.write(get_lat +'\n')
    elif jz == 'n':
        print('请检查网络是否良好，环境是否正确，经纬是否正确，然后重试\n')
        print('或者访问"'+ test_weather_url+ '"尝试')
        exit()

elif lx == '2':
    local_url = 'https://geoapi.heweather.net/v2/city/lookup?location=' + local_city + '&key=' + key
    local_query = requests.get(local_url)
    local_dict = local_query.json()
    local_list = local_dict['location']    
    for list in local_list:
        print('区名：' + list['name'])
        print('经度：' + list['lon'])
        print('纬度：' + list['lat'])
    get_lon = str(input('请输入你所在区的经度：'))
    get_lat = str(input('请输入你所在区的纬度：'))
    test_weather_url = 'https://api.heweather.net/v7/weather/now?location='+ get_lon+ ','+ get_lat+'&key='+ key
    test_weather_query = requests.get(test_weather_url)
    test_weather_dict = test_weather_query.json()
    test_weather_now_dict = test_weather_dict["now"]
    print('测量时间：'+test_weather_now_dict['obsTime']+ '\n实际温度：'+test_weather_now_dict['temp']+ '体感温度：'+test_weather_now_dict['feelsLike'])
    print('天气实况：'+test_weather_now_dict['text'])
    jz = str(input('这是否正确？(y/n):'))
    if jz == 'y':
        with open(configname, 'w') as file_object:
            file_object.write(key +'\n')
            file_object.write(get_lon +'\n')
            file_object.write(get_lat +'\n')
    elif jz == 'n':
        print('请检查网络是否良好，经纬是否正确，然后重试')
        print('或者浏览器访问"'+ test_weather_url+ '"尝试')
        exit()
