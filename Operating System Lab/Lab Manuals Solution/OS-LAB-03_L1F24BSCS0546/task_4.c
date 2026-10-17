#include <stdio.h>

void isPrime(int num, int& prime) {
    if (num <= 1) {
        prime = 0;
        return;
    }

    for (int i = 2; i * i <= num; i++) {
        if (num % i == 0) {
            prime = 0;
            return;
        }
    }
    prime =1 ;
    return;
}


int main() {
    int num;
    printf("Enter Num to check if it is prime or not: ");
    scanf("%d", &num);
    int prime;
    isPrime(num, prime);
    printf("IsPrime: %s\n", (prime ? (const char*)"Yes": (const char*)"NO"));
}