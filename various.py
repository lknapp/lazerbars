def increment_color(hsv_color):
  velocity = 0.01
  hsv_color[0] += velocity
  hsv_color[0] = hsv_color[0]%1

hsv_colors = []
frame = 0

for i in range(64):
  hsv_colors.append([((4*i-1)%256)/256.0, 1, 1])

def modify_sinusoidally(hsv_color):
  velocity = math.sin(math.radians(frame*5))/100.0
  hsv_color[0] += velocity
  hsv_color[0] = hsv_color[0]%1


