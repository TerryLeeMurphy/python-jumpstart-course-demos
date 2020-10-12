import headers
import os
import shutil
import requests
import platform
import subprocess

# #########################           Globals          ######################
ds =72                                                                      # Console Width for Display
title = ' C u t e  C a t s '                                                # app title
url = 'http://consuming-python-services-api.azurewebsites.net/cats/random'  # web location for cats
subfolder = 'cats'                                                             # local folder to store results

def main():
    headers.print_header(title, ds)
    folder = create_folder()
    download_cats(folder)
    display_cats(folder)
    headers.print_header('Goodbye', ds)

def create_folder():

    pathname = os.path.abspath(os.path.dirname(__file__))
    full_pathname = os.path.join(pathname, subfolder)
    if not os.path.exists(full_pathname) or not os.path.isdir(full_pathname):
        print('Create Folder {} ... '.format(full_pathname))
        os.mkdir(full_pathname)

    return full_pathname

def download_cats(folder):
    print('connect server to download cats . . .')
    cat_count = 18
    for i in range(1, cat_count +1):
        name = 'lolcat_{}'.format(i)
        print('Downloading Cat ' + name)
        get_cat(folder, name)

    print('Done')

def get_cat(folder, name):
 #   url = 'http://consuming-python-services-api.azurewebsites.net/cats/random'
    data = get_data_from_url(url)
    save_image(folder, name, data)


def get_data_from_url(url):
    response = requests.get(url, stream=True)
    return response.raw


def save_image(folder, name, data):
    file_name = os.path.join(folder, name + '.jpg')
    with open(file_name, 'wb') as fout:
        shutil.copyfileobj(data, fout)

def display_cats(folder):
    print('Opening Folder ... ')
    if platform.system() == 'Darwin':
        subprocess.call(['open', folder])
    elif platform.system() == 'Windows':
        subprocess.call(['explorer', folder])
    elif platfrom.syste() == 'Linux':
        subprocess.call(['xdg-open', folder])
    else:
        print('This program does not support ' + platform.system())


if __name__ == '__main__':
    main()
