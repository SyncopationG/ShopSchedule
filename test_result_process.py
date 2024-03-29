__doc__ = """
工具，结果汇总处理
"""

import os

import numpy as np
import pandas as pd

from src.test_setting import N_EXP

dir_result = r"GA_FjspNew_dpox"
"================================================================================================================="
dir_file = r"E:\Python\ShopSchedule\%s" % dir_result
save_to = r"%s\%s.csv" % (dir_file, dir_result)
try:
    os.remove(save_to)
except FileNotFoundError:
    pass
name_csv_file_list = [i for i in os.listdir(dir_file) if os.path.splitext(i)[1] == ".csv"]
data = "group,case,min.,max.,avg.,std."
for i in range(1, N_EXP + 1):
    data += ",%s" % i
data += "\n"
for name_csv_file in name_csv_file_list:
    name_csv_file = os.path.splitext(name_csv_file)[0]
    val_read_file = pd.read_csv(r"%s\%s.csv" % (dir_file, name_csv_file))
    val_obj = val_read_file.loc[:9, "Objective"]
    data += "%s,%s" % (dir_result, name_csv_file)
    val_min = np.min(val_obj)
    val_max = np.max(val_obj)
    val_avg = np.mean(val_obj)
    val_std = np.std(val_obj)
    data += ",{:},{:},{:.2f},{:.2f}".format(val_min, val_max, val_avg, val_std, )
    for val in val_obj:
        data += ",%s" % int(val)
    data += "\n"
    print(name_csv_file)
with open(save_to, "w", encoding="utf-8") as f:
    f.write(data)
"================================================================================================================="
print(save_to)
