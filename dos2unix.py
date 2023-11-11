#dos2unix.py - it is utility that convert the /r/n to /n
# learning reading and writing files
#2 argparser
#3 format string 
import argparse
import os
def str2unix(input_str: str) -> str:
    return input_str.replace('\r\n','\n')

def dos2unix(source_file: str, dest_file: str):
    #line = []
    with open(source_file,'r') as reader:
        line = reader.read()
    with open(dest_file,'w') as writer:
        writer.write(str2unix(line))
		
		
		
if __name__ == '__main__':
	parser = argparse.ArgumentParser(description="Script that converts a DOS like file to an Unix like file",)
	parser.add_argument('source_file',help='The location of the source ')
	parser.add_argument('--dest_file', \
						help='Location of dest file (default: source_file appended with `_unix`', \
						default=None)

	args = parser.parse_args()
	src_file = args.source_file
	dest_file = args.dest_file

	if dest_file is None:
		dir_path,file_extension = os.path.splitext(src_file)
		dest_file = f'{dir_path}_unix{file_extension}'

	dos2unix(src_file,dest_file)
