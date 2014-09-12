#adapted from https://github.com/tehmaze/ansi

def rgb256(rgb_color):
    r = rgb_color[0]
    g = rgb_color[1]
    b = rgb_color[2]

    grey = False
    poss = True
    step = 2.5

    while poss: # As long as the colour could be grey scale
        if r < step or g < step or b < step:
            grey = r < step and g < step and b < step
            poss = False

        step += 42.5

    if grey:
        colour = 232 + int(float(sum([r, g, b]) / 33.0))
    else:
        colour = sum([16] + [int (6 * float(val) / 256) * mod
            for val, mod in ((r, 36), (g, 6), (b, 1))])

    return str(colour)
