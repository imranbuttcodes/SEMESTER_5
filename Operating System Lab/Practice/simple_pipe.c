#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char *argv[]) {
    int fd[2]; //0->read , 1-> write

    if(pipe(fd) == -1) {
        perror("erorr generating pipe!\n");
        exit(1);
    }

    
    pid_t child = fork();

    if (child > 0) {
        

        close(fd[0]);

        write(fd[1], argv[1], strlen(argv[1]) + 1);
        printf("Data sent!\n");
        
    } else {
        close(fd[1]);

        char recieved[strlen(argv[1])];
        read(fd[0], recieved, sizeof(recieved));

        printf("data recieved : %s\n", recieved);
    }


    return 0;
}