import cProfile
import os

from src import *

pr = cProfile.Profile()


def main(instance="example"):
    time_unit = 1
    a = jsp_benchmark.instance[instance]
    n, m, p, tech, proc = Utils.string2data_jsp_fsp(a, int, time_unit)
    b = Utils.load_text("./src/data/limited_wait_jsp/%s.txt" % instance)
    c = [None, Utils.string2data_wait(b, p, int, time_unit)][0]
    problem = Utils.create_schedule(Jsp, n, m, p, tech, proc, limited_wait=c, time_unit=time_unit)
    """调度规则"""
    # node_list_complete = problem.spt_lpt_new(spt_or_lpt=0)
    # for node in node_list_complete:
    #     print(node.value + 1, problem.decode(node.value, direction=1).schedule.makespan)
    # code = node_list_complete[0].value
    # solution = problem.decode(code, direction=1)
    # """基于工序的编码"""
    code = problem.spt()
    pr.enable()
    solution = problem.decode(code)
    pr.disable()
    pr.dump_stats("./Result/test_decode_jsp")
    os.system("pyprof2calltree -i ./Result/test_decode_jsp -o ./Result/callgrind.test_decode_jsp")
    # solution = problem.decode_new(code)
    # solution = problem.decode_new_twice(code)
    # solution = problem.decode_limited_wait(code)
    # solution = problem.decode_limited_wait_new(code)
    # solution = problem.decode_limited_wait_new_twice(code)
    # code = solution.trans_operation_based2machine_based()
    # print(code, "# solution.trans_operation_based2machine_based()")
    """基于机器的编码"""
    # code = Code.sequence_machine_based(n, m, problem.job)
    # solution = problem.decode_machine_based(code)
    # solution = problem.decode_machine_based_limited_wait(code)
    """解码结果"""
    print(solution.schedule.machine[0].idle)
    print(Objective.total_workload(solution))
    print(Objective.max_workload(solution))
    solution.print()
    solution.save_code_to_txt("./Result/Code/%s.txt" % instance)
    solution.save_gantt_chart_to_csv("./Result/GanttChart/%s.csv" % instance)
    solution.gantt_chart_png("./Result/GanttChartPngHtml/%s.png" % instance, key_block=True, lang=0)


if __name__ == '__main__':
    main(instance="example2")
