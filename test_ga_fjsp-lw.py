__doc__ = """
算法测试，等待时间有限的柔性作业车间调度
"""

from src import *
from src.test_parameter_ga_nsga import *


def main(instance="example"):
    time_unit = 1
    a = fjsp_benchmark.instance[instance]
    n, m, p, tech, proc = Utils.string2data_fjsp_hfsp(a, int, time_unit)
    lw = Utils.string2data_wait(Utils.load_text("./src/data/limited_wait_fjsp/%s.txt" % instance), p, int, time_unit)
    best_known = fjsp_benchmark.best_known[instance]
    problem = Utils.create_schedule(Fjsp, n, m, p, tech, proc, limited_wait=lw, best_known=best_known,
                                    time_unit=time_unit)
    ga = GaLwFjsp(pop_size=POP_SIZE, rc=RC, rm=RM, max_generation=MAX_GENERATION, objective=Objective.makespan,
                  schedule=problem, max_stay_generation=MAX_STAY_GENERATION)
    ga.schedule.ga_operator[Crossover.name] = Crossover.ox
    ga.schedule.ga_operator[Mutation.name] = Mutation.tpe
    ga.schedule.ga_operator[Selection.name] = Selection.roulette
    ga.schedule.para_key_block_move = False
    ga.schedule.para_tabu = False
    ga.schedule.para_dislocation = False
    GaTemplate(save="GA_LWFJSP", instance=instance, ga=ga, n_exp=N_EXP)


def exp():
    for instance in INSTANCE_LIST_LWFJSP.split():
        main(instance=instance)


if __name__ == '__main__':
    exp()
