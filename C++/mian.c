#include <stdio.h>;

int main() {
  // const <type> readonly variable
  const int kRed = 0xFF0000;
  printf("kRed: %d\n", kRed);
  int *p_k_red = &kRed;
  *p_k_red = 0;
  printf("kRed: %\n", kRed);
  return 0;
}
