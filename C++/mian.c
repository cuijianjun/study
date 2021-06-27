#include <stdio.h>;

double f(double x) {
    return x * x + x + 1;
  }
double g(double x, double y, double z) {
  return x * x + y * y + z * z;
}

int main(void) {
  /**
   * <return type> <name> (<parmaeters>) {
   *  ...statement
   *  return <return value>;
   * }
   * 
   * 
   * */
  puts("HelloWorld");
  double return_f = f(2.0);
  double return_g = g(3.0, 4.0, 5.0);

  printf("result of f: %f\n", return_f);
  printf("result of f: %f\n", return_g);
  return 0;
}

void EmptyParamList(void);

/*
  1. 函数名
  2.函数的返回值类型，如果没写，默认为int
  3. 函数参数列表，参数类型和参数顺序，参数形参顺序，参数形参名不重要
*/

int Add(int, int);

int main2(void){
  puts("");
  EmptyParamList();
  int result = Add(1, 2);
  return 0;
}
