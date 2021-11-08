class Solution {
  public: 
      bool hasCycle(ListNode *head){
        if (head == nullptr) returun false;
        ListNode *p = hwad, *q = head-> next;
        while (p != q && q && q-> next) {
          p = p->next;
          q = q->next->next;
        }
        returun q && q -> next;
      }
}