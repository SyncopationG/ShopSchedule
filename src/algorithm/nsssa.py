_doc__ = """
NSSSA：非支配排序麻雀搜索算法


"""

import time

import numpy as np

from ..define import Selection
from ..pareto import Pareto, SelectPareto
from ..resource import Code
from ..utils import Utils


class NSSSA:
    def __init__(self, pop_size, st, pd, sd, sigma, max_generation, objective, schedule, max_rate_front1):
        self.pop_size = pop_size
        self.st = st
        self.pd = pd
        self.sd = sd
        self.sigma = sigma
        self.max_generation = max_generation
        self.objective = objective
        self.schedule = schedule
        self.max_rate_front1 = max_rate_front1
        self.num_pd = int(self.pd * self.pop_size)
        self.num_pd2 = self.pop_size - self.num_pd
        self.num_sd = int(self.sd * self.pop_size)
        self.permutation = np.arange(self.pop_size)
        self.p = [job.nop for job in self.schedule.job.values()]
        self.tech = [[task.machine for task in job.task.values()] for job in self.schedule.job.values()]
        self.num_obj = len(self.objective)
        self.pop = [[], [], []]  # (info, objective)
        self.pop_child = [[], []]  # (info, objective)
        # (start, end, pareto front rate)
        self.record = [[], [], []]
        self.obj_rank1 = set()
        self.pareto = []

    def clear(self):
        self.pop = [[], []]
        self.pop_child = [[], []]
        self.record = [[], [], []]
        self.obj_rank1 = set()

    def get_obj(self, info):
        obj = []
        for func in self.objective:
            obj.append(func(info))
        return obj

    def update_child(self, info):
        self.pop_child[0].append(info)
        self.pop_child[1].append(self.get_obj(info))

    def update_child2(self, i, info):
        old = self.pop[1][i]
        new = self.get_obj(info)
        if Utils.is_dominate(new, old, self.num_obj):
            self.pop[0][i] = info
            self.pop[1][i] = new

    def show_generation(self, g):
        Utils.print("Generation {:<4} Runtime {:<8.4f} Pareto rate: {:<.2f} Objective：{}".format(
            g, self.record[1][g] - self.record[0][g], self.record[2][g], self.obj_rank1))

    @staticmethod
    def selection_elite_strategy(select_pareto):
        return select_pareto.elite_strategy()

    @staticmethod
    def selection_champion(select_pareto):
        return select_pareto.champion()

    @property
    def func_selection(self):
        func_dict = {
            Selection.default: self.selection_elite_strategy,
            Selection.nsga_elite_strategy: self.selection_elite_strategy,
            Selection.nsga_champion: self.selection_champion,
        }
        return func_dict[self.schedule.ga_operator[Selection.name]]

    def update_pareto(self):
        pareto = Pareto(self.pop_size, self.pop[1], self.num_obj)
        pareto.fast_non_dominate_sort()
        pareto.crowd_distance()
        self.pareto = pareto

    def do_selection(self):
        if len(self.pop_child[0]) != 0:
            info_new = []
            obj = np.vstack(self.pop_child[1])
            obj_new = np.vstack([self.pop[1], obj])
            for info in self.pop[0]:
                info_new.append(info)
            for info in self.pop_child[0]:
                info_new.append(info)
            scale = obj_new.shape[0]
            obj_new = obj_new.tolist()
        else:
            info_new = self.pop[0]
            obj_new = self.pop[1]
            scale = self.pop_size
        info_copy = info_new
        obj_copy = obj_new
        pareto = Pareto(scale, obj_copy, self.num_obj)
        pareto.fast_non_dominate_sort()  # 非支配排序
        pareto.crowd_distance()  # 计算拥挤度
        f = pareto.f
        rank = pareto.rank
        cd = pareto.cd
        select_pareto = SelectPareto(self.pop_size, scale, f, rank, cd, self.max_rate_front1)
        index = self.func_selection(select_pareto)
        pareto_front = []
        self.pop = [[], [], []]
        self.obj_rank1 = set()
        for i in range(self.pop_size):
            b = index[i]
            self.pop[0].append(info_copy[b])
            self.pop[1].append(obj_copy[b])
            if b in f[0]:
                pareto_front.append(i)
                self.obj_rank1.add(str(obj_copy[b]))
        self.record[2].append(len(pareto_front) / self.pop_size)
        self.pop_child = [[], [], []]
        self.update_pareto()

    def do_init(self, pop=None):
        pass

    def do_update_pd1(self, ):
        pass

    def do_update_pd2(self, ):
        pass

    def do_update_sd(self, ):
        pass

    def do_evolution(self, pop=None, n_level=5, column=0, exp_no=None):
        exp_no = "" if exp_no is None else exp_no
        Utils.print("{}Evolution {}  start{}".format("=" * 48, exp_no, "=" * 48), fore=Utils.fore().LIGHTYELLOW_EX)
        self.clear()
        self.do_init(pop)
        self.do_selection()
        self.show_generation(0)
        for g in range(1, self.max_generation + 1):
            self.record[0].append(time.perf_counter())
            self.do_update_pd1()
            self.do_update_pd2()
            self.do_update_sd()
            self.do_selection()
            self.record[1].append(time.perf_counter())
            self.show_generation(g)
        Utils.print("{}Evolution {} finish{}".format("=" * 48, exp_no, "=" * 48), fore=Utils.fore().LIGHTRED_EX)
        # 对结果进行处理
        pareto = Pareto(self.pop_size, self.pop[1], self.num_obj)
        pareto.fast_non_dominate_sort()
        all_res = []
        for level in range(len(pareto.f[:n_level])):
            if len(pareto.f[level]) == 1 and level > 0:
                break
            res, obj = [], []
            index = pareto.sort_obj_by(pareto.f[level], column)
            for i in [pareto.f[level][v] for v in index]:
                if self.pop[1][i] not in obj:
                    res.append((self.pop[0][i], self.pop[1][i]))
                obj.append(self.pop[1][i])
            all_res.append(res)
        return all_res


