__doc__ = """
基于遗传算法求解作业车间调度问题；

"""

from src import *


def run(instance="ft06"):
    a = jsp_benchmark.instance[instance]
    b = jsp_benchmark.due_date[instance]
    n, m, p, tech, proc = Utils.string2data_jsp_fsp(a)
    due_date = list(map(int, b.split()))
    best_known = jsp_benchmark.best_known[instance]
    ga = GaTemplateJsp(pop_size=50, rc=0.85, rm=0.15, max_generation=500, objective=Objective.makespan,
                       n=n, m=m, p=p, tech=tech, proc=proc, due_date=due_date,
                       index_template=0, best_known=best_known)
    ga.do_exp(exp_log="./GA_JSP", instance=instance, n_exp=10, tabu_search=True, key_block_move=False,
              gc=False, y_based=1)


def main():
    for instance in INSTANCE_LIST_JSP.split():
        run(instance=instance)


if __name__ == '__main__':
    main()
