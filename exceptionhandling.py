try:
    f=open("elif.py","w")
    f.write("#this file is used in as an example of exception handling")
# except IOError:
#  print("file cannot found")
# else:
#  print("content uploaded successfull")
# f.close()
finally:
    print("error cannot find in data")
    f.close()