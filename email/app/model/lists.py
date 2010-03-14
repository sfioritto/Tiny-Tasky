import json
import pytyrant
from hashlib import sha1
from webapp.lists.models import List

lists = pytyrant.PyTyrant.open('127.0.0.1', 1978)


def make_key(name, unique):
    
    return sha1(name + "@" + str(unique)).hexdigest()
    

def create(name, account, value=[]):

    """
    Create a list if it doesn't exist and return
    it. Otherwise, return the list that exists.
    """
    
    lst = get_list(name, account.id)
    if lst:
        return lst
    else:
        key = make_key(name, account.id)
        lists[key] = json.dumps(value)
        newlist = List(name=name, account=account)
        newlist.save()
        return lists[key]


def get_list(name, unique):
    
    try:
        lst = json.loads(lists[make_key(name, unique)])
    except KeyError:
        lst = None

    return lst
