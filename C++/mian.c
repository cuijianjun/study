#include <stdio.h>;

int main() {
  short int short_int = 0;
  int i = 0;
  long int long_int = 0;
  long long int longlong_int = 0;
  // d = decimal
  // x = hex
  // 0 = oct
  // hd%: short decimal
  // %d: decimal
  // %ld: long decimal
  // %lld: long long decimal
  // %d : decimal
  // \n new line 
  printf("short int : %d\n", sizeof(short int));
  printf("int : %d\n", sizeof(int));
  printf("long int : %d\n", sizeof(long int));
}
