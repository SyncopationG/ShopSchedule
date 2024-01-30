__doc__ = """
解码测试，多加工路径的柔性作业车间调度
"""

from src import *


def main(save="mrfjsp", instance="example"):
    time_unit = 1
    a = mrfjsp_benchmark.instance[instance]
    # a = Utils.load_text("./src/data/mrfjsp/%s.txt" % instance)
    n, m, p, tech, proc = Utils.string2data_mrfjsp(a, int, time_unit)
    problem = Utils.create_schedule(Fjsp, n, m, p, tech, proc, multi_route=True)
    r = [job.nor for job in problem.job.values()]
    code = Code.sequence_operation_based(n, p)
    # route = Code.assignment_route(n, r)
    # route = Code.assignment_route_min_avg_fjsp(n, r, problem.job)
    route = Code.assignment_route_min_total_fjsp(n, r, problem.job)
    """解码方式一：有机器编码，在迭代的过程中要保持mac和route匹配"""
    # mac = Code.assignment_job_based_route(n, p, tech, route)
    # solution = problem.test_decode(code, mac, route, direction=0)
    """解码方式二：无机器编码，可以在解码过程中保存机器编码"""
    solution = problem.decode_new(code, route, direction=0)
    solution.print()
    solution.save_code_to_txt(f"./{dir_DecodeTest}/Code/%s.txt" % save)
    solution.save_gantt_chart_to_csv(f"./{dir_DecodeTest}/GanttChart/%s.csv" % save)
    solution.gantt_chart_png(f"./{dir_DecodeTest}/GanttChartPngHtml/%s.png" % save, lang=0)


if __name__ == '__main__':
    main(save="example-mrfjsp")
