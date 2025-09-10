



def Time(milliseconds=0, seconds=0, minutes=0, hours=0, days=0):
    total = ((((days*24) + hours*60) + minutes*60) + seconds*1000) + milliseconds
    # day = (week*7) + day
    # hour = (day*24) + hour
    # minute = (hour*60) + minute
    # second = (minute*60) + second
    # millisecond = (second*1000) + millisecond
    milliseconds = int((total % 1000))
    seconds = int((total / 1000) % 60)
    minutes = int((total / (1000 * 60)) % 60)
    hours = int((total / (1000 * 60 * 60)) % 24)
    days = int(total / (1000 * 60 * 60 * 24))
    # return (milliseconds, seconds, minutes, hours, days, total)
    return {
        "mill": milliseconds,
        "sec": seconds,
        "min": minutes,
        "hour": hours,
        "day": days,
        "total": total,
    }
