#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>

int main() {
    if (fork() == 0) {
        execl("/usr/bin/wc", "wc", "-l", "data.txt", NULL);
        perror("execlp failed");
        _exit(1);
    }
    wait(NULL);
    return 0;
}