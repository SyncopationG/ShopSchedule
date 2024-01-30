__doc__ = """
算法测试，多目标作业车间调度
"""

from src import *
from src.test_parameter_ga_nsga import *


def run(instance="ft06"):
    time_unit = 1
    a = jsp_benchmark.instance[instance]
    b = jsp_benchmark.due_date[instance]
    n, m, p, tech, proc = Utils.string2data_jsp_fsp(a, int, time_unit)
    due_date = list(map(int, b.split()))
    problem = Utils.create_schedule(Jsp, n, m, p, tech, proc, due_date=due_date, time_unit=time_unit)
    objective_list = [Objective.makespan, Objective.tardiness, ]
    nsga = NsgaJsp(pop_size=POP_SIZE, rc=RC, rm=RM, max_generation=MAX_GENERATION, objective=objective_list,
                   schedule=problem,
                   max_rate_front1=MAX_RATE_FRONT1)
    nsga.schedule.ga_operator[Crossover.name] = Crossover.pox
    nsga.schedule.ga_operator[Mutation.name] = Mutation.tpe
    nsga.schedule.ga_operator[Selection.name] = Selection.nsga_elite_strategy
    nsga.schedule.para_key_block_move = True
    NsgaTemplate(save="NSGA_JSP", instance=instance, nsga=nsga, n_exp=N_EXP, n_level=N_LEVEL, column=0)


def main():
    for instance in INSTANCE_LIST_JSP.split():
        run(instance=instance)


if __name__ == '__main__':
    main()
