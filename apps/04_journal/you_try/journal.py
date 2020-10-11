""" Journal Module
    Handles all File I/O for the Journary """
import os

def load(name):
    """ load a new journal file

    :param name : the name of the file to load
    :return     : a data structure populated with file data """
    data = []
    rows = 0
    filename = get_full_pathname(name)
    print('Loading Your Journal from {}'.format(filename))
    if os.path.exists(filename):
        with open(filename) as fin:
            for entry in fin.readlines():
                data.append(entry.rstrip())
                rows = rows + 1

    print('{} entriesloaded'.format(rows))
    return(data)


def save(name, journal_data):
    filename = get_full_pathname(name)
    print("..... saving to: {}".format(filename))

    with open(filename, 'w') as fout:
        for entry in journal_data:
            fout.write(entry + '\n')


def get_full_pathname(name):
    filename = os.path.abspath(os.path.join('.', 'journals', name + '.jrl'))
    return filename


def add_entry(text, journal_data):
    journal_data.append(text)
