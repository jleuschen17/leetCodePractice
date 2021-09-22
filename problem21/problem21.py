class ListNode:
    def __init__(self, val=0, next=None):
        self.val = 0
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        pylist = []
        while True:
            checker = 0
            try:
                pylist.append(l1.val)
            except:
                checker += 1
            try:
                pylist.append(l2.val)
            except:
                checker += 1
            if checker == 2:
                break
            try:
                if l1.next == None and l2.next == None:
                    break
            except:
                try:
                    if l1.next == None:
                        break
                except:
                    pass
                try:
                    if l2.next == None:
                        break
                except:
                    pass

            else:
                try:
                    l1 = l1.next
                except:
                    pass
                try:
                    l2 = l2.next
                except:
                    pass
        pylistsorted = sorted(pylist)
        if len(pylistsorted) == 0:
            return None
        flnodes = []
        y = 0
        for x in range(len(pylistsorted) - 1, -1, -1):
            if x == len(pylistsorted) - 1:
                flnodes.append(ListNode(pylistsorted[x], None))
            else:
                flnodes.append(ListNode(pylistsorted[x], flnodes[y]))
                y += 1
        return flnodes[-1]