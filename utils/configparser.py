from configparser import ConfigParser

def parse(path):
	parser = ConfigParser()
	parser.read(path)
	return parser