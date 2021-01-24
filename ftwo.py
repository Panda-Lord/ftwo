"""
Windows files renaming tool.
The initial idea is that it works similar to 'Find and Replace' in Microsoft Excel
"""

import os

class FileInfo():
    """
    Anything to do with renaming of the file.
    """
    
    def __init__(self, filepath):
        self.full_name = filepath
        self.name = os.path.basename(filepath)
        self.directory, self.extension = os.path.splitext(filepath)

