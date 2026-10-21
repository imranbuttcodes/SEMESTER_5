#include <stdio.h>
#include <stdlib.h>

int main(int argc, char** argv) {
    if (argc != 3) {
        printf("Please Enter 2 integer arguments in command line\n");
        return 0;
    }

    int a = atoi(argv[1]);
    int b = atoi(argv[2]);
    
    printf("Entered numbers %d %d ", a, b);

    printf("\n");
    printf("%d * %d = %d\n", a, b, a * b);
}