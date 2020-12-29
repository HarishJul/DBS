from collections import OrderedDict

class Redis:
 
    def __init__(self, size):
        self.cache = OrderedDict()
        self.size = size
    
    def get(self, key):
        if key not in self.cache:
            return -1
        else:
            self.cache.move_to_end(key)
            return self.cache[key]
     
    def set(self, key, value):
        self.cache[key] = value
        self.cache.move_to_end(key)
        if len(self.cache) > self.size:
            self.cache.popitem(last = False)
    
    def delete(self,key):
        if key in self.cache:
            del self.cache[key]
            return 1
        return 0
    
    def flush(self):
        dict_len = len(self.cache)
        self.cache.clear()
        return dict_len

##Example
r = Redis(10)
r.set('a',1)
r.set('b',2)
r.set('c',3)
r.set('d',4)
r.set('e',5)
r.set('f',6)
r.get('c')
r.delete('c')
r.flush()