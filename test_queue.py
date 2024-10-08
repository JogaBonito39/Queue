#Queue
#FIFO
#customers in line for the grocery store
#the first customer in the checkout line is the first customer out of the checkout line

class Queue():
    def __init__(self):
        self.queue_elements = []
        
    def add(self, data):
        self.queue_elements.append(data)
        
    def remove(self):
        #[1,2,3,4,5] -> removes 1 then 2 then 3 then ... etc.
        #etcetera
        return self.queue_elements.pop(0)
        
    def __repr__(self):
        return f"queue: {self.queue_elements}"
 

def automated_queue_add(num_range):
    for i in range(0,num_range):
        q.add(i)
    print(q.queue_elements)
    
def automated_queue_remove(amount):
    count = 0
    while count != amount:
        print(f"removed elements: {q.remove()}")
        count+=1    
    print(q.queue_elements)
    
    
if __name__ == "__main__":
    q = Queue()
    #q.add(1)
    #q.add(2)
    #q.add(3)
    #q.add(4)
    #q.add(5)
    #q.add(6)
    #q.add(7)
    #q.add(8)
    #q.add(9)
    #q.add(10)
    automated_queue_add(11)
    automated_queue_remove(5)
    #print(q)
    #print(f"value removed: {q.remove()}")
    #print("value removed: {}".format(q.remove()))
    #print(q)
    
#Complete