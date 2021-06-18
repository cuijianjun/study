#include <stdio.h>;

double f(double x) {
    return x * x + x + 1;
  }
double g(double x, double y, double z) {
  return x * x + y * y + z * z;
}

int main() {
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
