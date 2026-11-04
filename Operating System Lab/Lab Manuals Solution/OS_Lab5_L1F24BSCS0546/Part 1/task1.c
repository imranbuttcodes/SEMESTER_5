#include<stdio.h>
#include <unistd.h>
#include <sys/wait.h>
#include <stdbool.h>
#include <stdlib.h>


int main() {

    pid_t pid = fork();

    if (pid < 0) {
        printf("Fork Failed!\n");
        return 1;
    } else if (pid == 0) {
        printf("Child procss pid: %d\n", getpid());
        char c = 'A';
        while (true)
        {
            if (c == 'F') {
                exit(0);
            }
            printf("Child: %c\n", c);
            c += 1;
        }
        

    } else {
            printf("Parent process pid: %d\n", getpid());
            for (int i = 1; i < 6; i++) {
            printf("Parent: %d\n", i);
        }

        wait(NULL);
    }

    

   
    return 0;
}