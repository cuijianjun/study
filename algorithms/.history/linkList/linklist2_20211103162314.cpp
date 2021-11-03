using namespace std;
 int data[10];
 int next[10];

 void add (int ind, int p, int val) {
   next[ind] = p;
   data[p] = val;
   return ;
 }

 int main