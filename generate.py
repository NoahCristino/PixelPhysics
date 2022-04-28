import cv2, random
import numpy as np
from draw import get_map, draw_pixel

w, h = 400, 400
plrs = 4
teams = []
team_colors = []

def placePlayers(arr):
    x = random.randint(0,w-1)
    y = random.randint(0,h-1)
    while np.array_equal(arr[x][y], np.array([0, 255, 0])) == False:
        x = random.randint(0,w-1)
        y = random.randint(0,h-1)
    team_color = np.array([random.randint(0,255), random.randint(0,255), random.randint(0,255)])
    draw_pixel(arr, x, y, team_color)
    teams.append([(x,y)])
    team_colors.append(team_color)

def get_neighbors(arr, team):
    pt = random.choice(teams[team])
    valid = []
    ctr = 0
    while True:
        valid.append((pt[0]+1, pt[1]+1))
        valid.append((pt[0]+1, pt[1]))
        valid.append((pt[0]+1, pt[1]-1))
        valid.append((pt[0]-1, pt[1]+1))
        valid.append((pt[0]-1, pt[1]))
        valid.append((pt[0]-1, pt[1]-1))
        valid.append((pt[0], pt[1]+1))
        valid.append((pt[0], pt[1]-1))
        rm = []
        for v in valid:
            if v[0] > w-1 or v[0] < 0 or v[1] > h-1 or v[1] < 0 or np.array_equal(arr[v[0]][v[1]], np.array([255, 0, 0])) or np.array_equal(arr[v[0]][v[1]], team_colors[team]):
                rm.append(v)
                continue
        for r in rm:
            valid.remove(r)
        #print(len(valid))
        if len(valid) > 0:
            return random.choice(valid)
        pt = random.choice(teams[team])
        ctr+=1
        if (ctr == 100):
            return
            

map = get_map()

for i in range(plrs):
    placePlayers(map)

print(teams)
while True:
    for i in range(plrs):
        n = get_neighbors(map, i)
        if n != None:
            teams[i].append((n[0], n[1]))
            draw_pixel(map, n[0], n[1], team_colors[i])

    cv2.imshow('image', map)
    k = cv2.waitKey(1)
    if k == 27:         # If escape was pressed exit
        cv2.destroyAllWindows()
        break
    #if k == 97:
        #map = draw_pixel(map, 399, 399, np.array([0,0,255]))
        #map = draw_pixel(map, random.randint(0,399), random.randint(0,399), np.array([0,0,255]))