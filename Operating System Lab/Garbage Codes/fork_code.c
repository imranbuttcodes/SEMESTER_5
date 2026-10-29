#include<stdio.h>
#include<unistd.h>

int main() {
    printf("pid, A: %d\n", getpid());

    pid_t pid = fork();
    if (pid == 0) {
        printf("child: pid: %d\n", getpid());
        printf("child: ppid: %d\n", getppid());
    } else if (pid > 0) {
        printf("Parent: pid, A: %d\n", getpid());
    }
    
    
}