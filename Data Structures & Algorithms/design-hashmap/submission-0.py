class ListNode:
    def __init__(self,key, val, next = None):
        self.key = key
        self.val = val
        self.next = next

class MyHashMap:

    def __init__(self):
        self.size = 10**4
        self.arr = [ListNode(0, 0)] * self.size

    def put(self, key: int, value: int) -> None:
        index = key % self.size
        curr = self.arr[index]
        while curr and curr.next:
            if curr.next.key == key:
                curr.next.val = value
                return
            curr = curr.next
        curr.next = ListNode(key, value)

    def get(self, key: int) -> int:
        index = key % self.size
        curr = self.arr[index]
        while curr and curr.next:
            if curr.next.key == key:
                return curr.next.val
            curr = curr.next
        return -1

    def remove(self, key: int) -> None:
        index = key % self.size
        curr = self.arr[index]
        prev = curr
        curr = curr.next
        while curr:
            if curr.key == key:
                break
            prev = curr
            curr = curr.next
        if curr:
            prev.next = curr.next


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)