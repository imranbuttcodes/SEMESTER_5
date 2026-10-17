#include <stdio.h>

int main() {
    int a, b, c;
    printf("Enter the length of side 1: ");
    scanf("%d", &a);
    printf("Enter the length of side 2: ");
    scanf("%d", &b);
    printf("Enter the length of side 3: ");
    scanf("%d", &c);

    if ((a > (b+c)) || (b > (a + c)) || (c > (a + b))) {
        printf("Invalid Triangle");
    } else if ((a == b) && (b == c)) {
        printf("Triangle is Equilateral");
    } else if ((a == b) || (a == c) || (b == c)) {
        printf("Triangle is Isosceles");
    } else {
        printf("Triangle is Scalene");
    }

}