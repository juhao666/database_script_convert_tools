# coding=utf-8
# !
# -------------------------------------------------------------------------------
# Description :stored procedure handler for aspira stored procedure
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
    src_dir = "E:\Work-RAOutdoors\CA\AspiraFocusDB\AspiraFocusDatabaseCodes\Databases\CA\Schema Objects\Programmability\Stored Procedures"
    # target script location
    tgt_dir = "E:\Work-RAOutdoors\CA\AspiraFocusDB\\UniversalDatabasesCodes\Databases\StoredProcedures"

    if os.path.exists(src_dir) and os.path.exists(tgt_dir):
        files = os.listdir(src_dir)
        for f in files:
            if f == "dbo.UserStory59.proc.sql": # except this script
                continue
            file_name = os.path.join(src_dir, f)
            # only read trigger files
            if os.path.isfile(file_name):
                try:
                    encoding_name = fh.get_file_encoding(file_name)
                    context = fh.get_file_context(file_name,encoding_name)
                    ex = re.compile(r"\[.*?\]+")
                    l = ex.findall(context)
                    sp_name = l[1].replace('[', '').replace(']', '')
                    """debug code below 3 rows"""
                    # fh.check_obj_name(sp_name, f)
                    header = '''IF EXISTS(SELECT TOP 1 1 FROM sys.procedures i with(nolock) 
              WHERE i.name = \'''' + sp_name + '''\')
BEGIN
DROP PROCEDURE ''' + sp_name + '''
PRINT concat('[INFO] ', convert(varchar,getdate(),120), ' - Dropped Stored Procedure '''+sp_name+'''...')
END;
GO
    '''
                    tail = '''
GO
PRINT concat('[INFO] ', convert(varchar,getdate(),120), ' - Created Stored Procedure '''+sp_name+'''...')               
GO
    '''
                    new_context = header + context + tail

                    new_file_name = os.path.join(tgt_dir, f)
                    fh.write_file(new_file_name, new_context, 'utf-8')
                    # print('{} {}'.format(f,trigger_name))
                except:
                    print(f)
                    pass







