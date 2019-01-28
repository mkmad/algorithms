"""
NOTE: You have to declare the decorators before calling/using
      them, else this won't work
"""
class TestDeco(object):
    class_var = 'test' 

    def outter(func):  # takes the func as args
        print '\noutter'
        val = None
        def inner(cls, *args,**kwargs): # takes the args of func (including cls or self)
            print 'Inner\n'
            print 'kwargs passed'
            print kwargs
            func(cls, *args, **kwargs)
            kwargs['first'] = '3'
            print '\nkwargs modified'
            print kwargs 
            val = func(cls, *args, **kwargs)
            print 'value from my_func'
            print val
            cls.class_var = 'changed'
            return 'Signing off'
        return inner
        print 'this statement is out of scope'
    
    @classmethod   
    @outter
    def my_func(cls, first=None, second=None):
        print 'my_func\n'
        print first
        print second
        print cls.class_var
        return 'wadup'


    def outter_with_args(test=None):
        print 'outter\n'
        def inner(func):
            print 'inner\n'
            def sub_inner(cls, *args, **kwargs):
                print 'sub inner\n'
                kwargs['first'] = 'Mohan'
                kwargs['second'] = 'Madhavan'
                val = func(cls, *args, **kwargs)
                print 'value from func'
                print val
                return val
            return sub_inner
        print '\noutter arg'
        print test
        return inner

    @classmethod
    @outter_with_args(test='heyaa')
    def my_sec_func(cls, first=None, second=None):
        print first
        print second
        return 'well'

    @property
    def get_deco_val(self):
        return self.my_sec_func()
                
    @property
    def get_class_var(self):
        return self.my_func()
    
    def main(self):
        print 'class_var'
        print self.class_var
        val = self.my_func(first='1', second='2')
        print '\nclass_var_after'
        print self.class_var
        print '\nValue from inner'
        print val
        print 'calling property decorator'
        print '*'*80
        val_ = self.get_class_var
        print '*'*80
        print val_
        print 'calling second func property decorator'
        print '*'*80
        print self.get_deco_val
        print '*'*80

if __name__ == '__main__':
    t = TestDeco()
    t.main()
        
        
