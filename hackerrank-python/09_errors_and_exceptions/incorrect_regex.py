import re

for _ in range (int(input())):
    string = raw_input()

    try :
        re.compile(string)
        print "True"
    except  re.error :
        print "False"
        

