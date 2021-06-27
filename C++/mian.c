#include <stdio.h>;

int global_var = 1;
void LocalstaticVar(void) {
  // 静态变量
  // 1. 作用域全局，内存不会因函数退出而销毁
  // 2. int 初始值默认为0
  static int static_var;
  // 自动变量
  // 1. 函数，块作用域，随着函数的块退出而销毁
  // 2. 没有默认的初值
  int non_static_var;
  printf("static var : %d\n", static_var++);
  printf("non static var : %d\n", non_static_var++);
}

double Add(double a, double b);

// proto scope
double Sort(int size, int array[size]);

int main(void){
  // 自动变量
  auto int value = 0;
  {
    auto int a = 0;
    printf("%d\n", a);
  }
}