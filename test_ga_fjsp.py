from src import *


def main(instance="example"):
    time_unit = 1
    a = fjsp_benchmark.instance[instance]
    n, m, p, tech, proc = Utils.string2data_fjsp_hfsp(a, int, time_unit)
    best_known = fjsp_benchmark.best_known[instance]
    problem = Utils.create_schedule(Fjsp, n, m, p, tech, proc, best_known=best_known, time_unit=time_unit)
    ga = GaFjsp(pop_size=60, rc=0.65, rm=0.35, max_generation=int(10e4), objective=Objective.makespan,
                   schedule=problem, max_stay_generation=50)
    ga.schedule.ga_operator[Crossover.name] = Crossover.dpox
    ga.schedule.ga_operator[Mutation.name] = Mutation.tpe
    ga.schedule.ga_operator[Selection.name] = Selection.roulette
    ga.schedule.para_key_block_move = False
    ga.schedule.para_tabu = False
    ga.schedule.para_dislocation = False
    GaTemplate(save="GA_Fjsp_dpox", instance=instance, ga=ga, n_exp=10)


def exp():
    for instance in INSTANCE_LIST_FJSP.split():
        main(instance=instance)


if __name__ == '__main__':
    exp()
