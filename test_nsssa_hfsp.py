__doc__ = """
基于非支配排序麻雀搜索算法求解多目标混合流水车间调度问题；
"""

from src import *


def run(instance="real1"):
    time_unit = 1
    a = hfsp_benchmark.instance[instance]
    b = hfsp_benchmark.due_date[instance]
    n, m, p, tech, proc = Utils.string2data_fjsp_hfsp(a, int, time_unit)
    due_date = list(map(int, b.split()))
    problem = Utils.create_schedule(Hfsp, n, m, p, tech, proc, due_date=due_date, time_unit=time_unit)
    objective_list = [Objective.makespan, Objective.tardiness, ]
    nssssa = NSSSAFHFSP(pop_size=40, st=0.8, pd=0.2, sd=0.2, sigma=1, max_generation=50, objective=objective_list,
                        schedule=problem, max_rate_front1=0.8)
    nssssa.schedule.ga_operator[Selection.name] = Selection.nsga_elite_strategy
    NsgaTemplate(save="NSSSA_HFSP", instance=instance, nsga=nssssa, n_exp=10, n_level=10, column=0)


def main():
    for instance in INSTANCE_LIST_HFSP.split():
        run(instance=instance)


if __name__ == '__main__':
    main()
