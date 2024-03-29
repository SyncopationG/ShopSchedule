__doc__ = """
解码测试，考虑工人的柔性作业车间调度
"""

from src import *


def main(save="drcfjsp", instance="DMFJS01"):
    time_unit = 1
    a = drcfjsp_benchmark.instance[instance]
    n, m, w, p, tech, worker, proc = Utils.string2data_drcfjsp(a, int, time_unit)
    problem = Utils.create_schedule(Fjsp, n, m, p, tech, proc, w=w, worker=worker)
    code = Code.sequence_operation_based(n, p)
    """解码方式一：有机器编码、工人编码，在迭代的过程中要保持mac和wok匹配"""
    # mac = Code.assignment_job_based(n, p, tech)
    # wok = Code.assignment_worker(n, p, tech, worker, mac)
    # solution = problem.decode_worker(code, mac, wok, direction=0)
    """解码方式二：无机器编码、工人编码，可以在解码过程中保存机器编码和工人编码"""
    solution = problem.decode_worker_new(code, direction=0)
    solution.print()
    solution.save_code_to_txt(f"./{dir_DecodeTest}/Code/%s.txt" % save)
    solution.save_gantt_chart_to_csv(f"./{dir_DecodeTest}/GanttChart/%s.csv" % save)
    solution.gantt_chart_png(f"./{dir_DecodeTest}/GanttChartPngHtml/%s.png" % save, lang=0)


if __name__ == '__main__':
    main(save="example-drcfjsp")
