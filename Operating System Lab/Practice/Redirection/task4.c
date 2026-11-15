#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>
#include <sys/types.h>
#include <sys/wait.h>

int main() {

    pid_t pid = fork();

    if (pid < 0) {
        printf("ERROR");
        return 1;
    }


    if (pid == 0) {
        int fd = open("input.txt", O_WRONLY | O_CREAT | O_TRUNC, 0644);

        dup2(fd, STDOUT_FILENO);


        close(fd);

        char* args[] = {"ls", "/", "-l", NULL};

        execvp(args[0], args);

        perror("WTF");

    } else {
        int status;
        waitpid(pid, &status,0);

        if (WIFEXITED(status)) {
            printf("Child exited with status: %d\n",
                   WEXITSTATUS(status));
        }
    }
}