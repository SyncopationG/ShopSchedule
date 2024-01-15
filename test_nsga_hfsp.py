__doc__ = """
基于非支配排序遗传算法求解多目标作业车间调度问题；

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
    nsga = NsgaHfsp(pop_size=40, rc=0.85, rm=0.15, max_generation=50, objective=objective_list, schedule=problem,
                   max_rate_front1=0.8)
    nsga.schedule.ga_operator[Crossover.name] = Crossover.pmx
    nsga.schedule.ga_operator[Mutation.name] = Mutation.tpe
    nsga.schedule.ga_operator[Selection.name] = Selection.nsga_elite_strategy
    NsgaTemplate(save="NSGA_HFSP", instance=instance, nsga=nsga, n_exp=10, n_level=10, column=0)


def main():
    for instance in INSTANCE_LIST_HFSP.split():
        run(instance=instance)


if __name__ == '__main__':
    main()
