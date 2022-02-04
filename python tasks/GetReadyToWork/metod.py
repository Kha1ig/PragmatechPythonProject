class MyClass:
    property1 = [1, 2, 3]
 
    def __init__(self, a):
        assert isinstance(a, float) or isinstance(a, int)
        self.state = a
 
    def add(self, a):
        assert isinstance(a, float) or isinstance(a, int)
        self.state = self.state + a
        return self.state
 
    def subtract(self, a):
        assert isinstance(a, float) or isinstance(a, int)
        self.state = self.state - a
        return self.state
 
    def multiply(self, a):
        assert isinstance(a, float) or isinstance(a, int)
        self.state = self.state * a
        return self.state
 
    def divide(self, a):
        assert isinstance(a, float) or isinstance(a, int)
        self.state = self.state / a
        return self.state
 
 
    @staticmethod
    def global_method(a, b):
        return a + b
 
    @classmethod
    def myclass_method(cls):
        return cls
 
method_list = [method for method in dir(MyClass) if method.startswith('_') is False]
print(method_list)