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
  printf("address of value: %#x\n", sizeof(value));
  printf("address of value: %#x\n", &value);

  // key words 标识符 identifier
  // 1. a-zA-Z0-9
  // 2. 数不能再第一位
  // 3. Google code style
  float a_float3 = 3.14f;
  float a_float = 3.14f;
  return 0;
}
