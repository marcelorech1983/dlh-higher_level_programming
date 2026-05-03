#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False
