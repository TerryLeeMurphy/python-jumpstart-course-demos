def dashes_line(width):
    """a function that prints a line of dashes to the width that is given"""
    for x in range(width):
        print('-', end='')
    print()


def print_title(title, width):
    """a function the prints a title centered across a given width"""
    offset = int((width - (len(title)))/2)
    if offset < 0:                     # Check to see if the title is too long
        offset = 0
    for x in range(offset):
        print(' ', end='')
    print(title)

def print_header(title, width):
    dashes_line(width)
    print_title(title, width)
    dashes_line(width)
    print ()



