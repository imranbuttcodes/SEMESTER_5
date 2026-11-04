#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>

int main(int argc, char *argv[]) {
    if (argc != 2) { fprintf(stderr, "Usage: %s <file>\n", argv[0]); return 1; }
    pid_t pid = fork();
    if (pid == 0) {
        execlp("cat", "cat", argv[1], NULL);
        perror("cat failed");
        _exit(1);
    }
    int status;
    wait(&status);
    if (WIFEXITED(status) && WEXITSTATUS(status) == 0)
        printf("Parent: file displayed successfully\n");
    else
        printf("Parent: cat failed\n");
    return 0;
}