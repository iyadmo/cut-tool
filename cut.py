import sys

if len(sys.argv) == 2:
    f = sys.stdin
elif sys.argv[-1] == "-":
    f = sys.stdin
else:
    f = open(sys.argv[-1], "r")

delimiter = "\t"

if sys.argv[1].startswith("-d"):
    delimiter = sys.argv[1][2]
    field_arg = sys.argv[2]
else:
    field_arg = sys.argv[1]

fields_required = field_arg[2:].split()

try:
    for line in f:
        field = line.strip().split(delimiter)

        for i in range(len(fields_required)):
            print(field[int(fields_required[i]) - 1], end="")
            if i != len(fields_required) - 1:
                print(delimiter, end="")
        print()

finally:
    if f is not sys.stdin:
        f.close()