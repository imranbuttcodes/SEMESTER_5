#include <stdio.h> 
#include <unistd.h>
#include <sys/wait.h> 
#include <stdlib.h>

int main(int argc, char *argv[]) {
    if (argc < 2) { 
        fprintf(stderr, "Usage: %s <program> [arguments...]\n", argv[0]);
        return 1;
    }

pid_t pid = fork();

if (pid < 0) {
    perror("fork failed");
    return 1;
}

if (pid == 0) {
    execv(argv[1], &argv[1]);

    perror("execv failed");
    _exit(1);
}

wait(NULL);
return 0;


}