# sum_integers_args.py
def my_sum(*args):
    result = 0
    # Iterating over the Python args tuple
    for x in args:
        result += x
    return result

# passing three different positional argument
print(my_sum(1, 2, 3))