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
    print "\nShowing dict of t and b (only instance variable is shown)"
    print '\nt\'s Dict: {0}'.format(t.__dict__)
    print 'b\'s Dict: {0}\n'.format(t.__dict__)

    # To show that changing class var in
    # different instance will not
    # impact the other instance
    print 'Before\n'
    print "t's vars"
    t.printvars()
    print "b's vars"
    b.printvars()

    print "changinh b.class_var to 3"
    b.class_var = 3

    print 'After\n'
    print "t's vars"
    t.printvars()
    print "b's vars"
    b.printvars()

    # This is to show class var can be
    # accessed without instantiating
    print 'Without Instatiating'
    print test.class_var

    # This is to show how objects behave
    # when class variable are changed
    # outside the class.
    print '\nShowing the difference when messing with class vars,'
    print "setting class var to 4 without instantiating\n"
    test.class_var = 4
    print "t's vars"
    t.printvars()
    print "b's vars"
    b.printvars()  # This won't change because we set b.class_var
    print "Note how b's vars did not change because b.class_var\n" \
          "was set earlier and now that resides in the b object"

    # Seting t's class var this time
    print '\nSetting t\'s var'
    t.class_var = 5
    t.printvars()
    b.printvars()

    # To show that class vars default values is changed completely
    print '\nTo show that class vars default value is changed completely'
    f = test()
    f.printvars()
    print test.class_var

    # Printing f, b and t
    print '\nPrinting vars f, b and t'
    f.printvars()
    b.printvars()
    t.printvars()

    print '\nTo conclude, the class vars stays in the class\'s address space ' \
          'unless \nand until its set by the particular instance. Then its ' \
          'copied over to\nthe instance\'s address space'
