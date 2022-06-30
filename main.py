#pylint:disable=W0101
#pylint:disable=W0621
#pylint:disable=W0703
import pickle, traceback, os
from termcolor import cprint, colored
from utils.configparser import parse as parseConfig
from utils.path import path as mpath, ps

def error(msg = "", err = None, formatsize=0, color = 'red'):
	if err:
		errtext = str(traceback.format_exc(formatsize))
	if err and not msg:
		error("Error: \n"+errtext)
		return
	cprint(msg, color)
	if err:
		cprint(errtext, color)

# BX Class
class BX:
	def __init__(self):
		self.memory = self.buffer = []
	
	def init_mem(self, size, path):
		self.p('Initializing memory...')
		if not os.path.exists(path):
			self.clearMem(path)
		memFile = open(path, 'rb')
		self.memory = []
		memFile.flush()
		self.p('Checking memory file...')
		if os.path.getsize(path): # if file contains anything
			self.p('Memory file not empty')
			self.p('Reading memory from file...')
			try:
				self.memory = pickle.load(memFile)
				self.p('Successfully readed')
				if len(self.memory) != size:
					self.p('Memory size invalid')
					self.clearMem()
					self.p('Clearing memory...')
					self.p('Please restart program.')
					exit()
			except Exception as er:
				error('Error occured', er)
				self.clearMem()
				exit()
		else: # if file empty (size=0)
			#self.p('Memory file empty')
			#self.p('Creating memory...')
			self.memory = [0 for i in range(size)]
			#self.p('Saving memory in file...')
			self.saveMem(path)
		self.p(f'Memory size: {len(self.memory)}')
		memFile.close()
		
	def init_buffer(self, size):
		#self.p('Creating Buffer...')
		self.buffer = [0 for i in range(size)]
		self.p(f'Buffer size: {len(self.buffer)}')
	
	def saveMem(self, path):
		with open(path,'wb') as f:
			pickle.dump(self.memory, f)
	
	def clearMem(self, path):
		open(path,'w').close()
	
	# Run Code
	def run(self, path):
		#configPath = filePath.split('/')
		#configPath.pop()
		#configPath = '/'.join(configPath)
		configPath = path + ps + 'config.yml'
		config = parseConfig(configPath)
		perms = config.get('permissions', [])
		if 'python' in perms or 'terminal' in perms:
			cprint("************\n* WARNING! *\n************", 'yellow')
			cprint(f'This program can execute {"Python" if "python" in perms else "Terminal"} code!','yellow')
			ans = ''
			while ans.lower() != 'y' and ans.lower() != 'n':
				ans = input(colored('Continue? [Y/n] ','yellow'))
			if ans.lower() == 'n': return
		entrance = ps + config.get('script', {'entrance': 'main.bx'})['entrance']
		filePath = path + entrance
		self.init_mem(int(config['requirements']['sizes']['mem']), path+ps+'memory.dat')
		self.init_buffer(int(config['requirements']['sizes']['buf']))
		memory = self.memory
		buffer = self.buffer
		codeFile = open(filePath)
		try:
			code = codeFile.read().split('\n')
			from lang.bytex import BX as _BX
			self.p('[Code started]\n')
			_BX(code=code,mem=memory,buf=buffer,config=config)
		except Exception as er:
			error('Error occured while executing code:', er, formatsize=3)
		finally:
			codeFile.close()
			self.p('\n[Code finished]')
	
	def p(self, *args):
		print(*args)

if __name__ == '__main__':
	import sys
	args = sys.argv[1:]
	def interface():
		bx = BX()
		if args:
			path = args[0]
			print(f'Running script at {path}')
			bx.run(path)
		else:
			pre_location = mpath('scripts/examples/')
			print('Select script:')
			name = input(pre_location)
			print(mpath(pre_location+name+ps+'<entrance point>'))
			bx.run(pre_location+name)
			#bx.saveMem()
	interface()