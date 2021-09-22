class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pylist = []
        try:
            test = head.val
        except:
            return None
        while True:
            try:
                pylist.append(head.val)
            except:
                break
            try:
                head = head.next
            except:
                break
        flist = []
        for x in range(0, len(pylist), 2):
            try:
                flist.append(0)
                flist.append(0)
                flist[x] = pylist[x+1]
                flist[x+1] = pylist[x]
            except:
                flist.append(0)
                flist[x] = pylist[x]
        flnodes = []
        y = 0
        for x in range(len(flist) - 1, -1, -1):
            if x == len(flist) - 1:
                flnodes.append(ListNode(flist[x], None))
            else:
                flnodes.append(ListNode(flist[x], flnodes[y]))
                y += 1
        return flnodes[-1]