class bird:
    def __init__(self):
        print("Bird is ready!")
    def whoisthis(self):
        print("Who am i?")
    def swim(self):
        print("I can swim!")

class penguin(bird):
    def __init__(self):
       print("penguin is ready")
       super().__init__()
        
    def whoisthis(self):
        print("Who are you?")
    def run(self):
        print("I can run!")
obj = penguin()
obj.whoisthis()
obj.run()
obj.swim()
