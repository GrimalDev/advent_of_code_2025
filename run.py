#!/usr/bin/env python3
"""
Advent of Code runner script
Usage: python run.py <day_number>
"""

import sys
import os
import importlib.util

# Import all the math/algorithm libraries like in LeetCode
import math
import itertools
import functools
import operator
import collections
from collections import defaultdict, Counter, deque, namedtuple, OrderedDict
import heapq
import bisect
import string
import re
from typing import List, Dict, Set, Tuple, Optional, Any, Union
from itertools import (
    permutations,
    combinations,
    product,
    combinations_with_replacement,
    accumulate,
    chain,
    compress,
    cycle,
    dropwhile,
    filterfalse,
    groupby,
    islice,
    starmap,
    takewhile,
    tee,
    zip_longest,
)
from functools import lru_cache, reduce, partial, wraps
from operator import add, mul, itemgetter, attrgetter, methodcaller
import copy
from decimal import Decimal, getcontext
from fractions import Fraction
import array
import statistics
from math import (
    ceil,
    floor,
    sqrt,
    pow,
    log,
    log10,
    log2,
    exp,
    sin,
    cos,
    tan,
    asin,
    acos,
    atan,
    atan2,
    degrees,
    radians,
    pi,
    e,
    inf,
    nan,
    gcd,
    factorial,
    comb,
    perm,
    isqrt,
    lcm,
)


def main():
    if len(sys.argv) != 2:
        print("Usage: python run.py <day_number>")
        sys.exit(1)

    try:
        day = int(sys.argv[1])
    except ValueError:
        print("Error: Day number must be an integer")
        sys.exit(1)

    day_dir = f"day{day}"

    if not os.path.isdir(day_dir):
        print(f"Error: Directory '{day_dir}' does not exist")
        sys.exit(1)

    solution_file = os.path.join(day_dir, "mai.py")

    if not os.path.isfile(solution_file):
        print(f"Error: '{solution_file}' does not exist")
        sys.exit(1)

    # Import and run the solution module
    spec = importlib.util.spec_from_file_location(f"day{day}.solution", solution_file)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    # Check if the module has a main function and run it
    if hasattr(module, "main"):
        module.main()
    else:
        print(f"Warning: No main() function found in {solution_file}")


if __name__ == "__main__":
    main()
