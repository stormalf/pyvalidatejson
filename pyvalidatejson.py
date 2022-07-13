#!/usr/bin/python3
import json
import os
import argparse



__version__ = "1.0.0"


def pyvalidatejsonVersion():
    return f"pyvalidatejson version : {__version__}"



def parse_json(filename):
    
    with open(filename) as f:
        return json.load(f)

#root_dir = '.'
def main():
    for directory, subdirectories, files in os.walk(args.dir):
        for file in files:
            if file.endswith(".json"):
                try:
                    parse_json(os.path.join(directory, file))
                except json.decoder.JSONDecodeError as e: 
                    print(os.path.join(directory, file))
                    print(f"JSONDecodeError : {e}")
            

if __name__== "__main__":
    parser = argparse.ArgumentParser(description="pyvalidatejson is a python3 program that displays json files with incorrect format")
    parser.add_argument('-V', '--version', help='Display the version of pyvalidatejson', action='version', version=pyvalidatejsonVersion())
    parser.add_argument('dir', help = "directory to scan json files with .json extension only")
    args = parser.parse_args()
    main()