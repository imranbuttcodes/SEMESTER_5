#include<stdio.h>
#include<unistd.h>
//#include <stdlib.h>

int main() {
    printf("We are in exec2.c\n");
    printf("PID of exec2 = %d\n", getpid());
    char* args[] = {"Hello", "Imran", "Butt", NULL};
    return 0;
}