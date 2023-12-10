
with open("files/day10.txt", "r") as file_stream:
    lines = file_stream.readlines()

dir_options = {
    '|': [(-1, 0), (1, 0)],
    '-': [(0, -1), (0, 1)],
    'L': [(-1, 0), (0, 1)],
    'J': [(-1, 0), (0, -1)],
    '7': [(0, -1), (1, 0)],
    'F': [(0, 1), (1, 0)],
    'S': [(-1, 0), (0, -1), (0, 1), (1, 0)],
}
dir_values = {
    (-1, 0): {'|', '7', 'F'},
    (0, -1): {'-', 'L', 'F'},
    (0, 1): {'-', 'J', '7'},
    (1, 0): {'|', 'J', 'L'},
}

wall_options = {
    'F': 'J',
    'L': '7'
}

grid = [list(line) for line in lines]
start = None
for a, row in enumerate(grid):
    for b, cell in enumerate(row):
        if cell == 'S':
            start = (a, b, 0)

# Manual entry after looking at grid
grid[start[0]][start[1]] = '|'

queue = [start]
saved = {}
while len(queue) > 0:
    a, b, dist = queue.pop(0)
    if (a, b) in saved:
        continue

    value = grid[a][b]
    saved[(a, b)] = value

    for c, d in dir_options[value]:
        e, f = a+c, b+d
        pos_value = grid[e][f]
        if pos_value in dir_values[(c, d)]:
            queue.append((e, f, dist+1))

inside = False
wall = None
count = 0
for a, row in enumerate(grid):
    for b, cell in enumerate(row):
        if (a, b) in saved.keys():
            if cell == '|':
                inside = not inside
            elif cell != '-':
                if wall is None:
                    wall = cell
                else:
                    if cell == wall_options[wall]:
                        inside = not inside
                    wall = None
        else:
            if inside:
                count += 1
print(count)

