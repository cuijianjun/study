#include "stdafx.h";

void main(void)
{
    bool bA = false, bB = true;
    cout < < (bA == true || bA != true) < < endl;
    cout < < (bB == true || bB != true) < < endl;
    // 德*摩根率
    cout < < (!(bA || bB) == (!bA && !bB)) < < endl;
    cout < < (!(bA && bB) == (!bA || !bB)) < < endl;
}
