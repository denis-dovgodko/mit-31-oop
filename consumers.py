import collections.abc

class Consumers(collections.abc.MutableSequence):
    def __init__(self):
        self.__consumers = []

    def __len__(self):
        return len(self.__consumers)

    def append(self, consumer):
        self.__consumers.append(consumer)

    def insert(self, consumer):
        self.__consumers.insert(consumer)

    def __setitem__(self, consumer):
        self.__consumers[self.__consumers.index(consumer)] = consumer

    def __delitem__(self, consumer):
        del self.__consumers[self.__consumers.index(consumer)]

    def __getitem__(self, consumer):
        if consumer in self.__consumers:
            return self.__consumers[self.__consumers.index(consumer)]
        
    def __iter__(self):
        return iter(self.__consumers)