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
        Replacing string within the file name whilist checking for parsed arguements to alter the method
        """
        def change():
            try:
                
                if parsed_args.whole:
                    new_name = parsed_args.new_string
                else:
                    new_name = self.name.replace(parsed_args.old_string, parsed_args.new_string)
                os.rename(self.file, new_name + self.extension)

                if self.file != new_name:
                    print(f"'{self.file}' -> '{new_name}{self.extension}'")
                    return True

            except FileExistsError:

                if parsed_args.numbering == True:
                    duplicate = 1
                    while duplicate < 999:
                        try:
                            os.rename(self.file, new_name + f" ({duplicate})" + self.extension)
                            print(f"'{self.file}' -> '{new_name} ({duplicate}){self.extension}'")
                            return True
                        except FileExistsError:
                            duplicate += 1

            print(f"'{self.file}' -> '{new_name}' : File already exists. Name not changed")
            return False

        if parsed_args.exact and parsed_args.old_string == parsed_args.new_string:
            return change()
        elif parsed_args.old_string in self.file:
            return change()

def parsing_args():
    parser = argparse.ArgumentParser()

    parser.add_argument("path", help="Targeted folder path")

    parser.add_argument("old_string", help ="Old string that is to be replaced")
    
    parser.add_argument("new_string", help ="New string to replace with")

    parser.add_argument('-e', '--exact', action='store_true',
                    help='Specifies whether the full file name is to be exact match')
    parser.add_argument('-w', '--whole', action='store_true',
                    help='Specifies whether the file name is to be fully replaced with new string if any part is a match')
    parser.add_argument('-n', '--numbering', action='store_true',
                    help='Attempts to sequentially number the files if a file with that name already exists')
    
    return parser.parse_args()

class Main():
    """
    Application start and working folder directory set up
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
    print(f"Renaming string '{parsed_args.old_string}' with '{parsed_args.new_string}'{method}\n...\nRenaming:")

    pass_count = 0
    fail_count = 0
    for file in files:
        status = FileRename(file).change_name(parsed_args)
        if status == True:
            pass_count += 1
        elif status == False:
            fail_count += 1
    
    print(f"...\nRenaming total of {pass_count} files. {fail_count} files failed")


if __name__ == "__main__":
    Main()