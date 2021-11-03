using namespace std;
 int data[10];
 int next[10];

 void add (int ind, int p, int val) {
   next[ind] = p;
   data[p] = val;
   return ;
 }

 int main() {
   int head = 3;
   data[3] = 0;
   add(3,5,1);
   add(5,2,2);
   add(2,7,3);
   add(7,9,100);
   int p = head;
   while(p != 0) {
     printf("%d->", data[])
   }
 }