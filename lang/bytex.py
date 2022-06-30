#pylint:disable=W0122
import os

def BX(code,mem,buf,config):
	memory = mem
	buffer = buf
	m = memory
	
	def err(er, msg, line='<Err>'):
		raise er(f'{msg} (line {line})')
	
	def toArg(arg):
		try:
			return int(arg)
		except ValueError:
			return str(arg)
	
	def get(val):
		if val[0] == 'm':
			return m[int(val[1::])]
		elif val[0] == '@':
			return {
				'TEXT': '<built-in type TEXT>',
				'NUM': '<built-in type NUM>',
				'MEM': '<Memory object>',
				'BUF': '<Buffer object>',
			}[val[1::]]
		else:
			return toArg(val)
	
	i = 0
	while i < len(code):
		line = code[i].split('#')[0].strip().split(' ')
		if not code[i]:
			i += 1
			continue
		cmd = line[0].upper()
		args = line[1::]
		arg = ' '.join(args)
		if cmd == 'PRINT':
			print(get(arg))
		elif cmd == 'SET':
			m[get(args[0])] = get(args[1])
		elif cmd == 'USE':
			if args[0] == '@BUF':
				memory = m
				m = buffer
			elif args[0] == '@MEM':
				buffer = m
				m = memory
			else:
				raise err(TypeError, 'USE: Unrecognised type', i)
		elif cmd == 'ADD':
			m[get(args[0])] += type(m[get(args[0])])(get(args[1]))
		elif cmd == 'SUB':
			m[get(args[0])] -= get(args[1])
		elif cmd == 'MUP':
			m[get(args[0])] *= get(args[1])
		elif cmd == 'DIV':
			m[get(args[0])] /= get(args[1])
		elif cmd == 'OP':
			continue
		elif cmd == 'JUMP':
			if args[3] == '==' and get(args[2]) == get(args[4]):
				i = get(args[0])-1
				continue
			if args[3] == '!=' and get(args[2]) != get(args[4]):
				i = get(args[0])-1
				continue
			if args[3] == '>' and get(args[2]) > get(args[4]):
				i = get(args[0])-1
				continue
			if args[3] == '>=' and get(args[2]) >= get(args[4]):
				i = get(args[0])-1
				continue
			if args[3] == '<' and get(args[2]) < get(args[4]):
				i = get(args[0])-1
				continue
			if args[3] == '<=' and get(args[2]) <= get(args[4]):
				i = get(args[0])-1
				continue
		elif cmd == 'GET':
			if args[0] == '@NUM':
				data = None
				while type(data) != int:
					data = toArg(input('Enter number: '))
				m[int(args[1][1:])] = data
			elif args[0] == '@TEXT':
				m[int(args[1][1:])] = input('Enter text: ')
			else:
				raise err(TypeError, 'GET: Unrecognized type: ' + args[0], i)
		elif cmd == 'END':
			break
		elif cmd == 'PYTHON':
			if 'python' in config.get('permissions',['-']):
				exec(' '.join(args))
			else:
				err(PermissionError, 'Attempt to execute Python without permission', i)
		elif cmd == 'TERMINAL':
			if 'terminal' in config.get('permissions',['-']):
				os.system(' '.join(args))
			else:
				err(PermissionError, 'Attempt to execute shell without permission', i)
		else:
			err(SyntaxError, f'Invalid command: {cmd}', line)
		i += 1
	if len(m) == len(memory):
		memory = m