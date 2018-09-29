def func(a,b,c=1,*args,**kw):
    print "a=",a
    print "b=",b
    print "c=",c
    print "*args",args
    print "**kw",kw
    return None
func(1,2,3,4,5,6,abcd=12);
func(1,*(44,55,66),**{"haha":12,"abcd":"abcd"})


def count():
    result = []
    for x in range(3):
        def func(x):
            return lambda: x*x
        result.append(func(x))
    return result
fun1,fun2,fun3 = count()
print fun1()
print fun2()
print fun3()

