# coding=utf-8
# !
# -------------------------------------------------------------------------------
# Description :constraint handler for aspira constraint
#
# Pre-requests: n/a
# History     :
# DATE        AUTHOR          DESCRIPTION
# ----------  ----------      ----------------------------------------------------
# 03/05/2018  - eliu2         - created
#
# @CopyRight  :
# -------------------------------------------------------------------------------

import os, re
import file_handler as fh


def run():
    # source script location
    src_dir = "E:\Work-RAOutdoors\CA\AspiraFocusDB\AspiraFocusDatabaseCodes\Databases\CA\Schema Objects\Tables\Constraints"
    # target script location
    tgt_dir = "E:\Work-RAOutdoors\CA\AspiraFocusDB\\UniversalDatabasesCodes\Databases\Constraints"

    if os.path.exists(src_dir) and os.path.exists(tgt_dir):
        files = os.listdir(src_dir)
        for f in files:
            file_name = os.path.join(src_dir, f)
            # only read trigger files
            if os.path.isfile(file_name):
                try:
                    fh.file_str_replace(file_name, 'GO', '')
                    fh.file_str_replace(file_name, 'go', '')
                    encoding_name = fh.get_file_encoding(file_name)
                    context = fh.get_file_context(file_name,encoding_name)
                    ex = re.compile(r"\[.*?\]+")
                    l = ex.findall(context)
                    constraint_name = l[2].replace('[', '').replace(']', '')
                    # fh.check_obj_name(constraint_name, f)
                    header = '''IF (OBJECT_ID(\'''' + constraint_name + '''\')) IS NULL
BEGIN
'''
                    tail = '''
PRINT concat('[INFO] ', convert(varchar,getdate(),120), ' - Created Constraint '''+constraint_name+'''...')                             
END;
GO
'''
                    new_context = header + context + tail

                    new_file_name = os.path.join(tgt_dir, f)
                    fh.write_file(new_file_name, new_context, 'utf-8')
                    # print('{} {}'.format(f, constraint_name))
                except:
                    print(f)
                    # pass







