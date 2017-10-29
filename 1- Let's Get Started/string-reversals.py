"""String reversals."""
import sys


def string_reversal(s):
    """Return inverse of string given."""
    inverse_list = []
    print(" ".join(s))
    split_list = list(s)
    print(split_list)
    for index in range(0, len(split_list)):
        inverse_list.append(split_list[index * -1])
    # print("".join(inverse_list))


string_reversal(sys.argv[1:])
