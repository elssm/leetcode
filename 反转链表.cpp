//���� 
struct ListNode* reverseList(struct ListNode* head) {
    if (head == NULL || head->next == NULL) //����Ϊ�ջ��߽�1����ֱ�ӷ���
        return head;
    struct ListNode* p = head, *newH = NULL;
    while (p != NULL)                 //һֱ��������β
    {
    struct  ListNode* tmp = p->next;          //�ݴ�p��һ����ַ����ֹ�仯ָ��ָ����Ҳ�����������
        p->next = newH;               //p->nextָ��ǰһ���ռ�
        newH = p;                     //�������ͷ�ƶ���p������һ������
        p = tmp;                   //pָ��ԭʼ����pָ�����һ���ռ�
    }
    return newH;
}

/**�ݹ� 
struct ListNode* reverseList(struct ListNode* head) {
    if (head == NULL || head->next == NULL)       //����Ϊ��ֱ�ӷ��أ���H->nextΪ���ǵݹ��
        return head;
    struct ListNode* newHead = In_reverseList(H->next); //һֱѭ������β 
    head->next->next = head;                       //��ת�����ָ��
    head->next = NULL;                          //�ǵø�ֵNULL����ֹ�������
    return newHead;   
}
**/ 
