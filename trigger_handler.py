# coding=utf-8
# !
# -------------------------------------------------------------------------------
# Description :trigger handler for aspira triggers
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
    src_dir = "E:\Work-RAOutdoors\CA\AspiraFocusDB\AspiraFocusDatabaseCodes\Databases\CA\Schema Objects\Tables\Triggers"
    # target script location
    tgt_dir = "E:\Work-RAOutdoors\CA\AspiraFocusDB\\UniversalDatabasesCodes\Databases\Triggers"

    if os.path.exists(src_dir) and os.path.exists(tgt_dir):
        files = os.listdir(src_dir)
        for f in files:
            file_name = os.path.join(src_dir, f)
            # only read trigger files
            if os.path.isfile(file_name) and re.search(r'trigger', f) is not None:
                try:
                    encoding_name = fh.get_file_encoding(file_name)
                    context = fh.get_file_context(file_name,encoding_name)
                    ex = re.compile(r"\[.*?\]+")
                    l = ex.findall(context)
                    trigger_name = l[1].replace('[','').replace(']','')
                    fh.check_obj_name(trigger_name, f)
                    header = '''IF EXISTS(SELECT * FROM sys.triggers WHERE name =\'''' + trigger_name +'''\')
BEGIN
DROP TRIGGER ''' + trigger_name + '''
PRINT concat('[INFO] ', convert(varchar,getdate(),120), ' - Dropped Trigger '''+trigger_name+'''...')
END;
GO
    '''
                    tail = '''
PRINT concat('[INFO] ', convert(varchar,getdate(),120), ' - Created Trigger '''+trigger_name+'''...')
GO
    '''
                    new_context = header + context + tail

                    new_file_name = os.path.join(tgt_dir, f)
                    fh.write_file(new_file_name, new_context, 'utf-8')
                    # print('{} {}'.format(f,trigger_name))
                except:
                    print(f)
                    # pass







