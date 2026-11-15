#include <stdio.h>
#include <sys/wait.h>
#include <unistd.h>
#include <string.h>

int main(int argc, char* argv[]) {
    
    if (argc < 1) {
        printf("BRO ENTER MORE DATA\n");
        return 1;
    }

    int n = argc - 1;

    int fd[2];

    pipe(fd);

    pid_t pid = fork();

    if (pid < 0) {
        perror("Couldn't create child!");
        return 1;
    }

    if (pid > 0) {
        close(fd[0]);
        
        write(fd[1], &argv[1], n * sizeof(char*));

        printf("Data sent!\n");
        close(fd[1]);
        wait(NULL);
    } else {
        close(fd[1]);
        char* recieved[n];
        read(fd[0], recieved, n * sizeof(char*));

        printf("%ld", n * sizeof(char*));

        for (int i = 0; i < n; i++)
        {
            printf("%s      ",recieved[i]);
        }
        printf("\n");
        close(fd[1]);
        
    }


    return 0;
}