# ftwo
Simple command line windows file renamer in Python. The idea behind this is similar to Excel 'find and replace', to find every matching string within the specified range and replace it with a new string.

Please note, extension of the file will not be replaced. It is simply removed and then added back on to the new name to avoid this.
Where a file name already existed, or has been created in the process, duplicates will not be touched. See numbering option to change this.

## Requirements & Installation
### Python 3
Yoy will need Python 3 -> <https://www.python.org/downloads/>

### Installation
Simply clone the repo. The folder does not matter in relation to files you want to rename.

## Usage
### Basics
Once in the command line, you will need to locate folder with *ftwo.py*, and then run the following with your own positional arguements

`python ftwo.py path old_string new_string`

Where:
* `path` is either path to your target folder with pictures, either absolute or relative to *ftwo.py*. Make sure to use quotation marks if your path has spaces. e.g. 'C:\Users\panda lord\'
* `old_string` is a string that you wish to replace.
* `new_string` is a string that you wish to replace *old_string* with.

ftwo will replace every string while keeping rest of the files name and extension as is.
Example below:

`python ftwo.py .\pictures square rectangle`

![ftwo.py example, figure 1](https://raw.githubusercontent.com/Panda-Lord/ftwo/main/figure_1.png)

### Options


* `-e, exact` adds an option where files name has to be exact match for swap to take place.

* `-w, whole` adds an option where file name is replaced entirely if any part of the file name prodcues a match. Please note this will likely create a duplicates and if you wish for them to be renamed with subsequent numbers, add below option. This option alone will simply rename only the first file.

* `-n, numbering` adds an option where any duplicates will be subsequently numbered in order. Exactly the same as Windows Explorer works if you give more than one file the same name.

## Footnote
This is my first github project as I am trying to learn. If you wish for me to add any functionality, have any problems or simply you have some feedback, just give me a shout!
