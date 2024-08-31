from datetime import datetime, date

closing_time = "20:30:00"
opening_time = "9:00:00"

now = datetime.now().strftime("%H:%M:%S")


# if now > closing_time:
#     print("past now")
# else:
#     print("not 8")

# if date.isoweekday(datetime.now()) ==6:
#     print("weekend")

if date.isoweekday(datetime.now()) == 6 or date.isoweekday(datetime.now()) == 7:
    print("We are closed")

elif now.strftime("%H:%M:%S") > closing_time or now.strftime("%H:%M:%S") < opening_time:
    print("we are closed")

# print(date.isoweekday(datetime.today()))

