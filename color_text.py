from termcolor import colored, cprint

def color_text(txt):
   t=colored(txt,'yellow','on_red',attrs=['bold','underline'])
   print(t)

txt=colored(input("enter text"))
color_text(txt)