#include<stdio.h>
#include<unistd.h>
//#include <stdlib.h>

int main(int argc, char** argv) {
    printf("We are in exec2.c\n");
    printf("PID of exec2 = %d\n", getpid());
    printf("BRO GOT THESE ARGS FROM exec 2: %s %s %s\n", argv[0], argv[1], argv[2]);
    return 0;
}