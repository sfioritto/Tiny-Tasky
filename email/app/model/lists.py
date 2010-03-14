import json
import pytyrant
from hashlib import sha1
from webapp.lists.models import List

lists = pytyrant.PyTyrant.open('127.0.0.1', 1978)


def make_key(name, id):
    
    return sha1(name + "@" + str(id)).hexdigest()
    

def create(name, account):

    """
    Create a list if it doesn't exist and return
    it. Otherwise, return the list that exists.
    """
    
    lst = get_list(name, account.id)
    if lst:
        return lst
    else:
        key = make_key(name, account.id)
        lists[key] = json.dumps({'name' : name,
                                 'key' : key,
                                 'tasks' : []})
        newlist = List(name=name, account=account)
        newlist.save()
        return lists[key]


def get_list(name, id):
    
    try:
        lst = json.loads(lists[make_key(name, id)])
    except KeyError:
        lst = None

    return lst


def add_task(lst, task):
    
    lst['tasks'].append(task)
    update_list(lst)


def update_list(lst):

    lists[lst['key']] = json.dumps(lst)
