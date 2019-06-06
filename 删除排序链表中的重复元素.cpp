/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


struct ListNode* deleteDuplicates(struct ListNode* head){
    struct ListNode *p,*q;
    p=head;
    if(p==NULL)
        return 0;
    else
    {
        while(p->next!=NULL){
        if(p->next->val==p->val){
            q=p->next;
            p->next=q->next;
            free(q);
        }
        else
            p=p->next;  
    }
    return head;
    }
}

