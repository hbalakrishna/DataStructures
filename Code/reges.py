
import re
import datetime
from datetime import datetime
import time

ip = '2016-02-12T03:22:03Z    Program x did operation y successfully.'
print(ip[:20])
re.compile('^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z+')

regex = r"^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z+"
match = re.search(regex, "2016-02-12T03:22:03Z    Program x did operation y successfully")
match_1 = re.search(regex, "2016-02-12T03:21:54Z    Program x did operation y successfully.")
testing_time = re.search(regex, "")


# print("Full match: %s" % (match.group(0)))
try:
    a = (match.group(0))
    b = (match_1.group(0))
    x = (testing_time.group(0))


    t2 = time.strptime(a[:19], "%Y-%m-%dT%H:%M:%S")
    t1 = time.strptime(b[:19], "%Y-%m-%dT%H:%M:%S")
    test_time = time.strptime(x[:19], "%Y-%m-%dT%H:%M:%S")


    if test_time>t1 and test_time<t2:
        print("format", time.strftime("%m/%d/%Y %H:%M:%S", test_time), "lies between t1", time.strftime("%m/%d/%Y %H:%M:%S", t1)
              , "and", time.strftime("%m/%d/%Y %H:%M:%S", t2)
              )
    else:
        print("out of range")

    print(time.strftime("%m/%d/%Y %H:%M:%S", t1))
    print(time.strftime("%m/%d/%Y %H:%M:%S", t2))
    print(time.strftime("%m/%d/%Y %H:%M:%S", test_time))
except Exception:
    print("Caught Error")




