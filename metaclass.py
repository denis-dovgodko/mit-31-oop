

class CacheMeta(type):
    def __new__(cls, clsname, bases, dct):
        methods_dict = {name: cls.caching(value) for name, value in dct.items() if not name.startswith('__') and callable(value)}
        base_dict = {name: value for name, value in dct.items() if name.startswith('__') or not callable(value)}
        base_dict.update(methods_dict)
        return super(CacheMeta, cls).__new__(cls, clsname, bases, base_dict)

    @staticmethod
    def caching(func):
        def cache_processing(self, *args, **kwargs):
            if not hasattr(self, '_cache'):
                self._cache = {}
            key = (args, frozenset(kwargs.items()))
            if key not in self._cache:
                self._cache[key] = func(self, *args, **kwargs)
            return self._cache[key]
        return cache_processing