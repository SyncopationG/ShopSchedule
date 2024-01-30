__doc__ = """
甘特图
"""

from src import *

"""Decode result"""
# file_dir = f"./{dir_DecodeTest}/GanttChart"  # 甘特图数据文件所在目录
# save_dir = f"./{dir_DecodeTest}/GanttChartPngHtml"  # 生成的甘特图保存目录
# file = "example.csv"  # 甘特图数据文件
# file_save = "%s/%s" % (save_dir, file[:-4])  # 保存的甘特图名称
"""Algorithm result"""
save = "GA_JSPWT"
instance = "case1"
exp = "1"
file_dir = "./%s/%s/GanttChartReal" % (save, instance)  # 甘特图数据文件所在目录
save_dir = "./%s/%s/GanttChartPngHtml" % (save, instance)  # 生成的甘特图保存目录
file = "%s.csv" % exp  # 甘特图数据文件
file_save = "%s/%s" % (save_dir, file[:-4])  # 保存的甘特图名称
"""===================================================================================="""
a = GanttChart("%s/%s" % (file_dir, file))  # 调用甘特图生成类
a.gantt_chart_png(
    filename=file_save, fig_width=9, fig_height=5, random_colors=False, lang=0,
    dpi=200, height=0.8, scale_more=12, x_step=a.schedule.makespan // 10,
    y_based=0, text_rotation=0,
    with_operation=True, with_start_end=False, key_block=False, show=False
)  # 绘制png格式的甘特图
a.gantt_chart_html(date="2020 7 6", filename=file_save, show=False, lang=0)  # 绘制html格式的甘特图
"""===================================================================================="""
"""Worktimetable"""
if save[-2:] == "WT":
    file_dir = "./%s/%s/GanttChart2" % (save, instance)  # 甘特图数据文件所在目录
    save_dir = "./%s/%s/GanttChartPngHtml2" % (save, instance)  # 生成的甘特图保存目录
    file = "%s.csv" % exp  # 甘特图数据文件
    file_save = "%s/%s" % (save_dir, file[:-4])  # 保存的甘特图名称
    a2 = GanttChart("%s/%s" % (file_dir, file))  # 调用甘特图生成类
    a2.schedule.time_unit = 60  # 设置加工时间单位
    a2.gantt_chart_html(date="2020 7 6", filename=file_save, show=False, lang=0)  # 绘制html格式的甘特图
