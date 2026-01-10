import time

def print_time():
    strf = "%Y-%m-%d %H:%M:%S"
    twelve_hours_ago = time.time() - 12 * 60 * 60
    print(time.strftime(strf, time.localtime()))
    print(twelve_hours_ago)
    
print_time()
