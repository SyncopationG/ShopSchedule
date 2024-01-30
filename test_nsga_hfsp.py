__doc__ = """
算法测试，多目标混合流水车间调度
"""

from src import *
from src.test_parameter_ga_nsga import *


def run(instance="real1"):
    time_unit = 1
    a = hfsp_benchmark.instance[instance]
    b = hfsp_benchmark.due_date[instance]
    n, m, p, tech, proc = Utils.string2data_fjsp_hfsp(a, int, time_unit)
    due_date = list(map(int, b.split()))
    problem = Utils.create_schedule(Hfsp, n, m, p, tech, proc, due_date=due_date, time_unit=time_unit)
    objective_list = [Objective.makespan, Objective.tardiness, ]
    nsga = NsgaHfsp(pop_size=POP_SIZE, rc=RC, rm=RM, max_generation=MAX_GENERATION, objective=objective_list,
                    schedule=problem,
                    max_rate_front1=MAX_RATE_FRONT1)
    nsga.schedule.ga_operator[Crossover.name] = Crossover.pmx
    nsga.schedule.ga_operator[Mutation.name] = Mutation.tpe
    nsga.schedule.ga_operator[Selection.name] = Selection.nsga_elite_strategy
    NsgaTemplate(save="NSGA_HFSP", instance=instance, nsga=nsga, n_exp=N_EXP, n_level=N_LEVEL, column=0)


def main():
    # for instance in INSTANCE_LIST_HFSP.split():
    for instance in hfsp_benchmark.instance.keys():
        run(instance=instance)


if __name__ == '__main__':
    main()
