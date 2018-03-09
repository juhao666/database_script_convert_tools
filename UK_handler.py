# coding=utf-8
# !
# -------------------------------------------------------------------------------
# Description :UK handler for aspira UKs
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
    tgt_dir = "E:\Work-RAOutdoors\CA\AspiraFocusDB\\UniversalDatabasesCodes\Databases\\UniqueKeys"

    if os.path.exists(src_dir) and os.path.exists(tgt_dir):
        files = os.listdir(src_dir)
        for f in files:
            file_name = os.path.join(src_dir, f)
            # only read ukey files
            if os.path.isfile(file_name) and re.search(r'ukey', f) is not None:
                try:
                    encoding_name = fh.get_file_encoding(file_name)
                    context = fh.get_file_context(file_name,encoding_name)
                    ex_table = re.compile(r"\[.*?\]+")
                    l = ex_table.findall(context)
                    if l[0].replace('[','').replace(']','') != 'dbo':
                        print(1/0)
                    table_name = l[1].replace('[','').replace(']','')
                    uk_name = l[2].replace('[','').replace(']','')
                    fh.check_obj_name(uk_name, f)
                    header = '''IF NOT EXISTS(SELECT * FROM sys.indexes i WHERE i.name =\'''' + uk_name + '''\')
BEGIN 
    '''
                    tail = '''
PRINT concat('[INFO] ', convert(varchar,getdate(),120), ' - Created Unique Key '''+uk_name+'''...')                
END;
GO
    '''
                    new_context = header + context + tail

                    new_file_name = os.path.join(tgt_dir, f)
                    fh.write_file(new_file_name, new_context, 'utf-8')

                    # print('{} {} {}'.format(f,table_name,uk_name))
                except:
                    print(f)






