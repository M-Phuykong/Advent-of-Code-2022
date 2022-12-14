import pprint

dir = [(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1)]

dir_m = {
    "U": (0,1),
    "R": (1,0),
    "D": (0,-1),
    "L": (-1,0)
}

sign = lambda x: 1 if x > 0 else (-1 if x < 0 else 0)

def part1():
    global hx,hy,tx,ty
    dx = tx-hx
    dy = ty-hy
    
    # same col and row
    #
    if dx == 0 or dy == 0:
        if abs(dx) >= 2:
            tx -= sign(dx)
        if abs(dy) >= 2:
            ty -= sign(dy)
            
    # if the diagonal length is larger than 1
    #
    elif (abs(dx),abs(dy)) != (1,1):
        tx -= sign(dx)
        ty -= sign(dy)

global rope
rope = [[0,0] for _ in range(10)]

def part2(i):
    global hx, hy, tx, ty
    hx, hy = rope[i-1]
    tx, ty = rope[i]
    dx = tx-hx
    dy = ty-hy
    if dx == 0 or dy == 0:
        if abs(dx) >= 2:
            rope[i][0] -= sign(dx)
        if abs(dy) >= 2:
            rope[i][1] -= sign(dy)
    elif (abs(dx),abs(dy)) != (1,1):
        rope[i][0] -= sign(dx)
        rope[i][1] -= sign(dy)
    

def main():

    input_file = "Day9/input.txt"

    with open(input_file) as f:
        lines = list(map(str.strip,f.readlines()))

    visit = set()
    global hx,hy,tx,ty
    hx,hy = 0,0
    tx,ty = 0,0

    for line in lines:
        d, size = line.split()
        visit.add(tuple(rope[-1]))
        x,y = dir_m[d]

        for i in range(int(size)):
            
            rope[0][0] += x
            rope[0][1] += y

            for i in range(1,10):
                part2(i)

            visit.add(tuple(rope[-1]))
            # part1()
            # visit.add((tx,ty))

    print(len(visit))

if __name__ == "__main__":
    main()

