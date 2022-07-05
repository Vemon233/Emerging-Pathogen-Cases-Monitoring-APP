from datetime import datetime, timedelta
archdate = '20220705'
archnum = 8704233
currdate = datetime.strptime(archdate, "%Y%m%d")
startdate = datetime.strptime('2022/07/01', "%Y/%m/%d")

archive = archdate + '.' + str(archnum)
print(archive)
while currdate > startdate:
    currdate = currdate - timedelta(days=1)
    archdate = currdate.strftime("%Y%m%d")
    print(archdate)
