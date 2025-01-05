class Queue:
    def __init__(self):
        self.queue = []
        start_queue()


    def enqueue(self):
        self.queue.append(int(input("Enter the element to remove.")))


    def dequeue(self):
        self.queue.pop(0)


    def front(self):
        print(self.queue[0])

    def rear(self):
        print(self.queue[-1])

    def display(self):
        print(self.queue)


    def start_queue( ):
        while True:
            n = input("What operation would you like to do: ").lower().strip()
            match n:
                case "front":
                    front()
                
                case "display":
                    display()
                
                case "rear":
                    rear()

                case "enqueue":
                    enqueue()
                
                case "dequeue":
                    dequeue()

                case "quit":
                    break

                case _:
                    continue

my_queue = Queue