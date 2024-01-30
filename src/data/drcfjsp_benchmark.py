"""
5 6 4 # 工件数量 机器数量 工人数量
3 3 3 3 3  # 工件的工序数量
3 1 2 1 150 3 152 2 2 2 128 4 134 3 2 1 148 4 154 # 工件1的第1道工序：3台机器可用 第1台可用机器为1 对应有2个工人 第1个工人为1 加工时间为150 第2个工人为3 加工时间为152
2 4 2 2 145 3 147 2 2 2 135 4 141
2 4 2 2 155 3 157 5 2 1 163 2 168
2 1 2 1 217 3 219 3 2 1 153 4 159 # 工件2的第一道工序：
2 3 2 1 90 4 96 2 2 2 71 4 77
2 5 2 1 181 2 186 6 2 3 97 4 103
2 1 2 1 90 3 92 2 2 2 67 4 73 # 工件3的第一道工序：
2 3 2 1 183 4 189 4 2 2 110 3 112
3 4 2 2 195 3 197 5 2 1 103 2 108 6 2 3 155 4 161
2 1 2 1 90 3 92 2 2 2 70 4 76 # 工件4的第一道工序：
1 5 2 1 176 2 181
2 4 2 2 150 3 152 6 2 3 138 4 144
3 2 2 2 128 4 134 3 2 1 148 4 154 1 2 1 131 3 133 # 工件5的第一道工序：
3 3 2 1 89 4 95 4 2 2 70 3 72 5 2 1 50 2 55
2 5 2 1 113 2 118 6 2 3 87 4 93
"""
instance = {
    "DMFJS01": """5 6 4
3 3 3 3 3 
3 1 2 1 150 3 152 2 2 2 128 4 134 3 2 1 148 4 154 
2 4 2 2 145 3 147 2 2 2 135 4 141 
2 4 2 2 155 3 157 5 2 1 163 2 168 
2 1 2 1 217 3 219 3 2 1 153 4 159 
2 3 2 1 90 4 96 2 2 2 71 4 77 
2 5 2 1 181 2 186 6 2 3 97 4 103 
2 1 2 1 90 3 92 2 2 2 67 4 73 
2 3 2 1 183 4 189 4 2 2 110 3 112 
3 4 2 2 195 3 197 5 2 1 103 2 108 6 2 3 155 4 161 
2 1 2 1 90 3 92 2 2 2 70 4 76 
1 5 2 1 176 2 181 
2 4 2 2 150 3 152 6 2 3 138 4 144 
3 2 2 2 128 4 134 3 2 1 148 4 154 1 2 1 131 3 133 
3 3 2 1 89 4 95 4 2 2 70 3 72 5 2 1 50 2 55 
2 5 2 1 113 2 118 6 2 3 87 4 93 """,
    "DMFJS02": """""",
    "DMFJS03": """""",
    "DMFJS04": """""",
    "DMFJS05": """""",
    "DMFJS06": """""",
    "DMFJS07": """""",
    "DMFJS08": """""",
    "DMFJS09": """""",
    "DMFJS10": """""",
    "DMk01": """""",
    "DMk02": """""",
    "DMk03": """""",
    "DMk04": """""",
    "DMk05": """""",
    "DMk06": """""",
    "DMk07": """""",
    "DMk08": """""",
    "DMk09": """""",
    "DMk10": """""",
}
best_known = {
    "DMFJS01": None,
    "DMFJS02": None,
    "DMFJS03": None,
    "DMFJS04": None,
    "DMFJS05": None,
    "DMFJS06": None,
    "DMFJS07": None,
    "DMFJS08": None,
    "DMFJS09": None,
    "DMk01": None,
    "DMk02": None,
    "DMk03": None,
    "DMk04": None,
    "DMk05": None,
    "DMk06": None,
    "DMk07": None,
    "DMk08": None,
    "DMk09": None,
    "DMk10": None,
}
