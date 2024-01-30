__doc__ = """
算法测试，多加工路径的作业车间调度
"""

import os

from src import *
from src.test_parameter_ga_nsga import *


def main(instance="example"):
    time_unit = 1
    # a = mrjsp_benchmark.instance[instance]
    # n, m, p, tech, proc = Utils.string2data_mrjsp(a, int, time_unit)
    # best_known = mrjsp_benchmark.best_known[instance]
    a = Utils.load_text("./src/data/mrjsp/%s.txt" % instance)
    n, m, p, tech, proc = Utils.string2data_mrjsp(a, int, time_unit)
    best_known = None
    problem = Utils.create_schedule(Jsp, n, m, p, tech, proc, best_known=best_known, time_unit=time_unit,
                                    multi_route=True)
    ga = GaMrJsp(pop_size=POP_SIZE, rc=RC, rm=RM, max_generation=MAX_GENERATION, objective=Objective.makespan,
                 schedule=problem, max_stay_generation=MAX_STAY_GENERATION)
    ga.schedule.ga_operator[Crossover.name] = Crossover.pox
    ga.schedule.ga_operator[Mutation.name] = Mutation.tpe
    ga.schedule.ga_operator[Selection.name] = Selection.roulette
    ga.schedule.para_key_block_move = True
    ga.schedule.para_tabu = True
    ga.schedule.para_dislocation = True
    GaTemplate(save="GA_MRJSP", instance=instance, ga=ga, n_exp=N_EXP)


def exp():
    # for instance in INSTANCE_LIST_MRJSP.split():
    instance_list = [i[:-4] for i in os.listdir("./src/data/mrjsp")]
    for instance in instance_list:
        main(instance=instance)


if __name__ == '__main__':
    exp()
