__doc__ = """
解码测试，等待时间有限的作业车间调度
"""

# import cProfile
# import os

from src import *


# pr = cProfile.Profile()


def main(save="lwjsp", instance="example"):
    time_unit = 1
    a = jsp_benchmark.instance[instance]
    n, m, p, tech, proc = Utils.string2data_jsp_fsp(a, int, time_unit)
    b = Utils.load_text("./src/data/limited_wait_jsp/%s.txt" % instance)
    c = [None, Utils.string2data_wait(b, p, int, time_unit)][0]
    problem = Utils.create_schedule(Jsp, n, m, p, tech, proc, limited_wait=c, time_unit=time_unit)
    # """基于工序的编码"""
    code = problem.spt()
    # pr.enable()
    solution = problem.decode_limited_wait(code)
    # pr.disable()
    # pr.dump_stats(f"./{dir_DecodeTest}/test_decode_jsp")
    # os.system("pyprof2calltree -i ./Result/test_decode_jsp -o ./Result/callgrind.test_decode_jsp")
    """解码结果"""
    solution.print()
    solution.save_code_to_txt(f"./{dir_DecodeTest}/Code/%s.txt" % save)
    solution.save_gantt_chart_to_csv(f"./{dir_DecodeTest}/GanttChart/%s.csv" % save)
    solution.gantt_chart_png(f"./{dir_DecodeTest}/GanttChartPngHtml/%s.png" % save, lang=0)


if __name__ == '__main__':
    main(save="example-lwjsp")
