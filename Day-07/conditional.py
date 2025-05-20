import sys


type = sys.argv[1]

if type == "micro":
    print("You will be charged 2$ everyday")
elif type == "big":
    print("You will charged 5$ everyday")
else:
    print("You cannot create an ec2 instance")