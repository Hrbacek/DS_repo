"""Solucion base para string madness
"""

from Estructuras.LinkedList import LinkedList
from Estructuras.Queue import Queue

def last_post_remaining(posts_list: LinkedList, operations_list: Queue) -> str:

    for _ in range(operations_list.size):
        current_op =  operations_list.peek()
        a, b = current_op

        node_a = posts_list._get_node(a-1)
        node_b = posts_list._get_node(b-1)

        node_a.data += node_b.data

        node_b.data = ""
        operations_list.dequeue()

    result = ""
    for i in range(posts_list.size):
        result = posts_list.get(i)
        if result != "":
            return result

    return result


def main():
    posts = ["cute", "cat", "cool", "is"]
    operations = [(3, 2), (4, 1), (3,4)]
    
    posts_list = LinkedList()
    for post in posts:
        posts_list.add(post)

    operations_list = Queue()
    for operation in operations:
        operations_list.enqueue(operation)

    result = last_post_remaining(posts_list, operations_list)
    print(result)

if __name__ == "__main__":
    main()