from .utils import Utils

dir_DecodeTest = "DecodeTest"
DIR_RESULT = [
    f"./{dir_DecodeTest}",
    f"./{dir_DecodeTest}/Code",
    f"./{dir_DecodeTest}/GanttChart",
    f"./{dir_DecodeTest}/GanttChartPngHtml"
]
[Utils.make_dir(i) for i in DIR_RESULT]
INSTANCE_LIST_JSP = """
ft06
"""
INSTANCE_LIST_FJSP = """
mk1
"""
INSTANCE_LIST_FSP = """
car2
car3
car4
car5
car6
car7
car8
"""
INSTANCE_LIST_HFSP = """
real1
"""
CASES_LIST = """
case1
"""
INSTANCE_LIST_LWJSP = """
ft06
"""
INSTANCE_LIST_LWFJSP = """
mk1
"""
INSTANCE_LIST_MRJSP = """
n10m10-1
"""
INSTANCE_LIST_MRFJSP = """
n10m10-1
"""
INSTANCE_LIST_DRCFJSP = """
DMFJS01
"""
