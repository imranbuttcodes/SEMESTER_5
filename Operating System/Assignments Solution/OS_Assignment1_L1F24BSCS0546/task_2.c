#include <unistd.h>
#include <stdio.h>
#include <sys/wait.h>

int main() {
    pid_t pid = fork();


    if (pid == -1) {
        perror("fork() failed!\n");
        return 1;
    }

    if (pid == 0) {
        printf("I'm Child Process!\n");
        execlp("ls", "ls", "-l", NULL);


    } else {
        printf("Parent is waiting...\n");
        wait(NULL);
        printf("Child Terminated\n");
    }



    return 0;
}