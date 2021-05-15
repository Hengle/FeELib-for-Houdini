
import hou


hou.hscript('ophide Sop packintrinsics_fee')
hou.hscript('ophide Sop groupbybearing_fee')
hou.hscript('ophide Sop matchsize_fee')
hou.hscript('ophide Sop uniquenames_fee')
hou.hscript('ophide Sop groupbyname_fee')
hou.hscript('ophide Sop sortnamebyattrib_fee')
hou.hscript('ophide Sop keepname_betweenframe_fee')
hou.hscript('ophide Sop numpieces_fee')
hou.hscript('ophide Sop polyframe_cubic_fee')
hou.hscript('ophide Sop polyframe_cubic_fee::1.0')
hou.hscript('ophide Sop meshlayout_fee')
hou.hscript('ophide Sop meshlayout_multilayer_fee')
hou.hscript('ophide Sop copytopoints_fee')

hou.hscript('ophide Sop uniformnormaldir_fee::1.0')
hou.hscript('ophide Sop uniformnormaldir_fee::2.0')

hou.hscript('ophide Sop spreadout_fee')
hou.hscript('ophide Sop spreadout_fee::0.9')
hou.hscript('ophide Sop spreadout_fee::1.0')
hou.hscript('ophide Sop spreadout_multiinput_fee')








import hou
import os

__FeE_FeELib_PATH = hou.getenv('FeELib')#### 复制脚本需要修改这个
# print(__FeE_FeELib_PATH)
__FeE_FeELib_PATH = os.path.normpath(__FeE_FeELib_PATH)
__FeE_FeELib_PATH = __FeE_FeELib_PATH.replace('\\', '/')
# print(__FeE_FeELib_PATH)

__FeE_HOUDINI_SCRIPT_PATH = hou.getenv('HOUDINI_SCRIPT_PATH')
__FeE_HOUDINI_SCRIPT_PATH_split = __FeE_HOUDINI_SCRIPT_PATH.split(';')

try:
    __FeE_startScriptNum = 1 + __FeE_HOUDINI_SCRIPT_PATH_split.index(__FeE_FeELib_PATH + '/scripts')
except:
    __FeE_startScriptNum = 9999999

for idx in range(__FeE_startScriptNum, len(__FeE_HOUDINI_SCRIPT_PATH_split)):
    __FeE_nextStartupPy = __FeE_HOUDINI_SCRIPT_PATH_split[idx] + '/456.py'
    if os.path.exists(__FeE_nextStartupPy):
        with open(__FeE_nextStartupPy, "r") as __FeE_open:
            __FeE_code = __FeE_open.read()
            exec(__FeE_code)
        break
