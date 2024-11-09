#Created By : Rutu Shah
#Created Date : 9th November 2024
#This is the task application demonstrating insert, search, delete using priority queue and max-heap data structure

from dataclasses import dataclass
from typing import Any, Optional
import time

@dataclass
class Task:
    """
    Represents a task in the priority queue.
    
    Attributes:
    1.	task_id: Unique identification of the task.
    2.	priority: Priority value of the task. In the case of a max heap, higher values denote higher priority.
    3.	arrival_time: Time at which the task arrived.
    4.	deadline: Time by which this task needs to be completed. It is optional but may be used in making task scheduling decisions.
    5.	Data : any additional task-specific data

    """
    task_id: int
    priority: int
    arrival_time: float
    deadline: Optional[float] = None
    data: Any = None

class PriorityQueue:
    """
    Max-heap implementation of a priority queue.
    
    We use a list-based implementation for the following reasons:
    1. Dynamic sizing - Python lists handle resizing automatically
    2. Index-based access - O(1) access to any element
    3. Cache-friendly - Contiguous memory allocation
    """
    
    def __init__(self):
        # Using list with sentinel element at index 0 for simpler index calculations
        self._heap = [None]
        
    def _parent(self, index: int) -> int:
        """Return the parent index of the given index."""
        return index // 2
    
    def _left_child(self, index: int) -> int:
        """Return the left child index of the given index."""
        return 2 * index
    
    def _right_child(self, index: int) -> int:
        """Return the right child index of the given index."""
        return 2 * index + 1
    
    def _swap(self, i: int, j: int) -> None:
        """Swap elements at indices i and j."""
        self._heap[i], self._heap[j] = self._heap[j], self._heap[i]
    
    def _shift_up(self, index: int) -> None:
        """
        Restore heap property by moving element up.
        Time Complexity: O(log n)
        """
        parent = self._parent(index)
        if index > 1 and self._heap[index].priority > self._heap[parent].priority:
            self._swap(index, parent)
            self._shift_up(parent)
    
    def _shift_down(self, index: int) -> None:
        """
        Restore heap property by moving element down.
        Time Complexity: O(log n)
        """
        max_index = index
        left = self._left_child(index)
        right = self._right_child(index)
        
        if (left < len(self._heap) and 
            self._heap[left].priority > self._heap[max_index].priority):
            max_index = left
            
        if (right < len(self._heap) and 
            self._heap[right].priority > self._heap[max_index].priority):
            max_index = right
            
        if index != max_index:
            self._swap(index, max_index)
            self._shift_down(max_index)
    
    def insert(self, task: Task) -> None:
        """
        Insert a new task into the priority queue.
        Time Complexity: O(log n)
        
        """
        self._heap.append(task)
        self._shift_up(len(self._heap) - 1)
    
    def extract_max(self) -> Optional[Task]:
        """
        Remove and return the highest priority task.
        Time Complexity: O(log n)
        
        """
        if self.is_empty():
            return None
            
        max_task = self._heap[1]
        self._heap[1] = self._heap[-1]
        self._heap.pop()
        
        if not self.is_empty():
            self._shift_down(1)
            
        return max_task
    
    def modify_priority(self, task_id: int, new_priority: int) -> bool:
        """
        Modify the priority of a task and restore heap property.
        Time Complexity: O(n + log n) due to linear search
        
        """
        # Linear search to find task - could be improved with additional data structure
        for i in range(1, len(self._heap)):
            if self._heap[i].task_id == task_id:
                old_priority = self._heap[i].priority
                self._heap[i].priority = new_priority
                
                if new_priority > old_priority:
                    self._shift_up(i)
                else:
                    self._shift_down(i)
                return True
        return False
    
    def is_empty(self) -> bool:
        """
        Check if priority queue is empty.
        Time Complexity: O(1)
        
        """
        return len(self._heap) == 1
    
    def peek(self) -> Optional[Task]:
        """
        Return highest priority task without removing it.
        Time Complexity: O(1)
        """
        return self._heap[1] if not self.is_empty() else None
    
    def size(self) -> int:
        """
        Return number of tasks in queue.
        Time Complexity: O(1)
        
        """
        return len(self._heap) - 1

# Example usage and testing
def test_priority_queue():
    pq = PriorityQueue()
    
    # Create sample tasks
    tasks = [
        Task(1, 3, time.time(), time.time() + 3600, "Low priority task"),
        Task(2, 5, time.time(), time.time() + 1800, "Medium priority task"),
        Task(3, 7, time.time(), time.time() + 900, "High priority task")
    ]
    
    # Test insertion
    for task in tasks:
        pq.insert(task)
        print(f"Inserted task {task.task_id} with priority {task.priority}")
    
    # Test peek
    highest = pq.peek()
    print(f"\nHighest priority task has ID {highest.task_id} and priority {highest.priority}")
    
    # Test priority modification
    pq.modify_priority(1, 8)
    print(f"\nModified task 1 priority to 8")
    highest = pq.peek()
    print(f"New highest priority task has ID {highest.task_id} and priority {highest.priority}")
    
    # Test extraction
    print("\nExtracting all tasks:")
    while not pq.is_empty():
        task = pq.extract_max()
        print(f"Extracted task {task.task_id} with priority {task.priority}")

if __name__ == "__main__":
    test_priority_queue()