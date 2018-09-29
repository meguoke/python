
def testrange():
    print "generate the list from the range "
    list1 = [x * x for x in range(0, 10)]
    print list1
    print "generate the list from the map "
    mapList = [x+k for x,k in {1:2,3:1}.iteritems()]
    print mapList
    print "generete the list from the nest loop"
    nestLoopList = [m+n for m in "ABC" for n in "123" if n=="1"]
    print nestLoopList
    lowerCase = ["Abcd","DGET",12]
    print [s.lower() for s in lowerCase if isinstance(s,str)]
if __name__ == "__main__":
    testrange()
