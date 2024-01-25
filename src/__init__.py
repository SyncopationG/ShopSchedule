from .algorithm import GaFjsp, GaLwFjsp, GaDrcFjsp, GaMrFjsp
from .algorithm import GaFjspNew, GaLwFjspNew, GaDrcFjspNew, GaMrFjspNew
from .algorithm import GaFspHfsp, GaFspHfspWorkTimetable
from .algorithm import GaJsp, GaLwJsp, GaMrJsp
from .algorithm import GaJspNew, GaLwJspNew, GaLwJspNew2, GaMrJspNew
from .algorithm import NSSSAFHFSP
from .algorithm import NsgaJsp, NsgaHfsp
from .algorithm import OrToolsJspSat
from .data import drcfjsp_benchmark
from .data import fjsp_benchmark, fsp_benchmark, jsp_benchmark, hfsp_benchmark
from .data import fjsp_simulation, fsp_simulation, jsp_simulation
from .data import mrfjsp_benchmark
from .data import mrjsp_benchmark
from .define import Crossover, Mutation, Selection
from .info import GanttChart
from .objective import Objective
from .pareto import Pareto, SelectPareto
from .resource import Code, Job, Machine, Task, TimeTable
from .shop import Jsp, Fjsp, Fsp, Hfsp
from .template import GaTemplate, NsgaTemplate
from .utils import Utils

DIR_RESULT = ["./Result", "./Result/Code", "./Result/GanttChart", "./Result/GanttChartPngHtml"]
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
