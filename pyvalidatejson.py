#!/usr/bin/python3
import json
import os
import argparse



__version__ = "1.0.0"

global nbdir
global nbfiles

nbdir = 0
nbfiles = 0

def pyvalidatejsonVersion():
    return f"pyvalidatejson version : {__version__}"



def parse_json(filename):
    
    with open(filename) as f:
        return json.load(f)

#root_dir = '.'
def main():
    global nbdir
    global nbfiles
    for directory, subdirectories, files in os.walk(args.dir):
        if args.debug:
            print(f"directory scanned : {directory}")
        nbdir +=1
        for file in files:
            if file.endswith(".json"):
                if args.debug:
                    print(f"file scanned : {file}")
                nbfiles += 1
                try:
                    parse_json(os.path.join(directory, file))
                except json.decoder.JSONDecodeError as e: 
                    print(os.path.join(directory, file))
                    print(f"JSONDecodeError : {e}")
    print(f"Number of directories scanned : {nbdir}, number of files scanned :  {nbfiles}")
            

if __name__== "__main__":
    parser = argparse.ArgumentParser(description="pyvalidatejson is a python3 program that displays json files with incorrect format")
    parser.add_argument('-V', '--version', help='Display the version of pyvalidatejson', action='version', version=pyvalidatejsonVersion())
    parser.add_argument('dir', help = "directory to scan json files with .json extension only")
    parser.add_argument('-d', '--debug', help='print debug information', action="store_true", required=False)
    args = parser.parse_args()
    main()