usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        odd = 0
        for j in range(x):
            if isinstance(my_list[j], int):
                print("{:d}".format(my_list[j]), end="")
                odd += 1
        print()
        return odd
    except IndexError:
        print()
        return odd
