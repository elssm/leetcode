/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


struct ListNode* mergeTwoLists(struct ListNode* l1, struct ListNode* l2){
    if(l1==NULL)
        return l2;
    if(l2==NULL)
        return l1;
    if(l1->val<l2->val){
        l1->next=mergeTwoLists(l1->next,l2);
            return l1;
        }else{
        l2->next=mergeTwoLists(l1,l2->next);
            return l2;
    }
}

struct ListNode* mergeTwoLists(struct ListNode* l1, struct ListNode* l2){
	struct ListNode *p,q;
	if(l1==NULL)
		return l2;
	else if(l2==NULL)
		return l1;
	p=NULL;
	q=NULL;
	while(l1!=NULL&&l2!=NULL){
		if(l1->val<l2->val){
			if(p==NULL)
				p=q=l1;
			else{
				q->next=l1;
				q=q->next;
			}
			l1=l1->next;
		}
		else{
			if(p==NULL){
				p=q=l2;
			}
			else{
				q->next=l2;
				q=q->next;
			}
			l2=l2->next;
		}
}
		if(l1==NULL)
			q->next=l2;
		else
			q->next=l1;
		return p;
} 
 
 
