import json
import argparse

parse = argparse.ArgumentParser(description="CM2 Code assembler. Made by KO6BXL")
parse.add_argument('-f', type=open,help="File to convert into assembly")
parse.add_argument('-c', type=open,help="Config for convertion.")
parse.add_argument('-o', type=str,help="Config for convertion.")
args = parse.parse_args()

code_file = args.f.read()
conf_file = args.c.read()
out_file = open(args.o, 'w')


