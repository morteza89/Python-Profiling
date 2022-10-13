'''
In this script we are going to see how well the python code is working based on time and memory
to do so we use profiling and optimization
we will use the cProfile module for time profiling and memory_profiler for profiling memory usege of each funtion
For memory profiling we use the memory_profiler module so:
we install it with:  pip install memory_profiler

Author: Morteza Heidari
Made in: 10/13/2022

'''
import cProfile
import pstats
import io
from memory_profiler import profile
import numpy as np
####

# -------------------------------------------------------------------------
# the function below is used for time profiling, all you need to do is put it on top of the main function you want to profile
# and it returns the time the function and all the subfunctions took to execute
# -------------------------------------------------------------------------
# it has a decorator @time_profiling that takes another function as an argument


def time_profiling(fnc):
    """A decorator that uses cProfile to profile a function"""

    def inner(*args, **kwargs):

        pr = cProfile.Profile()  # in that we start the profiler
        pr.enable()
        retval = fnc(*args, **kwargs)  # we execute the function
        pr.disable()  # then we stop the profiler
        s = io.StringIO()  # we create a string buffer
        sortby = 'cumulative'
        ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
        ps.print_stats()
        print(s.getvalue())  # we print the result
        return retval  # we return the result of the function

    return inner
# -------------------------------------------------------------------------

# make a couple of examples to see how it works


@time_profiling  # this is for profiling the code and see how much time it takes to execute
@profile  # this is for profiling the memory usege of the function
def example1():
    """This function is an example of a function that is not optimized"""
    a = [i**2 for i in range(10000)]
    # first define a numpy array of 10000  zero elements as b
    b = np.zeros(10000)
    for i in range(10000):
        b[i] = i ** 2
    j = 0
    for i in range(1000):
        j = j + i
    m = example2()
    d = example3()
    return i, m


@profile
def example2():
    """This function is an example of a function that is optimized"""
    m = 0
    n = 1468.4345
    for i in range(1000):
        for j in range(1000):
            m += i * j
    m = m + n
    q = m / 10
    s = m * 10000
    return m


@profile
def example3():
    """  we define a dictionary that contains the numbers from 0 to 9 as keys and the number of times they occur as values"""
    d = {i: 0 for i in range(10)}
    for i in range(10000):
        d[i % 10] += 12313453.5677643
    # s = d * 2
    return d

#  now we are going to do memory profiling
#  we will use the memory_profiler module


#
if __name__ == '__main__':
    # find_duplicate_movies()
    example1()
