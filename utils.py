conversion_month = {
    "January":1,
    "February":2,
    "March":3,
    "April":4,
    "May":5,
    "June":6,
    "July":7,
    "August":8,
    "September":9,
    "October":10,
    "November":11,
    "December":12
}

def convert(sr):
    date_month = sr.split()
    date = date_month[0]
    mon = conversion_month[date_month[1].title()]
    if len(str(date))!=2:
        date = f"0{date}"
    if len(str(mon)) != 2:
        mon = f"0{mon}"
    return f"{date}/{mon}/2026"