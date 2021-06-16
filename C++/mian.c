#include <stdio.h>;

int main() {
  int first = 0;
  int second;
  int third;
  // =
  third = second = first;

  int left, right;
  left = 2;
  right = 3;

  int sum;
  sum = left + right;
  int diff = left - right;
  int product = left * right; // 6
  int quotient = left / right;
  int remainder = left % right;

  int quitent_1 = 100 / 30; //

  int i = 1;
  int j = i++;
  int k = ++i;
  printf("3>3:%d\n", 3 > 2);
  printf("3>2 || 3< 2%d\n", 3 > 3 || 3 < 2);
  return 0;
}
