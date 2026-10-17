#include<stdio.h>


int main(){
    float length, width, area;
    printf("What is the length of rectangle?: ");
    scanf("%f", &length);
    printf("What is the width of rectangle?: ");
    scanf("%f", &width);
    area = length * width;
    printf("The area of rectangle is %f\n", area);
}