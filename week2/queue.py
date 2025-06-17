class Queue:
    def __init__(self) -> None:
       #we use a list to sotre the queue elements
       self.data  = []

    def enqueue(self, element):
        #append element to the end of the queue
        self.data.append(element)

    def dequeue(self):
        #remove and return the first element in the queue 
        if self.data:
            return self.data.pop(0)
        
        return None  #raise an exception if you prefer
    
    def read(self):
        #return the first element without removing it
        if not self.data:
            return None
        return self.data[0]


class PrintManager:
    def __init__(self) -> None:
        self.queue = Queue()

    def queue_print_job(self, document):
        self.queue.enqueue(document)

    def run(self):
        while self.queue.read():
            self._print(self.queue.dequeue())

    def _print(self, document):
        #simulates printing to a terminal
        print(document)


pm = PrintManager()
pm.queue_print_job("Document 1")
pm.queue_print_job("Document 2")
pm.queue_print_job("Document 3")

pm.run()
