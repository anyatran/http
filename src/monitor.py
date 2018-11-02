class Monitor:
    def __init__(self):
        self.queue = []

    def add_entry(self, entry):
        self.queue.append(entry)
        print(self.queue)
