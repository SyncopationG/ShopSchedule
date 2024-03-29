__doc__ = """
解码测试，多加工路径的作业车间调度
"""

from src import *


def main(save="mrjsp", instance="example2"):
    time_unit = 1
    a = mrjsp_benchmark.instance[instance]
    # a = Utils.load_text("./src/data/mrjsp/%s.txt" % instance)
    n, m, p, tech, proc = Utils.string2data_mrjsp(a, int, time_unit)
    problem = Utils.create_schedule(Jsp, n, m, p, tech, proc, multi_route=True)
    r = [job.nor for job in problem.job.values()]
    code = Code.sequence_operation_based(n, p)
    # route = Code.assignment_route(n, r)
    # route = Code.assignment_route_min_avg_jsp(n, r, problem.job)
    route = Code.assignment_route_min_total_jsp(n, r, problem.job)
    solution = problem.decode(code, route, direction=0)
    solution.print()
    solution.save_code_to_txt(f"./{dir_DecodeTest}/Code/%s.txt" % save)
    solution.save_gantt_chart_to_csv(f"./{dir_DecodeTest}/GanttChart/%s.csv" % save)
    solution.gantt_chart_png(f"./{dir_DecodeTest}/GanttChartPngHtml/%s.png" % save, lang=0)


if __name__ == '__main__':
    main(save="example-mrjsp")
