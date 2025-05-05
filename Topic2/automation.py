'''
Practicing writing automation scripts using python.
In this file I will practice the use of 1) The os module, 2) Writing and Reading files, 3) RegEx, 4) User Input.
I will also be using concepts from Topic1(Basic syntax, decorators, functions, lists, etc)

Project Summary
------------------
1. Ask the user to enter a file path (check)
2. If the path exists, proceed to organize (check)
3. Organise the path 
4. If the path doesn't exist, inform user and ask them to restart process
'''
import os
import csv
import datetime
import re

def greeting(func):
    def wrapper(*args, **kwargs):
        print("Welcome to my automation practice script")
        return func(*args, **kwargs)
    return wrapper

@greeting
def get_path():
    option = input("Enter 1 for file organisation, 2 for sub-category organisation: ")
    path = input("Enter the path you want to organise: ")
    return (path, option)

def check_path(path, option):
    if os.path.exists(path):
        print("The path exists, proceeding to organise.")
        match option:
            case '1':
                organise_path(path)
            case '2':
                organise_files(path)
    else:
        print("Please enter a path that exists.")

def organise_path(path):
    '''
    Put files with the same extension in the same folder
    Files: .txt, .rtf, .
    Videos: .mp4, .mov
    '''
    for file in os.listdir(path):
        full_path = os.path.join(path, file)
        if os.path.isfile(full_path):
            ext = os.path.splitext(file)[1].lower()

            # Organise documents
            if ext in ['.txt', '.rtf', '.docx', '.pdf']:
                new_dir = os.path.join(path, 'Files')
                os.makedirs(new_dir, exist_ok=True)
                new_path = os.path.join(new_dir, file)

                os.rename(full_path, new_path)
                write_log({'fromPath':full_path, 'toPath':new_path})
                print(f'File: {file} has been moved to {new_path}')
                print()
            
            # Organise videos
            elif ext in ['.mp4', '.mov']:
                new_dir = os.path.join(path, 'Videos')
                os.makedirs(new_dir, exist_ok=True)
                new_path = os.path.join(new_dir, file)

                os.rename(full_path, new_path)
                write_log({'fromPath':full_path, 'toPath':new_path})
                print(f'File: {file} has been moved to {new_path}')
                print()
            
            # Organise Audios
            elif ext in ['.mp3']:
                new_dir = os.path.join(path, 'Audio')
                os.makedirs(new_dir, exist_ok=True)
                new_path = os.path.join(new_dir, file)

                os.rename(full_path, new_path)
                write_log({'fromPath':full_path, 'toPath':new_path})
                print(f'File: {file} has been moved to {new_path}')
                print()
            
            # Organise Images
            elif ext in ['.png', '.jpeg', '.jpg', '.heic']:
                new_dir = os.path.join(path, 'Images')
                os.makedirs(new_dir, exist_ok=True)
                new_path = os.path.join(new_dir, file)

                os.rename(full_path, new_path)
                write_log({'fromPath':full_path, 'toPath':new_path})
                print(f'File: {file} has been moved to {new_path}')
                print()
            
            # Organise others
            else:
                new_dir = os.path.join(path, 'Others')
                os.makedirs(new_dir, exist_ok=True)
                new_path = os.path.join(new_dir, file)

                os.rename(full_path, new_path)
                write_log({'fromPath':full_path, 'toPath':new_path})
                print(f'File: {file} has been moved to {new_path}')
                print()
    print("All files have been organized. Check your Desktop log file for more information.")

def organise_files(path):
    '''
    Organise files depending on their names. 
    Example: Movies_Series_Hitman = Movies/Series/Hitman
    '''
    delimiter = '_'
    for file in os.listdir(path):
        full_path = os.path.join(path, file)
        if os.path.isfile(full_path):
            file_name = os.path.basename(full_path)

            # Set the file naming pattern and set names accordingly
            pattern = r"^([^_]+)_([^_]+)_(.+)$" # format: type_subtype_name
            match = re.match(pattern, file_name)

            if match:
                file_type = match.group(1)
                file_subtype = match.group(2)
                file_name = match.group(3)

                type_path = os.path.join(path, file_type)
                os.makedirs(type_path, exist_ok=True)

                sub_path = os.path.join(type_path, file_subtype)
                new_path = os.path.join(sub_path, file_name)
                os.makedirs(sub_path, exist_ok=True)

                os.rename(full_path, new_path)
                write_log({'fromPath': full_path, 'toPath': new_path})
                print(f"{file_name} was moved to {new_path}")
            else:
                print(f"{file_name} doesn't follow the type_subtype_name format for naming")
    print('All files have been moved, check your Desktop log file for more info.')

def create_log_file():
    path = os.path.join(os.environ.get('HOME'), 'Desktop')
    os.makedirs(path, exist_ok=True)
    file_path = os.path.join(path, 'File_Organiser_Log.csv')
    return file_path

def write_log(paths):
    log_path = create_log_file()
    with open(log_path, 'a') as log:
        logTitles = ['fileName', 'fromPath', 'toPath', 'Time']
        logWriter = csv.DictWriter(log, fieldnames=logTitles, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        
        if os.path.getsize(log_path) == 0:
            logWriter.writeheader()

        for fromPath, toPath in paths.items():
            fromPath = paths.get('fromPath')
            toPath = paths.get('toPath')
            if fromPath and toPath:
                fileName = os.path.basename(fromPath)
                logWriter.writerow({'fileName': fileName, 'fromPath':fromPath, 'toPath': toPath, 'Time':datetime.datetime.now()})
            else:
                print("Error writing the log file")

def main():
    path, option = get_path()
    check_path(path, option)

if __name__ == '__main__':
    main()