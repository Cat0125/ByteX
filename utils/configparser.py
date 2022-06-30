import yaml

def parse(path):
	with open(path) as file:
		return yaml.safe_load(file)

if __name__ == '__main__':
	import pprint
	pprint.pprint(parse('test.yml'))