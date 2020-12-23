class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity=capacity
        self.d=collections.OrderedDict()

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.d.keys():
            s=(key,self.d[key])
            self.d.pop(key)
            t=list(self.d.items())
            t.append(s)
            self.d=collections.OrderedDict(t)
            # print(self.d)
            return self.d[key]
        else:
            return -1


    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if len(self.d)==0:
            self.d[key]=value
        elif len(self.d)<self.capacity and key not in self.d.keys():
            temp=list(self.d.items())
            temp.append((key,value))
            self.d=collections.OrderedDict(temp)
        elif len(self.d)<=self.capacity and key in self.d.keys():
            self.d.pop(key)
            s=(key,value)
            t=list(self.d.items())
            t.append(s)
            self.d=collections.OrderedDict(t)
        else:
            t=list(self.d.items())
            t.pop(0)
            t.append((key,value))
            self.d=collections.OrderedDict(t)
