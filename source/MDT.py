import datetime

def is_dst(date):
    start_dst = datetime.datetime(date.year, 3, 31)
    start_dst -= datetime.timedelta(days=start_dst.weekday() + 1)
    end_dst = datetime.datetime(date.year, 11, 30)
    end_dst -= datetime.timedelta(days=end_dst.weekday() + 1)
    return start_dst <= date <= end_dst
def get_mdt_time():
    now = datetime.datetime.now()
    if is_dst(now):
        mdt_offset = -6
    else:
        mdt_offset = -7
    mdt_time = now + datetime.timedelta(hours=mdt_offset)
    return mdt_time
#mdt_time = get_mdt_time()
#print("MDT Time:", mdt_time.strftime('%Y-%m-%d %H:%M:%S'))