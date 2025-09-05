# Rachel Riemersma

class MinHeap:
    def __init__(self, max_size: int = 100):
        """
        Initialize the minimum heap with a maximum size
        Args:
            max_size: maximum capacity of the heap.(default to 100)
        """
        self.heap_array = [None] * max_size 
        self.element_counter = 0 
        self.max_size = max_size 
    
    def left_child(self, parent_index: int) -> int:
        """ Returns the index of the left child of a node """
        return 2 * parent_index + 1

    def right_child(self, parent_index: int) -> int:
        """ Returns the index of the right child of a node """
        return 2 * (parent_index + 1)

    def parent(self, child_index: int) -> int:
        """ Returns the index of the parent of a child node """
        return (child_index - 1) // 2

    def swap(self, i: int, j: int) -> None:
        """
        Swaps two elements in the heap array using temporary variable 
        Args:
            i: index of the first element
            j: index of the second element 
        """
        if i != j:
            temp = self.heap_array[i]
            self.heap_array[i] = self.heap_array[j]
            self.heap_array[j] = temp

    def valid_index(self, index: int) -> bool:
        """ Checks if the index is within current heap size """
        return 0 <= index < self.element_counter
    
    def move_down(self, parent_index: int) -> None:
        """
        Restores heap property by moving the element at parent_index down the heap
        Args:
            parent_index: index of the node to move down 
        """
        current = parent_index
        property_satisfied = False
        while not property_satisfied:
            left_index = self.left_child(current)
            right_index = self.right_child(current)
            smallest = current
            # check if left child is smaller
            if (self.valid_index(left_index) and self.heap_array[left_index] < self.heap_array[smallest]):
                smallest = left_index
            # check if right child is smaller     
            if (self.valid_index(right_index) and self.heap_array[right_index] < self.heap_array[smallest]):
                smallest = right_index
            # if parent is already the smallest, stop     
            if smallest == current:
                property_satisfied = True
            # swap parent with smaller child and continue     
            else:
                self.swap(current, smallest)
                current = smallest

    def move_up(self, child_index: int) -> None:
        """
        Restores heap property by moving the element at child_index up the heap
        Args:
            child_index: index of the node to move up 
        """
        current = child_index 
        # executes while the current node is not the root and the parent is greater than child 
        while current > 0 and self.heap_array[self.parent(current)] > self.heap_array[current]:
            parent_index = self.parent(current)
            # swap with parent 
            self.swap(parent_index, current)
            current = parent_index

    def add(self, value) -> bool:
        """
        Inserts a new value into the heap
        Args:
            value: element being inserted 
        Returns:
            bool: True -> inserted successfully, False -> heap is full    
        """
        # the heap is full
        if self.element_counter >= self.max_size:
            return False 
        # inserts at next free spot 
        self.heap_array[self.element_counter] = value
        # restore minimum heap property 
        self.move_up(self.element_counter)
        self.element_counter += 1
        return True

    def remove(self):
        """
        Remove and return the minimum element from the heap 
        Returns:
            The minimum element or None if heap is empty 
        """
        # nothing to remove 
        if self.is_empty():
            return None
        # root is the minimum 
        minimum = self.heap_array[0]
        self.element_counter -= 1
        if self.element_counter > 0:
            # move last element to root and restore 
            self.heap_array[0] = self.heap_array[self.element_counter]
            self.heap_array[self.element_counter] = None
            self.move_down(0)
        else: 
            # heap becomes empty
            self.heap_array[0] = None 
        return minimum                              
    
    def peek(self):
        """
        Returns the minimum element without removing it 
        Returns:
            The minimum element or None if heap is empty
        """
        if self.is_empty():
            return None
        return self.heap_array[0]

    def size(self) -> int:
        """ Return the number of elements in the heap """
        return self.element_counter
    
    def is_empty(self) -> bool:
        """ Check if heap is empty """
        return self.element_counter == 0 
    
    def display(self) -> str:
        """ Displays the heap as a string """
        if self.is_empty():
            return "Empty heap"
        elements = []
        for i in range(self.element_counter):
            elements.append(str(self.heap_array[i]))
        return f"Heap: [{', '.join(elements)}]" 


