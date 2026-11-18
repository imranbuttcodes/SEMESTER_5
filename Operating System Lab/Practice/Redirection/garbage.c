#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <fcntl.h>
#include <sys/types.h>
#include <sys/wait.h>

int main() {

    pid_t child1 = fork();

    if (child1 == 0) {


        int fd = open("input.txt", O_CREAT | O_TRUNC | O_WRONLY, 0644);
        
        dup2(fd,STDOUT_FILENO);


        execlp("ls", "ls", "/", "-l", NULL);
        
        exit(0);
    }


    int status;
    waitpid(child1, &status,0);

    if (WIFEXITED(status)) {
        printf("Child exited with status: %d\n", WEXITSTATUS(status));
    }


}