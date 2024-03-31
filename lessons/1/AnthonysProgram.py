#!/usr/bin/python3
import sys


def main():
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    c = a + b
    d = a - b
    
    print(f"{a} + {b} = {c}")
    print(f"{a} - {b} = {d}")


if __name__ == "__main__":
    main()