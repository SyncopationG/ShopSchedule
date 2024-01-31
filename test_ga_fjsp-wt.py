__doc__ = """
算法测试，考虑作息时间的柔性作业车间调度
"""

from src import *
from src.test_parameter_ga_nsga import *


def main(instance="example"):
    time_unit = 60
    a = fjsp_simulation.case[instance]
    n, m, p, tech, proc = Utils.string2data_fjsp_hfsp(a, int, time_unit)
    rest_start_end = TimeTable.consistent5d8h(m, 2020, 7, 6, 30, connect_internet=False, save=False, show=False)
    problem = Utils.create_schedule(Fjsp, n, m, p, tech, proc, best_known=None, time_unit=time_unit)
    problem2 = Utils.create_schedule(Fjsp, n, m, p, tech, proc, rest_start_end=rest_start_end,
                                     resumable=Utils.crt_resumable(n, p, 0), best_known=None, time_unit=time_unit)
    ga = GaFjspNew(pop_size=POP_SIZE, rc=RC, rm=RM, max_generation=MAX_GENERATION, objective=Objective.makespan,
                   schedule=problem, max_stay_generation=MAX_STAY_GENERATION)
    ga2 = GaFjspNew(pop_size=ga.pop_size, rc=ga.rc, rm=ga.rm, max_generation=MAX_GENERATION2,
                    objective=Objective.makespan, schedule=problem2, max_stay_generation=MAX_STAY_GENERATION2)
    ga.strategy = 1  # 0：最早加工开始时间解码，1：最早加工完工时间解码
    ga.schedule.ga_operator[Crossover.name] = Crossover.pox
    ga.schedule.ga_operator[Mutation.name] = Mutation.tpe
    ga.schedule.ga_operator[Selection.name] = Selection.roulette
    ga.schedule.para_tabu = True
    ga.schedule.para_dislocation = True
    ga2.strategy = 1  # 0：最早加工开始时间解码，1：最早加工完工时间解码
    ga2.schedule.ga_operator[Crossover.name] = Crossover.pox
    ga2.schedule.ga_operator[Mutation.name] = Mutation.tpe
    ga2.schedule.ga_operator[Selection.name] = Selection.roulette
    ga2.schedule.para_tabu = True
    ga2.schedule.para_dislocation = True
    GaTemplate(save="GA_FJSPWT", instance=instance, ga=ga, ga2=ga2, n_exp=N_EXP)


def exp():
    # for instance in CASES_LIST.split():
    for instance in fjsp_simulation.case.keys():
        main(instance=instance)


if __name__ == '__main__':
    exp()
