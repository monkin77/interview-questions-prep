# Enter your code here. Read input from STDIN. Print output to STDOUT

class Queue():
    def __init__(self):
        # Stack for enqueue. Stores elements in the order they are enqueued.
        # Since stacks are LIFO, we need an auxiliary stack to reverse the order of elements and dequeue them in FIFO order.
        self.s1 = []

        # Auxiliary stack for dequeue. Reverses the order of elements in s1, making the pop operation in s2 a FIFO operation.
        # Elements in s2 are stored in reverse order [nth, (n-1)th, ..., 2nd, 1st], so we can pop the first element in O(1) time. 
        self.s2 = []    # Stack for dequeue. Inver

    def enqueue(self, elem):
        self.s1.append(elem)

    def dequeue(self):
        # If s2 is empty, let's invert the order of elements in s1.
        # to pop the next element.
        # if s2 is not empty, we don't need to move elements from s1 to s2 for now.
        if len(self.s2) == 0:
            # Move all elements from s1 to s2.
            while len(self.s1) > 0:
                self.s2.append(self.s1.pop())
        
        return self.s2.pop()
    
    def print(self):
        # Same as dequeue, but we don't remove the element from s2.
        if len(self.s2) == 0:
            # Move all elements from s1 to s2.
            while len(self.s1) > 0:
                self.s2.append(self.s1.pop())
        
        print(self.s2[-1])

        



num_queries = int(input())

for query_idx in range(num_queries):
    query = input().split(" ")  # Read string from stdin and split it into a list of strings. Stops when a '\n' is encountered.
    # print(f"query: {query}")

    query_type = int(query[0])   # 1: enqueue, 2: dequeue, 3: print

    if query_type == 1:
        # Enqueue (Push element to the end of the queue)
        elem = int(query[1])


