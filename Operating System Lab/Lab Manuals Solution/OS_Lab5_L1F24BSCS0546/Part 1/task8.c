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
        printf("Child Process: Executing a.out command.\n");
        execlp("./task1.out", "./task1.out", NULL);
        exit(0);
    } else {
        printf("Parent Process PID: %d\n", getpid());
        int status;

        waitpid(pid, &status, WNOHANG);
        if (WIFEXITED(status)) {
            printf("STatus returned %d\n", WEXITSTATUS(status));
        }

        printf("Parent Process: Child process completed successfully.\n");
    }
}