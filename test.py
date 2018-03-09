# coding = utf-8
import os,sys,chardet, file_handler as fh
import re
from shutil import move
moved_files = ['E:\\Work-RAOutdoors\\CA\\AspiraFocusDB\\UniversalDatabasesCodes\\Databases\\test.txt']
file_loc = 'E:\\Work-RAOutdoors\\CA\\AspiraFocusDB\\UniversalDatabasesCodes\\Databases\\SpecialScripts'


# fh.move_files(moved_files,file_loc)
for f in moved_files:
    move(f, file_loc)