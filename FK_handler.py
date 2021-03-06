# coding=utf-8
# !
# -------------------------------------------------------------------------------
# Description :FK handler for aspira FKs
#
# Pre-requests: n/a
# History     :
# DATE        AUTHOR          DESCRIPTION
# ----------  ----------      ----------------------------------------------------
# 03/02/2018  - eliu2         - created
#
# @CopyRight  :
# -------------------------------------------------------------------------------

import os, re
import file_handler as fh


def run():
    # source script location
    src_dir = "E:\Work-RAOutdoors\CA\AspiraFocusDB\AspiraFocusDatabaseCodes\Databases\CA\Schema Objects\Tables\Keys"
    # target script location
    tgt_dir = "E:\Work-RAOutdoors\CA\AspiraFocusDB\\UniversalDatabasesCodes\Databases\ForeignKeys"

    if os.path.exists(src_dir) and os.path.exists(tgt_dir):
        files = os.listdir(src_dir)
        for f in files:
            file_name = os.path.join(src_dir, f)
            # only read pkey files
            if os.path.isfile(file_name) and re.search(r'fkey', f) is not None:
                try:
                    fh.file_str_replace(file_name, 'GO', '')
                    fh.file_str_replace(file_name, 'go', '')
                    encoding_name = fh.get_file_encoding(file_name)
                    context = fh.get_file_context(file_name,encoding_name)
                    ex_table = re.compile(r"\[.*?\]+")
                    l = ex_table.findall(context)
                    if l[0].replace('[','').replace(']','') != 'dbo':
                        print(1/0)
                    table_name = l[1].replace('[','').replace(']','')
                    fk_name = l[2].replace('[','').replace(']','')
                    # if re.search('FK_' , fk_name) is None:
                    #     fh.check_obj_name(fk_name, f)
                    header = '''IF NOT EXISTS
(
    SELECT TOP 1 1
    FROM sys.foreign_keys fk
    WHERE OBJECT_ID = OBJECT_ID(N\'''' + fk_name + '''\')
          AND fk.parent_object_id = OBJECT_ID(N\'''' + table_name + '''\')
)
BEGIN
'''
                    tail = '''
PRINT concat('[INFO] ', convert(varchar,getdate(),120), ' - Created Foreign Key '''+ fk_name+'''...')                      
END;
GO
'''
                    new_context = header + context + tail

                    new_file_name = os.path.join(tgt_dir, f)
                    fh.write_file(new_file_name, new_context, 'utf-8')

                    # print('{} {} {}'.format(f,table_name,pk_name))
                except:
                    print(f)






