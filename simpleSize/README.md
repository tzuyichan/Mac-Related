## What does `simpleSize` do?
`simpleSize` lists how big the top-level items (files, folders) are in a given directory. The contents are listed in descending order, largest item first.
```
/sample/folder/
         File    Type      Size
1        venv  folder  93881064
2        .git  folder     34765
3   .DS_Store    file      6148
4  simpleSize  folder      3319
5  .gitignore    file        24
```

## How to use?
Run `list_contents.py` and provide either the relative path or full path of the directory you want to inspect. The relative path is calculated from the current
working directory the user is in.
```bash
python list_contents.py ~/sample/folder

         File    Type      Size
1        venv  folder  93881064
2        .git  folder     34765
3   .DS_Store    file      6148
4  simpleSize  folder      3319
5  .gitignore    file        24
```
You can also specify the unit for the file size. Choices include `gib`, `mib`, `kib`, `gb`, `mb`, `kb`. If not specified, file size is displayed in *bytes*.
```bash
python list_contents.py ~/sample/folder -u kib

Size unit: kib
         File    Type     Size
1        venv  folder  91680.7
2        .git  folder     34.0
3   .DS_Store    file      6.0
4  simpleSize  folder      4.2
5  .gitignore    file      0.0
```
## Dependencies
- pandas