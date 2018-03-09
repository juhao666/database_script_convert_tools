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
    src_dir = "E:\Work-RAOutdoors\CA\AspiraFocusDB\AspiraFocusDatabaseCodes\Databases\CA\Schema Objects\Tables\Indexes"
    # target script location
    tgt_dir = "E:\Work-RAOutdoors\CA\AspiraFocusDB\\UniversalDatabasesCodes\Databases\Indexes"

    if os.path.exists(src_dir) and os.path.exists(tgt_dir):
        files = os.listdir(src_dir)
        for f in files:
            file_name = os.path.join(src_dir, f)
            # only read ukey files
            if re.search(r'index', f) is not None:
                try:
                    fh.file_str_replace(file_name, 'GO', '')
                    fh.file_str_replace(file_name, 'go', '')
                    encoding_name = fh.get_file_encoding(file_name)
                    context = fh.get_file_context(file_name, encoding_name)
                    ex = re.compile(r"\[.*?\]+")
                    l = ex.findall(context)
                    idx_name = l[0].replace('[', '').replace(']', '')
                    if idx_name == 'dbo':
                        print(f)
                    fh.check_obj_name(idx_name, f)
                    header = '''IF NOT EXISTS(SELECT TOP 1 1 FROM sys.indexes i with(nolock) 
                  WHERE i.name = \'''' + idx_name + '''\')
BEGIN
'''
                    tail = '''
PRINT concat('[INFO] ', convert(varchar,getdate(),120), ' - Created Index '''+ idx_name+'''...')                               
END
GO
'''
                    new_context = header + context + tail

                    new_file_name = os.path.join(tgt_dir, f)
                    fh.write_file(new_file_name, new_context, 'utf-8')

                    # print('{} {} {}'.format(f,table_name,pk_name))
                except:
                    print(f)





