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


# source script location
src_dir = "E:\Work-RAOutdoors\CA\AspiraFocusDB\AspiraFocusDatabaseCodes\Databases\CA\Schema Objects\Tables\Keys"

if os.path.exists(src_dir) and os.path.exists(tgt_dir):
    files = os.listdir(src_dir)
    for f in files:
        file_name = os.path.join(src_dir, f)
        # only read ukey files
        if re.search(r'pkey', f) is None and re.search(r'fkey', f) is None and re.search(r'ukey', f) is None:
            print(f)





