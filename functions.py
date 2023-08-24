import os

def print_directory_tree(directory, indent=''):
    print(indent + directory)
    if os.path.isdir(directory):
        items = os.listdir(directory)
        for item in items:
            item_path = os.path.join(directory, item)
            if os.path.isdir(item_path):
                print_directory_tree(item_path, indent + '  ')
            else:
                print(indent + '  ' + item)