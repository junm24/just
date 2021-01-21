layout = [[".",".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".",".","."],[".",".","B",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".",".","."],[".",".",".",".",".","L",".",".",".","."],[".",".",".",".",".",".",".",".",".","R"]]
rock = []
barn = []
lake = []
for i in range(len(layout)):
    for j in range(len(layout)):
        row = layout[i]
        if row[j] == "R":
            rock = [i+1,j+1]
        elif row[j] == "B":
            barn = [i+1, j+1]
        elif row[j] == "L":
            lake = [i+1, j+1]
# if rock[0] not in list(range(min(barn[0], lake[0]), max(barn[0], lake[0]))) and rock[1] not in list(range(min(barn[1], lake[1]), max(barn[1], lake[1]))):
    print(len(list(range(min(barn[0], lake[0]), max(barn[0], lake[0])))) + len(list(range(min(barn[1], lake[1]), max(barn[1], lake[1])))) - 1)