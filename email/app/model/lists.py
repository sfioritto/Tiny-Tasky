import json
import pytyrant
from hashlib import sha1
from webapp.lists.models import List

lists = pytyrant.PyTyrant.open('127.0.0.1', 1978)


class ListWrapper:

    def __init__(self, data, account):
        self.data = data
        self.name = data['name']
        self.account = account
        self.key = data['key']
        self.tasks = data['tasks']


    def save(self):
        lists[self.key] = json.dumps(self.data)
        

    def add_task(self, text):
        
        task = {
            'text' : text,
            'complete' : False,
            'id' : create_task_id(text, self.account)}
        
        self.tasks.append(task)
        self.save()

        
    
def make_key(name, id):
    
    return sha1(name + "@" + str(id)).hexdigest()
    

def create(name, account):

    """
    Create a list if it doesn't exist and return
    it. Otherwise, return the list that exists.
    
    Returns a ListWrapper instance.
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
        return ListWrapper(lists[key], account)


def get_list(name, account):
    
    """
    Returns a ListWrapper object instantiated
    with data from the datastore.
    """

    try:
        lst = json.loads(lists[make_key(name, account.id)])
        return ListWrapper(lst, account)
    except KeyError:
        return None


def create_task_id(text, account):
    return sha1(text + ":" + account.email).hexdigest()




