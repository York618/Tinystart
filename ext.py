# TinyStart Extonsion file.

def get_line_context(files_path, lines_number):
    # Extension:Read Line In File , V1.0
    # Writted by York618
    # This is a necessary component
    import linecache
    return linecache.getline(files_path, lines_number).strip()

def greet_with_time():
    # Extension:Greet With Time , V1.0
    # Writted by York618
    # This is a necessary component
    from interval import Interval
    import getpass,time
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

