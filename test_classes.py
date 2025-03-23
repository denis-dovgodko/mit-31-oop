from metaclass import CacheMeta

class Test(metaclass=CacheMeta):
    def compute(self, x, y):
        print(f"x: {x}, y: {y}. Calculating x+y ...")
        return x + y
    def compute2(self, x, y):
        print(f"x: {x}, y: {y}. Calculating x^y ...")
        return x ^ y
    
class Test2(metaclass=CacheMeta):
    def compute(self, x, y):
        print(f"x: {x}, y: {y}. Calculating x-y ...")
        return x - y