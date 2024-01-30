__doc__ = """
算法测试，考虑工人的柔性作业车间调度
"""

from src import *
from src.test_parameter_ga_nsga import *


def main(instance="DMFJS01"):
    time_unit = 1
    a = drcfjsp_benchmark.instance[instance]
    n, m, w, p, tech, worker, proc = Utils.string2data_drcfjsp(a, int, time_unit)
    best_known = drcfjsp_benchmark.best_known[instance]
    problem = Utils.create_schedule(Fjsp, n, m, p, tech, proc, w=w, worker=worker, best_known=best_known,
                                    time_unit=time_unit)
    ga = GaDrcFjspNew(pop_size=POP_SIZE, rc=RC, rm=RM, max_generation=MAX_GENERATION, objective=Objective.makespan,
                      schedule=problem, max_stay_generation=MAX_STAY_GENERATION)
    ga.schedule.ga_operator[Crossover.name] = Crossover.ipox
    ga.schedule.ga_operator[Mutation.name] = Mutation.tpe
    ga.schedule.ga_operator[Selection.name] = Selection.roulette
    # ga.schedule.para_key_block_move = False # 不可用，存在问题待解决
    ga.schedule.para_tabu = True
    ga.schedule.para_dislocation = True
    GaTemplate(save="GA_DRCFJSP", instance=instance, ga=ga, n_exp=N_EXP)


def exp():
    # for instance in INSTANCE_LIST_DRCFJSP.split():
    for instance in drcfjsp_benchmark.instance.keys():
        main(instance=instance)


if __name__ == '__main__':
    exp()
