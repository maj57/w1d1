from datetime import date 
def age(x):
    months = x//30
    days = x
    hours = days*24
    minutes = hours*60
    return 'months :', months, 'days :', days,'hours :', hours,'minutes :', minutes

def agecalc(yr,mo,da):
    my = date(yr,mo,da)
    ttb = abs(my - date.today()).days
    return age(ttb)


