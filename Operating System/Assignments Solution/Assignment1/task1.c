
#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>
#include <stdlib.h>

int main() {
    pid_t pid;
   // printf("%d\n", getpid());
    pid = fork();

    if (pid < 0) {
        printf("Fork failed!\n");
        return 1;
    }
    else if (pid == 0) {
        
        printf("[CHILD] PID: %d, PPID: %d\n", getpid(), getppid());

        sleep(3);

        printf("[CHILD] Finished sleeping for 3 seconds.\n");
        exit(0);
    }
    else {
       
        printf("[PARENT] PID: %d, PPID: %d\n", getpid(), getppid());

        int status;
        int seconds = 0;

        while (1) {
            pid_t result = waitpid(pid, &status, WNOHANG);

            if (result == pid) {
                printf("[PARENT] Child has terminated.\n");
                break;
            }

            sleep(1);
            seconds++;

            printf("[PARENT] Child is still running. Time: %d second(s)\n",
                   seconds);
        }

        printf("[PARENT] Parent process finished.\n");
    }

    return 0;

}
