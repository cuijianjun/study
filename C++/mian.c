#include <stdio.h>;

int main() {
  // const <type> readonly variable
  const int kRed = 0xFF0000;
  printf("kRed: %d\n", kRed);
  int *p_k_red = &kRed;
  *p_k_red = 0;
  printf("kRed: %\n", kRed);
  // 字面量 literal
  3;
  3u;
  3l;
  3.f;
  3.9;
  'c';
  "cs";
  L'中'； L"中国";
  // 硬编码 hard code
  int background_color = kRed;
  return 0;
}
