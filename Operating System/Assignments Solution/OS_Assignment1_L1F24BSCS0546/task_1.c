#include <unistd.h>
#include <stdio.h>
#include <sys/wait.h>
#include <stdlib.h>

int main() {
    pid_t pid = fork();

    if (pid < 0) {
        perror("Process Failed!");
        return 1;
    }


    if (pid == 0) {

        printf("Child process created. PID = %d, Parent PID = %d\n", getpid(), getppid());
        printf("Child is running...\n");
        sleep(3);
        printf("Child is Finished!\n");
        exit(0);

    } else {

        printf("Parent process started. PID = %d\n", getpid());
        int status;

        while(1) {
        
            pid_t result = waitpid(pid, &status, WNOHANG);

            if (result == -1) {
                perror("waitpid failed\n");
                return 1;
            }

            if (result == pid) {
                break;
            }
            printf("parent is waiting...\n");
            sleep(1);
       
        }

        printf("Parent detected child termination.\n");

    }

}   