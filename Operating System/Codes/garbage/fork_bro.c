#include<stdio.h>
#include<unistd.h>
#include<sys/wait.h>
#include<sys/types.h>


int main() {

  //  fork();
    // fork();
    // printf("Hello, WOrld!\n");
    fork();
    fork();
    fork();
    printf("Hello, Imran!\nPID: %d\n", getpid());
    return 0;
}