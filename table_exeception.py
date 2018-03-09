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

import os, re
import file_handler as fh


def run():
    # source script location
    src_dir = "E:\Work-RAOutdoors\CA\AspiraFocusDB\AspiraFocusDatabaseCodes\Databases\CA\Schema Objects\Tables"
    # target script location
    tgt_dir = "E:\Work-RAOutdoors\CA\AspiraFocusDB\\UniversalDatabasesCodes\Databases\Tables"

    if os.path.exists(src_dir) and os.path.exists(tgt_dir):
        files = os.listdir(src_dir)
        for f in files:
            file_name = os.path.join(src_dir, f)
            if os.path.isfile(file_name):
                fh.file_str_replace(file_name, 'GO', '')
                fh.file_str_replace(file_name, 'go', '')
                pattern = re.compile(r"(?<=dbo.).+?(?=.table.sql)") # 取两个字符串中间的字符
                table_name = pattern.findall(f)[0]
                header = '''IF NOT EXISTS(SELECT TOP 1 1 FROM sys.tables t WITH(NOLOCK)
WHERE SCHEMA_NAME(schema_id) = 'DBO' AND OBJECT_NAME(object_id) =\''''+table_name + '''\' AND type = 'U')
BEGIN
    '''

                encoding_name = fh.get_file_encoding(file_name)
                context = fh.get_file_context(file_name,encoding_name)
                pattern = re.compile(r'(FK)')
                if pattern.search(context):
                    print(f)




