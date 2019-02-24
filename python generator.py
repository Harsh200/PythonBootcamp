def gen():
    n=1
    print("this is printed first")
    yield n

    n+=1
    print("this is printed second")
    yield n

    n+=1
    print("this is printed last")
    yield n
