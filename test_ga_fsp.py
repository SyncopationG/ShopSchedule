__doc__ = """
算法测试，流水车间调度
"""

from src import *
from src.test_parameter_ga_nsga import *


def main(instance="example"):
    time_unit = 1
    a = fsp_benchmark.instance[instance]
    n, m, p, tech, proc = Utils.string2data_jsp_fsp(a, int, time_unit)
    best_known = fsp_benchmark.best_known[instance]
    problem = Utils.create_schedule(Fsp, n, m, p, tech, proc, best_known=best_known, time_unit=time_unit)
    ga = GaFspHfsp(pop_size=POP_SIZE, rc=RC, rm=RM, max_generation=MAX_GENERATION, objective=Objective.makespan,
                   schedule=problem, max_stay_generation=MAX_STAY_GENERATION)
    ga.schedule.ga_operator[Crossover.name] = Crossover.pmx
    ga.schedule.ga_operator[Mutation.name] = Mutation.tpe
    ga.schedule.ga_operator[Selection.name] = Selection.roulette
    ga.schedule.para_tabu = True
    ga.schedule.para_dislocation = True
    GaTemplate(save="GA_FSP", instance=instance, ga=ga, n_exp=N_EXP)


def exp():
    # for instance in INSTANCE_LIST_FSP.split():
    for instance in fsp_benchmark.instance.keys():
        main(instance=instance)


if __name__ == '__main__':
    exp()
