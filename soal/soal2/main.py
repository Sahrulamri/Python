class MyClass:
    variable = 10

    def func(self, value):
        self.variable *= value

obj = MyClass()
obj.func(5)
print(obj.variable)


# my_dict = {"a": 1, "b": 2, "c": 3}