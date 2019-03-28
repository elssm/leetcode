/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* middleNode(struct ListNode* head) {
    int n=1;
    struct ListNode  *f=head ,*s=head;//¿ìÂıÖ¸Õë 
    while(f!=NULL&&f->next!=NULL){
        s=s->next;
        f=f->next->next;
    }
    return s;
}
