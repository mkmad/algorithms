class test(object):

    class_var = 1

    def __init__(self):
        self.instance_var = 2

    def printvars(self):
        print ''
        print self.class_var
        print self.instance_var
        print ''


if __name__ == '__main__':
    t = test()
    b = test()
    # printing dict, this will
    # print only the instance var
    print '\nDict: {0}\n'.format(t.__dict__)

    # To show that changing class var in
    # different instance will not
    # impact the other instance
    print 'Before'
    t.printvars()
    b.printvars()
    b.class_var = 3
    print 'After'
    t.printvars()
    b.printvars()

    # This is to show class var can be
    # accessed without instantiating
    print 'Without Instatiating'
    print test.class_var

    # This is to show how objects behave
    # when class variable are changed
    # outside the class.
    print '\nShowing the difference when messing with class vars'
    test.class_var = 4
    print t.printvars()
    print b.printvars()  # This won't change because we set b.class_var

    # Seting t's class var this time
    print '\nSetting t\'s var'
    t.class_var = 5
    print t.printvars()
    print b.printvars()

    # To show that class vars default values is changed completely
    print '\nTo show that class vars default value is changed completely'
    f = test()
    print f.printvars()
    print test.class_var

    # Printing f, b and t
    print '\nPrinting vars f, b and t'
    print f.printvars()
    print b.printvars()
    print t.printvars()

    print '\nTo conclude, the class vars stays in the class\'s address space ' \
          'unless and until its set by the particular instance. Then its ' \
          'copied over to the instance\'s address space'
