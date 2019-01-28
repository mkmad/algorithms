class test(object):
   
    # Testing static variables
    _myStaticvar = 'I am awesome'
    _mysecvar = 'way to go'
    def __init__(self, fname, lname):

        self.fname = fname
        self.lname = lname
        # Private to class, but will be revealed in class.__dir__
        # For this eample to work this has to be a private variable.
        self._email = None
        # Private to __init__ method
        fname = fname
    # Whenever we assign or retrieve any object attribute like fname, 
    # as show above, Python searches it in the object's __dict__ dictionary.
    # Therefore, test.fname internally becomes test.__dict__['fname'].

    @property
    def email(self):
        # Getter for self._email. Note how the name is same as the attribute
        # So, when email is called the interpreter is tricked to call this 
        # property method. Unless a setter is defined self._email cannot
        # be set.
        try:
            if not self._email:
                self._email = self.fname+'.'+self.lname+'@gmail.com'
            return self._email
        except Exception as e:
            print e


    @email.setter
    def email(self, value):
        # If commented, there is no way to set email, lol ;)
        self._email = value

    @email.deleter
    def email(self):
        self._email = None

    @property
    def myStaticvar(self):
        # Note how you call the static var
        # Either this or test._myStaticvar
        return type(self)._myStaticvar

    @myStaticvar.setter
    def myStaticvar(self, val):
        type(self)._myStaticvar = val

if __name__ == '__main__':

    print ''
    tt = test('Mohan', 'Madhavan')
    print('Calling email with Mohan and Madhavan')
    print(tt.__dict__)
    print(tt.email)
    
    print ''
    print('Setting fname to MKM')
    tt.fname = 'MKM'
    print(tt.__dict__)
    # Notice how you can call the property as an attribute
    print('Calling email with MKM Madhavan')
    print(tt.email)
    print('Note the difference in __dict__ value')
    print('Email gets reset after the variable is called')
    print(tt.__dict__)

    try:
        # uncomment setter first
        print ''
        print('Setting email to some.email.com')
        tt.email = 'some.email.com'
        print(tt.__dict__)
        print('trying email with new value')
        print(tt.email)
        print('Now trying to set the fname and calling email again.')
        tt.fname = 'test'
        print(tt.email)
        print('It fails due to the condition in ln 27')
    except Exception as e:
        print e.message

    # This will call the deleter property
    try:
        print ''
        print('Calling the deleter property')        
        del tt.email
        print(tt.__dict__)
    except Exception as e:
        print e.message

    f_t = test('f', 'l')
    print(f_t._myStaticvar)
    s_t = test('f', 'l')
    print(s_t._myStaticvar)
    f_t.myStaticvar = 'Oh yes I am'
    print(f_t.myStaticvar)
    print(s_t.myStaticvar)
    print('Note how the static var changed for s_t as well, this works only if you call the property')
    f_t._myStaticvar = 'oh no'
    print(f_t.myStaticvar)
    print(f_t._myStaticvar)
    print('This fails when we set the static var directly, even for the same instance variable!!!!!')
    print('To illustrate this, when we set the var using the decoraters. It changes the value at the class level and not the instance level, as shown below')
    print(f_t.__class__._myStaticvar)

    print('taking that concept further')
    print(f_t._mysecvar)
    print(s_t._mysecvar)
    f_t.__class__._mysecvar = 'change is good'
    f_t._mysecvar = 'This should not change s_t value'
    print(s_t._mysecvar)
    print('So true way to set the static var is obj.__class__.var')
    print('In conclusion obj.__class__ is type(obj)')