class NSSSAFHFSP(NSSSA):
    def __init__(self, pop_size, st, pd, sd, sigma, max_generation, objective, schedule, max_rate_front1):
        NSSSA.__init__(self, pop_size, st, pd, sd, sigma, max_generation, objective, schedule, max_rate_front1)

    def decode_update(self, code):
        info = self.schedule.decode_rk(self.permutation, code, stratege=0)
        self.update_child(info)

    def decode_update2(self, i, code):
        info = self.schedule.decode_rk(self.permutation, code)
        self.update_child2(i, info)
        # if np.random.random() < 0.5:
        #     self.update_child2(i, info)
        # else:
        #     self.update_child(info)

    def do_init(self, pop=None):
        self.record[0].append(time.perf_counter())
        for i in range(self.pop_size):
            if pop is None:
                code = Code.sequence_random_key(self.schedule.n)
            else:
                code = pop[0][i].code
            info = self.schedule.decode_rk(self.permutation, code)
            self.pop[0].append(info)
            self.pop[1].append(self.get_obj(info))
        self.record[1].append(time.perf_counter())

    def do_update_pd1(self, ):
        no = 0
        for f in self.pareto.f:
            for i in f:
                no += 1
                code = self.pop[0][i].ssa_pd1(no, self.st, self.max_generation)
                self.decode_update2(i, code)
                if no >= self.num_pd:
                    break

    def do_update_pd2(self, ):
        no = 0
        for f in self.pareto.f:
            for i in f:
                no += 1
                if no < self.num_pd:
                    continue
                else:
                    worst_no = np.random.choice(self.pareto.f[-1], 1, replace=False)[0]
                    p_no = np.random.choice(self.pareto.f[0], 1, replace=False)[0]
                    worst = self.pop[0][worst_no].code
                    p = self.pop[0][p_no].code
                    code = self.pop[0][i].ssa_pd2(no, self.num_pd2, worst, p)
                    self.decode_update2(i, code)

    def do_update_sd(self, ):
        no = 0
        # for f in self.pareto.f:
        for f in [np.random.permutation(self.pop_size)]:
            for i in f:
                no += 1
                worst_no = np.random.choice(self.pareto.f[-1], 1, replace=False)[0]
                best_no = np.random.choice(self.pareto.f[0], 1, replace=False)[0]
                worst = self.pop[0][worst_no].code
                best = self.pop[0][best_no].code
                code = self.pop[0][i].ssa_sd(
                    self.pop[1][i], self.pop[1][best_no], best, worst, self.pop[1][worst_no], self.sigma
                )
                self.decode_update2(i, code)
                if no >= self.sd:
                    break
