#include<stdio.h>
#include<unistd.h>
//#include <stdlib.h>

int main() {
   printf("Hello, I'm exec1\n");
   printf("PID of exec1.c = %d\n", getpid());
   char* args[] = {"Hello", "Imran", "Butt", NULL};
   execv("./exec2.out", args);
   printf("Back to exec1.c\n");
    return 0;
}