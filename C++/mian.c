#include <stdio.h>;

int main() {
  srand(time(NULL));
  int magic_number = rand();
  while (1)
  {
    int user_input;
    puts("Please input a number");
    scanf("%d", &user_input);
    if (user_input > magic_number) {
      puts("Your number is bigger");
    }
    else if (user_input < magic_number)
    {
      puts("Your number is smaller!");
    } else {
      puts("Yes! You got it");
      break;
    }
  }

  return 0;
}
