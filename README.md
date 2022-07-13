# pyvalidatejson.py

a very small python program to validate json files format by scanning a directory and analyze all \*.json.
It prints only the incorrect JSON file with first issue found into the json file.

## usage

./pyvalidatejson.py --help

    usage: pyvalidatejson.py [-h] [-V] dir

    pyvalidatejson is a python3 program that displays json files with incorrect format

    positional arguments:
    dir            directory to scan json files with .json extension only

    optional arguments:
    -h, --help     show this help message and exit
    -V, --version  Display the version of pyvalidatejson

## Examples :

./pyvalidatejson.py .

    ./fail1.json
    JSONDecodeError : Expecting ',' delimiter: line 1 column 18 (char 17)
    ./fail21.json
    JSONDecodeError : Expecting ',' delimiter: line 1 column 26 (char 25)
    ./fail18.json
    JSONDecodeError : Expecting ':' delimiter: line 1 column 18 (char 17)
    ./fail20.json
    JSONDecodeError : Expecting ':' delimiter: line 1 column 26 (char 25)
    ./fail2.json
    JSONDecodeError : Expecting property name enclosed in double quotes: line 1 column 2 (char 1)
    ./fail16.json
    JSONDecodeError : Invalid \escape: line 1 column 29 (char 28)
    ./fail9.json
    JSONDecodeError : Extra data: line 1 column 35 (char 34)
    ./fail22.json
    JSONDecodeError : Expecting value: line 1 column 15 (char 14)
    ./fail14.json
    JSONDecodeError : Invalid \escape: line 1 column 29 (char 28)
    ./fail24.json
    JSONDecodeError : Invalid control character at: line 1 column 3 (char 2)
    ./fail0.json
    JSONDecodeError : Expecting ',' delimiter: line 1 column 12 (char 11)
    ./fail15.json
    JSONDecodeError : Expecting value: line 1 column 2 (char 1)
    ./fail28.json
    JSONDecodeError : Expecting ',' delimiter: line 1 column 3 (char 2)
    ./fail17.json
    JSONDecodeError : Expecting property name enclosed in double quotes: line 1 column 41 (char 40)
    ./fail13.json
    JSONDecodeError : Expecting ',' delimiter: line 1 column 28 (char 27)
    ./fail23.json
    JSONDecodeError : Expecting value: line 1 column 2 (char 1)
    ./fail19.json
    JSONDecodeError : Expecting value: line 1 column 17 (char 16)
    ./fail25.json
    JSONDecodeError : Invalid \escape: line 1 column 6 (char 5)
    ./fail5.json
    JSONDecodeError : Expecting value: line 1 column 5 (char 4)
    ./fail27.json
    JSONDecodeError : Invalid \escape: line 1 column 7 (char 6)
    ./fail4.json
    JSONDecodeError : Expecting value: line 1 column 23 (char 22)
    ./fail29.json
    JSONDecodeError : Expecting ',' delimiter: line 1 column 3 (char 2)
    ./fail26.json
    JSONDecodeError : Invalid control character at: line 1 column 7 (char 6)
    ./fail12.json
    JSONDecodeError : Expecting ',' delimiter: line 1 column 41 (char 40)
    ./fail7.json
    JSONDecodeError : Extra data: line 1 column 16 (char 15)
    ./fail11.json
    JSONDecodeError : Expecting value: line 1 column 24 (char 23)
    ./fail3.json
    JSONDecodeError : Expecting value: line 1 column 16 (char 15)
    ./fail10.json
    JSONDecodeError : Expecting ',' delimiter: line 1 column 26 (char 25)
    ./fail30.json
    JSONDecodeError : Expecting ',' delimiter: line 1 column 3 (char 2)
    ./fail6.json
    JSONDecodeError : Extra data: line 1 column 26 (char 25)
    ./fail8.json
    JSONDecodeError : Expecting property name enclosed in double quotes: line 1 column 22 (char 21)
