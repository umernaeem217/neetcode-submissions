class ListNode:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next
class MyHashSet:

    def __init__(self):
        self.capacity = 10000
        self.arr = [ListNode(-1) for _ in range(self.capacity)]

    def add(self, key: int) -> None:
        index = key % self.capacity
        curr = self.arr[index]
        while curr and curr.next:
            if curr.next.val == key:
                return
            curr = curr.next
        curr.next = ListNode(key)

    def remove(self, key: int) -> None:
        index = key % self.capacity
        curr = self.arr[index]
        prev = curr
        while curr and curr.next:
            if curr.next.val == key:
                curr.next = curr.next.next
            prev = curr
            curr = curr.next   

    def contains(self, key: int) -> bool:
        index = key % self.capacity
        curr = self.arr[index]
        while curr and curr.next:
            if curr.next.val == key:
                return True
            curr = curr.next
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)