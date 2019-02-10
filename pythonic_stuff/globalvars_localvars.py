"""

This is to show that global vars can just be used for printing
and accessing their value (i.e. read only) and can not be used for 
modifying their value. If you want to modify then you need to use 
global key word in the function's address space

"""

MY_GLOBAL = 5


# Here MY_GLOBAL is treated as a local var
def func1():
    MY_GLOBAL = 42
    print MY_GLOBAL


# MY_GLOBAL just used for printing
def func2():
    print MY_GLOBAL


# Accessing the value of MY_GLOBAL
def func3():
    myLocal = MY_GLOBAL
    print myLocal
    myLocal += 1
    print myLocal


# Trying to modify MY_GLOBAL (results in error)
def func4():
    try:
        MY_GLOBAL += 1
        print MY_GLOBAL
    except Exception as e:
        print e.message


# Modifying MY_GLOBAL after using the global keyword
def func5():
    global MY_GLOBAL
    MY_GLOBAL += 1
    print MY_GLOBAL


if __name__ == '__main__':
    print
    func1()
    print
    func2()
    print
    func3()
    print
    func4()
    print
    func5()


