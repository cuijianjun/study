#include <stdio.h>;

int main() {
  // 字符集 ASCII
  char a = 'a'; // 97
  char char_1 = '1';
  char char_0 = '0';

  char i = 0; // \0, null
  // 字面量 literal
  // \n : new line
  // \b: backspace
  // \r:return
  // \t: table

  // Unicode CJK code point
  // C95
  wchar_t zhong = L"中";
  wchar_t zhogn_hex = L'\u4E2D';
  printf("中：%d\n", zhong);
  printf("中： %d\n", zhogn_hex);
}
