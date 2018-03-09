# coding=utf-8
# !
# -------------------------------------------------------------------------------
# Description :table handler for aspira tables
#
# Pre-requests: n/a
# History     :
# DATE        AUTHOR          DESCRIPTION
# ----------  ----------      ----------------------------------------------------
# 03/02/2018  - eliu2         - created
#
# @CopyRight  :
# -------------------------------------------------------------------------------

import re,os
import chardet
from shutil import copy, move



def get_file_encoding(path):
    with open(path,'rb') as f:
        data = f.read()
        encoding = chardet.detect(data)["encoding"]
    return encoding


def get_file_context(path, encoding):
    with open(path, 'r', encoding=encoding) as f:
        context = f.read()
    return context


def read_file(path):
    encoding = get_file_encoding(path)
    return get_file_context(path, encoding)


def write_file(path, context, encoding='utf-8', mode='w'):
    with open(path, mode, encoding=encoding) as f:
        f.write(context)


def check_obj_name(obj_name, file_name):
    """debug code below 3 rows"""
    name = obj_name.replace('dbo', '')
    if re.search(name.lower(), file_name.lower()) is None:
        print('{} {}'.format(obj_name, file_name))


def file_str_replace(f, old_str, new_str):
    coding = get_file_encoding(f)
    ex = '^' + old_str + '$'
    reg = re.compile(ex)
    with open(f, 'r', encoding=coding) as rf:
        r_lines = rf.readlines()
        with open(f, 'w', encoding=coding) as wf:
            for line in r_lines:
                if reg.findall(line):
                    wf.write(new_str)
                else:
                    wf.write(line)


def move_files(src_files, parent_folder):
    for f in src_files:
        move(f, parent_folder)


def clear_folder(path):
    files = os.listdir(path)
    for f in files:
        p = os.path.join(path, f)
        os.remove(p)
