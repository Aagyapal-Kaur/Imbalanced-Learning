from copy import copy
from collections import Counter
import warnings
warnings.filterwarnings('once')

def key_with_max_val(d):
    """ a) create a list of the dict's keys and values;
        b) return the key with the max value"""

    if isinstance(d,Counter) :
        d = dict(d)

    v=list(d.values())
    k=list(d.keys())
    return k[v.index(max(v))]

def key_with_min_val(d):
    """ a) create a list of the dict's keys and values;
        b) return the key with the min value"""

    if isinstance(d,Counter) :
        d = dict(d)

    v=list(d.values())
    k=list(d.keys())
    return k[v.index(min(v))]

def dictionary_probability_query(d, key):
    try:
        return d[key]
    except:
        return 0


def get_minority_class(y):
    counts = Counter(y)
    return key_with_min_val(counts)

def get_majority_class(y):
    counts = Counter(y)
    return key_with_max_val(counts)

def round_array(l,num_digits = 4):
    """
    Danger Danger, this method mutates the given list.
    # Keyword arguments:
    - l : A list of floats
    - num_digits the number of digits to round the elements too
    """
    for i in range(len(l)):
        l[i] = round(l[i],num_digits)
    return l
