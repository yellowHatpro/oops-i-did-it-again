class Parent:
    def parent_method(self):
        print("Parent calling method")
        self.some_method()

    def some_method(self):
        print("Parent some method")


class Child(Parent):
    def some_method(self):
        print("Child some method")

    def caller(self):
        super().parent_method()

child = Child()
child.caller()
# Result:
# Parent calling method
# Child some method

