"""Solucion base para ...
"""

from Estructuras.Queue import Queue
from Estructuras.LinkedList import LinkedList

def bug_plannig_seq(queue: Queue):
    output = LinkedList()
    max_value = queue.peek()
    output.add(max_value)

    for _ in range(queue.size):
        next_value = queue.dequeue()
        if next_value > max_value:
            output.add(next_value)
            max_value = next_value
    
    return output

def main():
    queue = Queue()
    queue.enqueue(5)
    queue.enqueue(4)
    queue.enqueue(3)
    queue.enqueue(2)
    queue.enqueue(1)

    output = bug_plannig_seq(queue)
    output.print_list()

if __name__ == "__main__":
    main()