__doc__ = """
算法测试，多目标混合流水车间调度
"""

from src import *
from src.test_parameter_ssa_nsssa import *


def run(instance="real1"):
    time_unit = 1
    a = hfsp_benchmark.instance[instance]
    b = hfsp_benchmark.due_date[instance]
    n, m, p, tech, proc = Utils.string2data_fjsp_hfsp(a, int, time_unit)
    due_date = list(map(int, b.split()))
    problem = Utils.create_schedule(Hfsp, n, m, p, tech, proc, due_date=due_date, time_unit=time_unit)
    objective_list = [Objective.makespan, Objective.tardiness, ]
    nssssa = NSSSAFHFSP(pop_size=POP_SIZE, st=ST, pd=PD, sd=SD, sigma=SIGMA, max_generation=MAX_GENERATION,
                        objective=objective_list,
                        schedule=problem, max_rate_front1=MAX_RATE_FRONT1)
    nssssa.schedule.ga_operator[Selection.name] = Selection.nsga_elite_strategy
    NsgaTemplate(save="NSSSA_HFSP", instance=instance, nsga=nssssa, n_exp=N_EXP, n_level=N_LEVEL, column=0)


def main():
    for instance in INSTANCE_LIST_HFSP.split():
        run(instance=instance)


if __name__ == '__main__':
    main()
