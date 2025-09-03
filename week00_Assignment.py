class MinHeap:
    def __init__(self, max_size: int = 100):
        self.heap_array = [None] * max_size
        self.element_counter = 0
        self.max_size = max_size

    def size(self) -> int:
        return self.element_counter
    
    def is_empty(self) -> bool:
        return self.element_counter == 0
    
    def display(self) -> str:
        if self.is_empty():
            return "Empty heap"
        elements = []
        for i in range(self.element_counter):
            elements.append(str(self.heap_array[i]))
        return f"Heap: [{', '.join(elements)}]"    


# Tests:

print("1) Create new heap")
heap = MinHeap(10)
print(f"created heap w max size 10")

print("\n2) Check initial state")
print(f"size: {heap.size()}")
print(f"is empty: {heap.is_empty()}")
print(f"display: {heap.display()}")

print("\n3) Another Heap")
heap = MinHeap(5)
print(f"heap w max size 5")

        
        