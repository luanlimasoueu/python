class Foo(object):
    def __init__(self):
        self.__bar = None
    @property
    def bar(self):
        if self.__bar is None:
            self.__bar = some_expensive_lookup_operation()
        return self.__bar