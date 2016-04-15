import os
from collections import OrderedDict
from operator import itemgetter

list_of_file_names = {}

#definition of the file directory
def get_file_size(directory = '/etc', reverse= 'False'):
	for root,dirs, files in os.walk(directory):
		for file in files:
			path_to_file = os.path.join(root, file)
			list_of_file_names[path_to_file]=os.path.getsize(path_to_file)

		return OrderedDict(sorted(list_of_file_names.items(), key=itemgetter(1), reverse = reverse))

#definition how to write a file in d directory
import time
timestamp = int(time.time())

def file_write(file_path, d):
	file_path = '/tmp/file'

	timestamp_files = open(file_path, 'w')
	for key, value in d.items():
		timestamp_files.write("{}: {}\n".format(key, value))
	
	timestamp_files.close()

#running the application & user input
if __name__ == '__main__':
	import argparse

	parser = argparse.ArgumentParser(description ='Script to list out files given from given directory')

	parser.add_argument('--directory', '-d', required=True, help='Source directory')
	parser.add_argument('--reverse', '-r', action='store_true', help='If set, reverse order')
	parser.add_argument('--file_path', '-fp', help = 'Change file directory')
	
	args = parser.parse_args()
	
  
	d = get_file_size(directory=args.directory, reverse=args.reverse)
	file_write(args.file_path, d)


	
	
