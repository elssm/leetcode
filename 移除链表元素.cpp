/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


struct ListNode* removeElements(struct ListNode* head, int val){
    struct ListNode *p,*q,*ppre;
    ppre=p=head;
    if(p==NULL)
        return 0;
    else{
        while(p->next!=NULL){
            if(p->val==val&&p==head){
                q=p;
                p=p->next;
                ppre=head=p;
                free(q);
            }  
            else
                if(p->val==val&&p!=head){
                    q=p;
                    ppre->next=q->next;
                    p=q->next;
                    free(q);
                }
                else{
                    ppre=p;
                    p=p->next;
                }
        }
        if(p->val==val&&p==head)
            return 0;
        else
            if(p->val==val){
                q=p;
                ppre->next=q->next;
                free(q);
                return head;
            }
            else
                return head;
    }
}


