class QueueList:
    def __init__(self):
        self.items = []

    def enqueue(self, data):
        self.items.insert(0, data)

    def dequeue(self):
        if len(self.items) > 0:
            item = self.items.pop(0)
            return item
        else:
            print("The queue is empty.")
            return None

    def print_queue(self):
        if len(self.items) > 0:
            for item in self.items:
                print(item)
        else:
            print("The queue is empty")

    def empty_queue(self):
        self.items = []

    def size(self):
        return len(self.items)

# ql = QueueList()
# ql.enqueue("1")
# ql.enqueue("2")
# ql.enqueue("3")
# ql.enqueue("4")
# ql.enqueue("5")
# ql.enqueue("6")
# ql.enqueue("7")
# ql.enqueue("8")
# ql.enqueue("9")
# ql.enqueue("10")
# print(ql.size())
#ql.print_queue()
