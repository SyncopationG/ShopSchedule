import numpy as np


class Objective:
    @staticmethod
    def total_workload(info):  # 机器的总负荷
        a = 0
        for machine in info.schedule.machine.values():
            a += machine.end
            for i, j in zip(machine.idle[0][:-1], machine.idle[1][:-1]):
                k = j - i
                a -= k
        return a

    @staticmethod
    def max_workload(info):  # 机器的最大负荷
        a = []
        for machine in info.schedule.machine.values():
            b = machine.end
            for i, j in zip(machine.idle[0][:-1], machine.idle[1][:-1]):
                k = j - i
                b -= k
            a.append(b)
        return max(a)

    @staticmethod
    def makespan(info):  # 工期
        return max([machine.end for machine in info.schedule.machine.values()]) / info.schedule.time_unit

    @staticmethod
    def total_makespan(info):  # 工件的完工时间之和
        return sum([job.end for job in info.schedule.job.values()]) / info.schedule.time_unit

    @staticmethod
    def total_flow_time(info):  # 工件的流程时间之和
        return sum([job.end - job.start for job in info.schedule.job.values()]) / info.schedule.time_unit

    @staticmethod
    def n_tardiness_job(info):  # 拖期工件数量
        time_unit = info.schedule.time_unit
        return sum([max([0, np.sign(job.end - job.due_date)]) for job in info.schedule.job.values()]) / time_unit

    @staticmethod
    def tardiness(info):  # 拖期
        time_unit = info.schedule.time_unit
        return sum([max([0, job.end - job.due_date]) for job in info.schedule.job.values()]) / time_unit

    @staticmethod
    def earliness(info):  # 提前期
        time_unit = info.schedule.time_unit
        return sum([max([0, job.due_date - job.end]) for job in info.schedule.job.values()]) / time_unit
