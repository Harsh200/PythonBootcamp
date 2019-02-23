class bird:
    def __init__(self):
        print("Bird is ready")

    def whoisthis(self):
            print("bird")

    def swim(self):
                print("swim faster")


class pigeon(bird):
    def __init__(self):
        super().__init__()
        print("pigeon is ready")

    def whoisthis(self):
            print("pigeon")

    def run(self):
                print("run faster")



