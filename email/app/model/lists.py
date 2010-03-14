import json
import pytyrant
from hashlib import sha1

lists = pytyrant.PyTyrant.open('127.0.0.1', 1978)


def make_key(name, unique):
    
    return sha1(name + str(unique)).hexdigest()
    

def create(name, unique, value=[]):

    """
    Create a list if it doesn't exist and return
    it. Otherwise, return the list that exists.
    """
    
    lst = get_list(name, unique)
    if lst:
        return lst
    else:
        key = make_key(name, unique)
        lists[key] = json.dumps(value)
        return lists[key]


def get_list(name, unique):
    
    try:
        lst = json.loads(lists[make_key(name, unique)])
    except KeyError:
        lst = None

    return lst
