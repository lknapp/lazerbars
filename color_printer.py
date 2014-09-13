from subprocess import call
from rgb_converter import rgb256_to_rgb8
from rgb_converter import hsv_to_rgb256 

def print_colors(hsv_colors):

  rgb_colors = (hsv_to_rgb256(hsv_colors))

  def to_color_string(ansi_color):
    length = 1;

    return "\033[48;5;" + ansi_color + "m" + " "*length + "\033[m"

  ansi_colors = map(rgb256_to_rgb8, rgb_colors) 
  color_strings = map(str, ansi_colors) 
  commands = map(to_color_string, ansi_colors)
  
  command_string = "".join(commands)
  
  call("echo " + "\"" + command_string + "\"", shell=True)


