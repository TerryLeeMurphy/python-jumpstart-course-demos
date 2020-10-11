import datetime


def dashes_line(width):
    for x in range(width):
        print('-', end='')
    next
    print()


def print_header(title, width):
    offset = int((width - (len(title)))/2)
    if offset < 0:                     # Check to see if the title is too long
        offset = 0
    for x in range(offset):
        print(' ', end='')
    next
    print(title)


def user_input():
    print()
    print('Please Enter Your Birthday')
    year = int(input('What Year where you born? '))
    month = int(input('What Month where you born?'))
    day = int(input('What Day where you born?'))
    birthday = datetime.date(year, month, day)
    return birthday

def days_between_dates(orig, target):
    this_year = datetime.date(target.year, orig.month, orig.day)
    t1 = this_year - target
    return t1.days

def user_output(days):
    if days > 0:
        message = "{} days til your birthday".format(days)
    elif days < 0:
        message = "{} days since your birthday".format(-days)
    else:
        message = "Today is your Birthday, Happy Birthday"
    return message

def main():
    ds = 72                             # Screen Console Width
    title = 'Y o u r B i r t h d a y'   # Program Title
    dashes_line(ds)
    print_header(title,ds)
    dashes_line(ds)
    # birthday = user_input()

    today = datetime.date.today()
    # verify my functions here ...
    birthday = datetime.date(1965, 8, 27)
    days = days_between_dates(birthday, today)
    print(user_output(days))
    birthday = datetime.date(1965, 10, 3)
    days = days_between_dates(birthday, today)
    print(user_output(days))
    birthday = datetime.date(1965, 12, 28)
    days = days_between_dates(birthday, today)
    print(user_output(days))



main()
