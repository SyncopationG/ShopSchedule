"""
5 5 工件数量 工序数量
2 4 3 工件1的加工路径数量 加工路径1的工序数量 加工路径*的工序数量
0 14 2 18 1 25 4 15 工件1的加工路径1
4 22 3 30 0 35 工件1的加工路径*
2 3 2 工件2的加工路径数量 加工路径1的工序数量 加工路径*的工序数量
1 15 2 14 3 12
2 22 4 19
3 3 3 4
3 16 0 32 1 21
4 17 1 28 2 24
1 18 2 12 0 25 2 15
3 3 4 4
0 23 3 26 1 32
2 18 4 16 1 15 4 31
3 22 2 16 0 16 2 19
2 3 2
1 31 4 14 3 15
3 28 0 30
"""
instance = {
    # 2012 An artificial immune algorithm for multiple-route job shop scheduling problem
    "example": """5 5
2 4 3
0 14 2 18 1 25 4 15
4 22 3 30 0 35
2 3 2
1 15 2 14 3 12
2 22 4 19
3 3 3 4
3 16 0 32 1 21
4 17 1 28 2 24
1 18 2 12 0 25 2 15
3 3 4 4
0 23 3 26 1 32
2 18 4 16 1 15 4 31
3 22 2 16 0 16 2 19
2 3 2
1 31 4 14 3 15
3 28 0 30""",
    "example2": """8 7
2 4 4
1 48 2 42 3 37 5 35
3 45 1 38 2 43 0 33
2 4 3
1 46 0 42 3 41 4 29
5 52 6 53 5 59
3 4 3 3
4 47 6 43 5 38 3 25
4 56 1 45 0 49
0 35 4 52 1 54
3 5 4 5
6 35 0 42 2 37 3 33 1 48
2 45 3 54 4 46 6 47
3 33 5 32 4 47 1 45 3 51
2 3 3
5 34 3 26 0 45
4 42 2 37 1 28
2 4 4
6 22 0 34 2 27 4 38
0 23 5 28 0 25 2 45
2 4 3
2 33 4 28 5 39 0 43
2 43 5 47 3 48
2 4 4
1 22 2 34 4 31 3 26
3 24 0 29 5 32 6 27
""",
    "case1": """3 4
2 2 3 
3 2 1 5 
2 1 3 2 1 1 
3 2 3 3 
2 5 0 1 
1 3 3 5 2 2 
3 3 1 3 2 2 
2 3 3 
3 2 0 3 1 1 
1 4 2 4 3 4 
"""
}
best_known = {
    "example": None,
    "example2": None,
    "case1": 8,
}
