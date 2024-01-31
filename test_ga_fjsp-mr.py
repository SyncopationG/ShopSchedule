__doc__ = """
算法测试，多加工路径的柔性作业车间调度
"""

import os

from src import *
from src.test_parameter_ga_nsga import *


def main(instance="example"):
    time_unit = 1
    # a = mrfjsp_benchmark.instance[instance]
    # n, m, p, tech, proc = Utils.string2data_mrfjsp(a, int, time_unit)
    # best_known = mrfjsp_benchmark.best_known[instance]
    a = Utils.load_text("./src/data/mrfjsp/%s.txt" % instance)
    n, m, p, tech, proc = Utils.string2data_mrfjsp(a, int, time_unit)
    best_known = None
    problem = Utils.create_schedule(Fjsp, n, m, p, tech, proc, best_known=best_known, time_unit=time_unit,
                                    multi_route=True)
    ga = GaMrFjsp(pop_size=POP_SIZE, rc=RC, rm=RM, max_generation=MAX_GENERATION, objective=Objective.makespan,
                  schedule=problem, max_stay_generation=MAX_STAY_GENERATION)
    ga.strategy = 1  # 0：最早加工开始时间解码，1：最早加工完工时间解码
    ga.schedule.ga_operator[Crossover.name] = Crossover.ipox
    ga.schedule.ga_operator[Mutation.name] = Mutation.tpe
    ga.schedule.ga_operator[Selection.name] = Selection.roulette
    # ga.schedule.para_key_block_move =  False # 不可用，存在问题待解决
    ga.schedule.para_tabu = True
    ga.schedule.para_dislocation = True
    GaTemplate(save="GA_MRFJSP", instance=instance, ga=ga, n_exp=N_EXP)


def exp():
    # for instance in INSTANCE_LIST_MRFJSP.split():
    instance_list = [i[:-4] for i in os.listdir("./src/data/mrfjsp")]
    for instance in instance_list:
        main(instance=instance)


if __name__ == '__main__':
    exp()
