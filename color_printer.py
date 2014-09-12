from subprocess import call
from rgb_converter import rgb256

def print_colors(rgb_colors):

  def to_color_string(ansi_color):
    length = 1;

    return "\033[48;5;" + ansi_color + "m" + " "*length + "\033[m"

  ansi_colors = map(rgb256, rgb_colors) 
  color_strings = map(str, ansi_colors) 
  commands = map(to_color_string, ansi_colors)
  
  command_string = "".join(commands)
  
  call("echo " + "\"" + command_string + "\"", shell=True)


