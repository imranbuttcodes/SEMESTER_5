//grep “m” < input.txt | sort > output.txt

#include <stdio.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>
#include <stdlib.h>

int main() {
    int fd[2];

    if (pipe(fd) < 0) {
        perror("Error in creating pipe!");
        exit(1);
    }

    pid_t pid1 = fork();


    if (pid1 < 0) {
        perror("Error in fork!\n");
        exit(1);
    }

    if (pid1 == 0) {
        close(fd[0]);

        dup2(fd[1], 1);

        close(fd[1]);

        execlp("ls", "ls", NULL);

        perror("execlp ls");
        exit(1);
    
    } else {
        
        close(fd[1]);

        dup2(fd[0], 0);

        close(fd[1]);
    
        execlp("wc", "wc", NULL);
 
        
        perror("execlp wc");
        exit(1);
    
    }



}


