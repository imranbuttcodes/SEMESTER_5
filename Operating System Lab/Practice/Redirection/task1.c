
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>


int main() {
    int fd[2];

    // Create pipe
    if (pipe(fd) == -1) {
        perror("pipe");
        return 1;
    }

    // Create first child: ls
    pid_t pid1 = fork();

    if (pid1 == -1) {
        perror("fork");
        return 1;
    }

    if (pid1 == 0) {

        // CHILD 1: Execute ls

        close(fd[0]);  // Close unused read end

        dup2(fd[1], STDOUT_FILENO);

        close(fd[1]);

        execlp("ls", "ls", NULL);

        perror("execlp ls");
        _exit(1);
    }

    // Create second child: wc
    pid_t pid2 = fork();

    if (pid2 == -1) {
        perror("fork");

        close(fd[0]);
        close(fd[1]);

        waitpid(pid1, NULL, 0);
        return 1;
    }

    if (pid2 == 0) {

        // CHILD 2: Execute wc

        close(fd[1]);  // Close unused write end

        dup2(fd[0], STDIN_FILENO);

        close(fd[0]);

        execlp("wc", "wc", NULL);

        perror("execlp wc");
        _exit(1);
    }

    // PARENT PROCESS

    close(fd[0]);
    close(fd[1]);

    waitpid(pid1, NULL, 0);
    waitpid(pid2, NULL, 0);

    return 0;
}
