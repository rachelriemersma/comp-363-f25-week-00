class MinHeap:
    def __init__(self, max_size: int = 100):
        self.heap_array = [None] * max_size
        self.element_counter = 0
        self.max_size = max_size

    # Nav Functions 
    
    def left_child(self, parent_index: int) -> int:
        return 2 * parent_index + 1

    def right_child(self, parent_index: int) -> int:
        return 2 * (parent_index + 1)

    def parent(self, child_index: int) -> int:
        return (child_index - 1) // 2

    def swap(self, i: int, j: int) -> None:
        if i != j:
            temp = self.heap_array[i]
            self.heap_array[i] = self.heap_array[j]
            self.heap_array[j] = temp
         
    # Methods 

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

heap = MinHeap(10)

print(f"\nLeft child of 0: {heap.left_child(0)}") # 1
print(f"\nRight child of 0: {heap.right_child(0)}") # 2
print(f"\nParent of 3: {heap.parent(3)}") # 1

heap.heap_array[0] = "A"
heap.heap_array[1] = "B"
heap.element_counter = 2

print(f"\nBefore: {heap.display()}")
heap.swap(0, 1)
print(f"\nAfter: {heap.display()}")


        
        