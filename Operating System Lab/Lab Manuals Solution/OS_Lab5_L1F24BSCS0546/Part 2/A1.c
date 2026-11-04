#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>

int main() {
    pid_t pid = fork();
    if (pid < 0) { perror("fork"); return 1; }
    if (pid == 0) {
        printf("CHILD PID: %d\n", getpid());
        execl("/bin/echo", "echo", "Hello from exec", NULL);
        perror("execl failed");
        _exit(1);
    }
    wait(NULL);
    printf("Parent: done\n");
    return 0;
}