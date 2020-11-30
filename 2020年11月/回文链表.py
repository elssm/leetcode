# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        #第一种思路
        #再创建一个链表与head相反，然后逐个对比
        #超时 失败
        #第二种思路
        #用list存下链表所有值，逐个对比
        #超时 失败
        #第三种思路
        #快慢指针找到中间节点，逆转后面的链表，逐个对比
        #超时 失败
        #第四种思路
        #将链表存到列表中，对比列表前后值
        if head==None or head.next==None:
            return True
        if head!=None and head.next!=None and head.next.next==None:
            if head.val==head.next.val:
                return True
            else:
                return False
        c=[]
        pre=head
        while pre:
            c.append(pre.val)
            pre=pre.next
        i=0
        j=-1
        for i in range(len(c)/2):
            if c[i]!=c[j]:
                return False
            j-=1
        return True

        # 参考方法
        # s1=0
        # s2=0
        # t=1

        # while head!=None:
        #     s1=s1*10+head.val
        #     s2=s2+t*head.val
        #     t=t*10
        #     head=head.next
            
        # return s1==s2
        



