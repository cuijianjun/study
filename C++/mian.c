#include <stdio.h>;

int main() {
  // <type> <name>
  int value;
  // <type> <name> = <initialized value>
  int value_init = 3;

  value = 4;
  value_init = 5;

  printf("value: %d\n", value);
  value_init = value;
  printf("value");
  return 0;
}
