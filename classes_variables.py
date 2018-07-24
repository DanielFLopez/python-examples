print("Python classes variables inside init")
print("----------------------------------------------------------------------")


class SomeClass(object):
    def __init__(self):
        self.x = "Default value"


instance1 = SomeClass()
instance2 = SomeClass()

instance1.x = "New asigned value"

print("instance1 x-> ", instance1.x)
print("instance2 x-> ", instance2.x)

SomeClass.x = "New value for all classes"

print("instance1 x-> ", instance1.x)
print("instance2 x-> ", instance2.x)

print("Python classes variables outside init")
print("----------------------------------------------------------------------")


class SomeClassNew(object):
    x = "Default value"


instance3 = SomeClassNew()
instance4 = SomeClassNew()

instance3.x = "New asigned value"

print("instance3 x-> ", instance3.x)
print("instance4 x-> ", instance4.x)

SomeClassNew.x = "New value for all classes"

print("instance3 x-> ", instance3.x)  # Looks like scope python works
print("instance4 x-> ", instance4.x)

print("----------------------------------------------------------------------")


# Python classes variables inside init
# ----------------------------------------------------------------------
# ('instance1 x-> ', 'New asigned value')
# ('instance2 x-> ', 'Default value')
# ('instance1 x-> ', 'New asigned value')
# ('instance2 x-> ', 'Default value')
# Python classes variables outside init
# ----------------------------------------------------------------------
# ('instance3 x-> ', 'New asigned value')
# ('instance4 x-> ', 'Default value')
# ('instance3 x-> ', 'New asigned value')
# ('instance4 x-> ', 'New value for all classes')
# ----------------------------------------------------------------------