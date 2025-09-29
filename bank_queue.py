
class Queue():
    def __init__(self):
        self.customers = []
        self.turn = 0
        
    def isempty(self):
        if len(self.customers) == 0:
            print("Empty queue")
            return True
        
    def add_custumer(self):
        self.turn += 1
        self.customers.append(self.turn)

    def attend_custumer(self):
        if not self.isempty():
            print(f"Next turn {self.customers[0]}")
            self.customers.pop(0)

    def show_custumers(self):
        if not self.isempty():
            print(f"All custumers: {self.customers}")

#Test
c = Queue()

c.add_custumer()
c.add_custumer()
c.add_custumer()
c.show_custumers()
c.attend_custumer()
c.attend_custumer()
c.show_custumers()
c.add_custumer()
c.add_custumer()
c.show_custumers()
c.attend_custumer()
c.attend_custumer()
c.attend_custumer()
c.attend_custumer()