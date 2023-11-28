

hours = input('Enter hours:')
rate = input('Enter rate per hour:')
min_hours = 40
extra_rate = 1.5
try:
    total_hours = float(hours)
    rate_per_hour = float(rate)
    #pay = float(hours) * float(rate)
    if total_hours <= min_hours:
        print('up to', min_hours, 'hours')
        pay = total_hours * rate_per_hour
    else:
        print('more then', min_hours, 'hours')
        min_hours_pay = min_hours * rate_per_hour
        print('min hours to pay', min_hours_pay)
        extra_hours = total_hours - min_hours
        print('total extra hours is', extra_hours)
        extra_hours_pay = extra_hours * rate_per_hour * extra_rate
        print('extra hours to pay', extra_hours_pay)
        #print('Extra hours pay is', extra_hours * r * 1.5)
        pay = min_hours_pay + extra_hours_pay
except:
    pay = -1

print('Pay:', pay)