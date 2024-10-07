# picasa-to-xnview-slideshow
Read ini files produced by Picasa tool to create the picture list to create a slideshow for XnViewMP tool.  

Usage
-----

usage: ini_to_sld.py [-h] [-f FOLDER_PATH] [-r {and,or}] [-c CONTACTS] [-o OUTPUT] [-v]

options:  
  -h, --help. Descrition: show this help message and exit.  
  -f FOLDER_PATH, --folder-path FOLDER_PATH. Descrition: Folder path.  
  -r {and,or}, --rule {and,or}. Descrition: rule to apply.  
  -c CONTACTS, --contacts CONTACTS. Descrition: contact list.  
  -o OUTPUT, --output OUTPUT. Descrition: SlideShow output file.  
  -v, --verbose. Descrition: increase output verbosity.  

Running command line
--------------------

Type the command after the dollar sign and hit enter:

```
$ python .\src\ini_to_sld.py -f C:\PicturesFolder -o slideshow
ini_to_sld - INFO - SlideShow file is 'C:\picasa-to-xnview-slideshow\output\slideshow.sld'
```
```
$ python .\src\ini_to_sld.py -f C:\PicturesFolder -c "contact1,contact2" -r and -o slideshow -v
ini_to_sld - INFO - SlideShow file is 'C:\picasa-to-xnview-slideshow\output\slideshow.sld'
```
