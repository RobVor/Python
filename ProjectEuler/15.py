"""Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.


How many such routes are there through a 20×20 grid?"""

GridSize = 20

def BuildGrid(Size):
    Grid = {}
    for i in range(1,Size + 1):
        Grid.setdefault(i,list())
        for j in range(1, Size + 1):
            Grid.setdefault(i,list()).append(j*i)
    return Grid

def Moves(Grid):
    Counter = [1] * len(Grid)
    for i in range(len(Grid)):
        for j in range(i):
            Counter[j] = Counter[j] + Counter[j - 1]
        Counter[i] = 2 * Counter[i - 1]
    return Counter[len(Grid) - 1]

for gr in BuildGrid(GridSize).items():
    print(gr)

print(Moves(BuildGrid(GridSize)))