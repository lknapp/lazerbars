from colorsys import hsv_to_rgb

def hsv_to_rgb256(hsv_color_array):
  #TODO: make more functional
  rgb_256_colors = []
  for i in range(len(hsv_color_array)): 
    h = hsv_color_array[i][0]
    s = hsv_color_array[i][1]
    v = hsv_color_array[i][2]
    (r, g, b) = hsv_to_rgb(h, s, v)
    r *= 256
    g *= 256
    b *= 256
    r = int(r) - 1
    g = int(g) - 1
    b = int(b) - 1
    rgb_256_colors.append([r, g, b])
  return rgb_256_colors


def rgb256_to_rgb8(rgb_color):

    #adapted from https://github.com/tehmaze/ansi
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
