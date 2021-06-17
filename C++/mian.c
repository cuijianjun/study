#include <stdio.h>;

int main() {
  _Bool is_enabled = true;
  is_enabled = 10;
  printf("is_enable:%d\n", is_enabled);
  is_enabled = false;
  bool is_visible = false;

  // if else 
  /**
   * if (<condition>){
   *  ... true statement
   * } else {
   * ...false statement
   * }
   * 
   * */
  
  #define MAGIC_NUMBER = 10
  int user_input;
  printf("please input a number : \n");
  scanf("%d", &user_input);
  if (user_input > MAGIC_NUMBER) {
    printf("Your number is bigger");
  } else if (user_input < MAGIC_NUMBER) {
    printf("Your number is smaller!")
  } else {
    printf("Yes! You got it!")
  }

  /*
  *
  switch(<cond>) {
    case 0: {}
    break;
    case 1: {

    }
  }
  */
 #define ADD "+"
 #define SUB "-"
 #define MULTIPLY "*"
 #define DIVIDE "/"
 #define REM "%"
  int left;
  int right;
  char operator;
  printf("please input an expression:\n");
  scanf("%d %c %d", &left, &operator, &right);
  int result;
  switch (operator)
  {
  case ADD:
    result = left + right;
    break;
  case SUB;
      result = left - right;
      default:
    break;
  }
  return 0;
}
