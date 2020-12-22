import compiler
import sys
import argparse

#set up argparse
parser = argparse.ArgumentParser(description='Compiler for the slatt programming language')

parser.add_argument("filename", help='    slattlang file to be compiled')

args = parser.parse_args()

arg_dict = vars(args) #set arg dictionary to easily callable variable for later

#######

sl_fname = arg_dict['filename']
compiler.sl_compile(sl_fname)