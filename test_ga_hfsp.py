from src import *


def main(instance="example"):
    time_unit = 1
    a = hfsp_benchmark.instance[instance]
    n, m, p, tech, proc = Utils.string2data_fjsp_hfsp(a, int, time_unit)
    best_known = hfsp_benchmark.best_known[instance]
    problem = Utils.create_schedule(Hfsp, n, m, p, tech, proc, best_known=best_known, time_unit=time_unit)
    ga = GaFspHfsp(pop_size=20, rc=0.85, rm=0.15, max_generation=int(10e4), objective=Objective.makespan,
                   schedule=problem, max_stay_generation=50)
    ga.schedule.ga_operator[Crossover.name] = Crossover.pmx
    ga.schedule.ga_operator[Mutation.name] = Mutation.sub_reverse
    ga.schedule.ga_operator[Selection.name] = Selection.roulette
    ga.schedule.para_tabu = False
    ga.schedule.para_dislocation = False
    GaTemplate(save="GA_HFSP", instance=instance, ga=ga, n_exp=10)


def exp():
    for instance in INSTANCE_LIST_HFSP.split():
        main(instance=instance)


if __name__ == '__main__':
    exp()
