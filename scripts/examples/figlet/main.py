from os import system as term
from termcolor import colored
text = ''
print('Type "$quit" to quit')
while text != '$quit':
  text = input(colored('~', 'green') + ' $ figlet ')
  term(f'figlet {text}')