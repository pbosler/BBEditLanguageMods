#!/usr/bin/env python

import sys, getopt, os, glob

def print_usage():
	print('usage: copy_plists_to_library.py [-t --tw --textwrangler -b --bb --bbedit -h --help -v --version]')

def print_version():
	print('BBEditLanguageMods: version 1.0')

def print_note():
	print('NOTE: For these language module changes to take effect, you must restart your text editor.')

def main(argv):
	try:
		opts, args = getopt.getopt(argv, "hvtb", ["tw", "textwrangler", "bb", "bbedit", "help", "version"])
	except getopt.GetoptError:
		print_usage()
		sys.exit(1)
	if len(opts) == 0:
		print_usage()
		sys.exit(1)

	commands = []
	for opt, arg in opts:
		if opt == '-h' or opt == "--help":
			print_usage()
			sys.exit()
		elif opt in ("-t", "--tw", "--textwrangler"):
			print("TO DO: Find TextWrangler directory.")
#			for file in glob.glob("*.plist"):
#				commands.append("cp " + file + " $HOME/Desktop/.")
		elif opt in ("-b", "--bb", "--bbedit"):
			for file in glob.glob("*.plist"):
				commands.append("cp " + file + " $HOME/Library/Application\ Support/BBEdit/Language\ Modules/.")
		elif opt == '-v' or opt == '--version':
			print_version()

	for cmd in commands:
		print(cmd)
		os.system(cmd)

	print_note()

if __name__ == "__main__":
	main(sys.argv[1:])

