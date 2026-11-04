#include<stdio.h>
#include <unistd.h>
#include <sys/wait.h>
#include <stdbool.h>
#include <stdlib.h>

int main() {
    pid_t pid = fork();

    if (pid < 0) {
        printf("fork failed!\n");
        return 1;
    } else if (pid == 0) {
        printf("Child Process: Executing date command.\n");
        execlp("date", "date", NULL);
        exit(0);
    } else {
        printf("Parent Process PID: %d\n", getpid());
        wait(NULL);
        printf("Parent Process: Child process completed successfully.\n");
    }
}