import noise
import cv2
import numpy as np

def my_filter(i):
    #print(i)
    #print(np.shape(i))
    #print(np.shape(np.array([0, 163, 108])))
    if (i[0] > 100):
        return np.array([255, 0, 0])
    return np.array([0, 255, 0])

def getMap():
    shape = (400,400)
    scale = .3
    octaves = 6
    persistence = 0.5
    lacunarity = 2.1
    seed = np.random.randint(0,100)

    world = np.zeros(shape)

    # make coordinate grid on [0,1]^2
    x_idx = np.linspace(0, 1, shape[0])
    y_idx = np.linspace(0, 1, shape[1])
    world_x, world_y = np.meshgrid(x_idx, y_idx)

    # apply perlin noise, instead of np.vectorize, consider using itertools.starmap()
    world = np.vectorize(noise.pnoise2)(world_x/scale,
                            world_y/scale,
                            octaves=octaves,
                            persistence=persistence,
                            lacunarity=lacunarity,
                            repeatx=400,
                            repeaty=400,
                            base=seed)

    # here was the error: one needs to normalize the image first. Could be done without copying the array, though
    gray_img = np.floor((world + .5) * 255).astype(np.uint8) # <- Normalize world first
    img = cv2.cvtColor(gray_img,cv2.COLOR_GRAY2RGB)
    for a, line in enumerate(img):
        for b, element in enumerate(line):
            np.put(img[a][b], [0, 1, 2], my_filter(img[a][b]))

    l2 = cv2.resize(img, (1000, 1000))
    return l2
