import sys
import bcrypt

if len(sys.argv) < 2:
    print("provide the phone number")
elif(len(sys.argv) > 2):
    print("provide the phone number alone")


if not sys.argv[1].isdigit():
    print("the number must be all digits")

