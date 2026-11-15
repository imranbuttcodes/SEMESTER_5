
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>
#include <sys/types.h>
#include <sys/wait.h>

int main() {
    int fd[2];

    // Create pipe
    if (pipe(fd) == -1) {
        perror("pipe");
        return 1;
    }

    // Create first child: grep
    pid_t pid1 = fork();

    if (pid1 == -1) {
        perror("fork");
        return 1;
    }

    if (pid1 == 0) {

        // CHILD 1: grep "m"

        int input = open("input.txt", O_RDONLY);

        if (input == -1) {
            perror("open input.txt");
            _exit(1);
        }

        // Redirect stdin to input.txt
        dup2(input, STDIN_FILENO);
        close(input);

        // Close unused read end
        close(fd[0]);

        // Redirect stdout to pipe
        dup2(fd[1], STDOUT_FILENO);
        close(fd[1]);

        execlp("grep", "grep", "m", NULL);

        perror("execlp grep");
        _exit(1);
    }

    // Create second child: sort
    pid_t pid2 = fork();

    if (pid2 == -1) {
        perror("fork");
        close(fd[0]);
        close(fd[1]);
        waitpid(pid1, NULL, 0);
        return 1;
    }

    if (pid2 == 0) {

        // CHILD 2: sort

        // Close unused write end
        close(fd[1]);

        // Redirect stdin to pipe
        dup2(fd[0], STDIN_FILENO);
        close(fd[0]);

        int output = open(
            "output.txt",
            O_WRONLY | O_CREAT | O_TRUNC,
            0644
        );

        if (output == -1) {
            perror("open output.txt");
            _exit(1);
        }

        // Redirect stdout to output.txt
        dup2(output, STDOUT_FILENO);
        close(output);

        execlp("sort", "sort", NULL);

        perror("execlp sort");
        _exit(1);
    }

    // PARENT PROCESS

    close(fd[0]);
    close(fd[1]);

    waitpid(pid1, NULL, 0);
    waitpid(pid2, NULL, 0);

    return 0;
}
