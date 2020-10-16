import os
import collections
import headers

# Globals #
ds = 72                                                                        # Set Display Width
title = 'File Searcher'                                                        # Display Title
SearchResult = collections.namedtuple('SearchResult', 'file, line, text')      # Output Collection


def get_folder():
    folder = input('Please Enter a folder name to search:')
    if not folder or not folder.strip():
        return None

    if not os.path.isdir(folder):
        return None

    return folder


def get_search_text():
    text = input("Please enter the text your are looking for: ")
    return text.lower

def search_folders(folder, text):
    items = os.listdir(folder)
    for item in items:
        full_file_name = os.path.join(folder, item)
        if os.path.isdir(full_file_name):     # if this a directory in the the do a recursive call back to the same function
            yield from search_folders(full_file_name,text)
        else:
            yield from search_files(full_file_name, text)

def search_files(name, text):
    try:

        with open(name,'r', encoding='utf-8') as fin:
            line_num = 0
            for line in fin:
                line_num += 1
                if line.lower().find(text) >= 0:
                    m = SearchResult(line=line_num, file=name, text=line)
                    print(m)
                    yield m

    except UnicodeDecodeError:
        print('Warning:  Binary file being skipped {}'.format(name))


def main():
    headers.dashes_line(ds)
    headers.print_header(title,ds)
    headers.dashes_line(ds)
    folder = get_folder()
    if not folder:
        print('We cannot search {}'.format(folder))
        return
    print()
    text = get_search_text()
    if not text:
        print("Sorry, but we cannot look for nothing")
        return
    matches = search_folders(folder, text)
    match_count = 0
    for m in matches:
        match_count += 1
        #print(m)
        #print('Match Found in {}'.format(m.file))

    print()
    headers.dashes_line(ds)
    print('Matched in {} files'.format(match_count))
    headers.dashes_line(ds)
    headers.print_header('Goodbye', ds)

if __name__ == '__main__':
    main()

