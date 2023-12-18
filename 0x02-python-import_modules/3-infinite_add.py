#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    sum = 0
    num_args = len(sys.argv) - 1
    for i in range(num_args):
        sum += int(sys.argv[i + 1])
    print(sum)
