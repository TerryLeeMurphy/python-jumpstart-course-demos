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


def main():
    ds = 72                             # Screen Console Width
    title = 'Y o u r B i r t h d a y'   # Program Title
    dashes_line(ds)
    print_header(title,ds)
    dashes_line(ds)
    birthday = user_input()
    print(birthday)


main()
