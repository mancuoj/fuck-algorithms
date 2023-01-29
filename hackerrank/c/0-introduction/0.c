#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
    char s[100];
    scanf("%[^\n]%*c", &s);
    // scanf 正则
    // ^\n 读取输入直到遇到换行符
    // %*c 读取换行符然后用 * 表示丢弃该换行符

    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    printf("Hello, World!\n");
    printf(s);
    return 0;
}