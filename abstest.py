def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x
    
def my_sum(x):
    mid=0
    for i in range(0,x):
        mid+=i
    return mid