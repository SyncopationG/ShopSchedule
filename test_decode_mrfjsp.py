from src import *


def main(instance="example"):
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
    # solution = problem.decode(code, mac, route, direction=0)
    """解码方式二：无机器编码，可以在解码过程中保存机器编码"""
    solution = problem.decode_new(code, route, direction=0)
    solution.print()
    solution.save_code_to_txt("./Result/Code/%s.txt" % instance)
    solution.save_gantt_chart_to_csv("./Result/GanttChart/%s.csv" % instance)
    solution.gantt_chart_png("./Result/GanttChartPngHtml/%s.png" % instance, key_block=True, lang=0)


if __name__ == '__main__':
    main(instance="example")
