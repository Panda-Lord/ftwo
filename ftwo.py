"""
Windows files renaming tool.
The initial idea is that it works similar to 'Find and Replace' in Microsoft Excel, but with for Window Explorer.
"""

import os
import argparse

class FileRename():
    """
    File renaming class.
    """
    def __init__(self, file):
        self.file = file
        self.name, self.extension = os.path.splitext(self.file)

    def change_name(self, parsed_args):
        """
        Replacing string within the file name, with possible args below as part of a string;
        'whole' - exact, to specify that the full file name has to be exact match.
        'exact' - whole, to specify that the whole name is to be replaced if any part of the string produces match.
        If 'exact' is True, this by logic makes 'w' True regardless of input
        """
        def change():
            try:
                if parsed_args.whole:
                    new_name = parsed_args.new_string + self.extension
                else:
                    new_name = self.name.replace(parsed_args.old_string, parsed_args.new_string) + self.extension
                os.rename(self.file, new_name)
                if self.file != new_name:
                    print(f"'{self.file}' -> '{new_name}'")
                    return True
            except FileExistsError:
                print(f"'{self.file}' -> '{new_name}' : file already exists. name not changed")
                return False

        if parsed_args.exact and parsed_args.old_string == parsed_args.new_string:
            return change()
        elif parsed_args.old_string in self.file:
            return change()

def parsing_args():
    parser = argparse.ArgumentParser()

    parser.add_argument("path", help="Targeted path")

    parser.add_argument("old_string", help ="String that is to be replaced")
    
    parser.add_argument("new_string", help ="String to replace with")

    parser.add_argument('-e', '--exact', action='store_true',
                    help='Specifies whether the file name is to be exact match')
    parser.add_argument('-w', '--whole', action='store_true',
                    help='Specifies whether the file name is to be fully replaced if any part is a match')
    
    return parser.parse_args()

class Main():
    """
    Application start and working directory set up
    """
    parsed_args = parsing_args()
    path = parsed_args.path
    os.chdir(path)
    files = os.listdir(path)

    print(f"...\nftwo found {len(files)} in {path}")
    if parsed_args.exact:
        method = " for full name exact match only"
    elif parsed_args.whole:
        method = " as whole new name for any match with old string"
    else:
        method = ""
    print(f"replacing string '{parsed_args.old_string}' with '{parsed_args.new_string}'{method}\n...\nreplacing:")

    pass_count = 0
    fail_count = 0
    for file in files:
        status = FileRename(file).change_name(parsed_args)
        if status == True:
            pass_count += 1
        elif status == False:
            fail_count += 1
    
    print(f"...\nreplaced total of {pass_count} files. {fail_count} files failed")


Main()