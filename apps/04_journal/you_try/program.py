""" main program for control the journal module """
import headers
import journal


def list_entries(data):
    print('Your journal entries: ')
    entries = reversed(data)
    for idx, entry in enumerate(entries):
        print('* [{}] {}'.format(idx + 1, entry))


def add_entry(data):
    text = input('Type your entry, <enter> to exit: ')
    journal.add_entry(text, data)
    # data.append(text)


def event_loop(journal_name, data):
    ds = 72
    headers.dashes_line(ds)
    print('What do you want to do?')
    action = ' '
    while action != 'X':
        action = input('Please enter [L]ist, [A]dd, or e[X]it :')
        action = action.upper().strip()  # forces input to upper case
        if action == 'L':
            list_entries(data)
        elif action == 'A':
            add_entry(data)
        elif action == 'X':
            journal.save(journal_name, data)
            print('Goodbye')
        else:
            print('Input of {} is unknown'.format(action))

def main():
    """  Journal by T. Murphy                             10/3/2020
    program to practice import your own modules and doing file i/o """
    ds = 72
    title = 'Journal'
    journal_name = 'my-journal'
    headers.dashes_line(ds)
    headers.print_header(title, ds)
    data = journal.load(journal_name)
    event_loop(journal_name, data)
    # list_entries(data)
    # add_entry(data)
    # journal.save(journal_name, data)

if __name__ == '__main__':
    main()
