"""Solucion base para classical jump problem
"""
from Estructuras.LinkedList import LinkedList

def classical_jump_seq(seq: LinkedList):
    diff_seq = LinkedList()

    for i in range(seq.size-1):
        print(seq.get(i), seq.get(i+1))
        diff_seq.add(
            abs(seq.get(i)-seq.get(i+1))
        )

    for i in range(1, seq.size):
        if diff_seq.search(i) == -1:
            return "Not jolly"

    return "Jolly"

def main():
    seq_1 = LinkedList()
    seq_1.add(10)
    seq_1.add(13)
    seq_1.add(11)
    seq_1.add(8)
    seq_1.add(16)
    print(classical_jump_seq(seq_1))

if __name__ == "__main__":
    main()