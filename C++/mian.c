#include <stdio.h>;

int main() {
  float a_float = 3.14f; // 6, 7~8 + -10^-37 ~10^37
  printf("size of float: %d\n", sizeof(float));
  double a_double = 3.14;
  printf("size of double : %d\n", sizeof(double));
  float lat = 39.90815f;
  printf("%f", 39.908156f - lat);
  return 0;
}
