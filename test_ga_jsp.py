import cProfile
import os

from src import *

pr = cProfile.Profile()


def main(instance="example"):
    time_unit = 1
    a = jsp_benchmark.instance[instance]
    n, m, p, tech, proc = Utils.string2data_jsp_fsp(a, int, time_unit)
    best_known = jsp_benchmark.best_known[instance]
    problem = Utils.create_schedule(Jsp, n, m, p, tech, proc, best_known=best_known, time_unit=time_unit)
    ga = GaJsp(pop_size=20, rc=0.85, rm=0.15, max_generation=int(10e4), objective=Objective.makespan,
               schedule=problem, max_stay_generation=50)
    ga.schedule.ga_operator[Crossover.name] = Crossover.pox
    ga.schedule.ga_operator[Mutation.name] = Mutation.tpe
    ga.schedule.ga_operator[Selection.name] = Selection.roulette
    ga.schedule.para_key_block_move = False
    ga.schedule.para_tabu = True
    ga.schedule.para_dislocation = False
    pr.enable()
    GaTemplate(save="GA_JSP", instance=instance, ga=ga, n_exp=10)
    pr.disable()
    pr.dump_stats("./Result/test_ga_jsp.prof")
    os.system("pyprof2calltree -i ./Result/test_ga_jsp.prof -o ./Result/callgrind.test_ga_jsp.prof")


def exp():
    for instance in INSTANCE_LIST_JSP.split():
        main(instance=instance)


if __name__ == '__main__':
    exp()
