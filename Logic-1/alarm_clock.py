def alarm_clock(day, vacation):
    return "off" if (vacation and (day==0 or day==6)) else "7:00" if (not vacation and (day>0 and day<6)) else "10:00"