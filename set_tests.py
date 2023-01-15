from minesweeper import Minesweeper, MinesweeperAI

cells = [(0,0),(1,0),(0,1),(1,1),(1,0)]
set_cells = set(cells)
set_set_cells = set(set_cells)
print("Array cells : ",cells)
print("Set cells : ", set_cells)
print("Set Set cells : ", set_set_cells)


cells = [(0,0),(0,2),(2,2),(2,0),(1,1)]
minesweeperAI = MinesweeperAI(3,3)
i = 1
for cell in cells:
    minesweeperAI.add_knowledge(cell, i)
    i += 1

