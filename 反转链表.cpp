//迭代 
struct ListNode* reverseList(struct ListNode* head) {
    if (head == NULL || head->next == NULL) //链表为空或者仅1个数直接返回
        return head;
    struct ListNode* p = head, *newH = NULL;
    while (p != NULL)                 //一直迭代到链尾
    {
    struct  ListNode* tmp = p->next;          //暂存p下一个地址，防止变化指针指向后找不到后续的数
        p->next = newH;               //p->next指向前一个空间
        newH = p;                     //新链表的头移动到p，扩长一步链表
        p = tmp;                   //p指向原始链表p指向的下一个空间
    }
    return newH;
}

/**递归 
struct ListNode* reverseList(struct ListNode* head) {
    if (head == NULL || head->next == NULL)       //链表为空直接返回，而H->next为空是递归基
        return head;
    struct ListNode* newHead = In_reverseList(H->next); //一直循环到链尾 
    head->next->next = head;                       //翻转链表的指向
    head->next = NULL;                          //记得赋值NULL，防止链表错乱
    return newHead;   
}
**/ 
