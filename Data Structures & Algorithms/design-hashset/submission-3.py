class ListNode:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next
class MyHashSet:

    def __init__(self):
        self.size = 10**4
        self.arr = [ListNode(0)] * self.size

    def findIndex(self, key) -> int:
        return key % self.size
    def add(self, key: int) -> None:
        index = self.findIndex(key)
        curr = self.arr[index]
        while curr and curr.next:
            if curr.next.val == key:
                return
            curr = curr.next
        curr.next = ListNode(key)

    def remove(self, key: int) -> None:
        index = self.findIndex(key)
        curr = self.arr[index]
        prev = curr
        while curr and curr.next:
            if curr.next.val == key:
                curr.next = curr.next.next
            prev = curr
            curr = curr.next
    def contains(self, key: int) -> bool:
        index = self.findIndex(key)
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