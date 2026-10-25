#include <unistd.h>
#include <stdio.h>
#include <sys/wait.h>

int main() {
    pid_t pid1 = fork();
    

    if (pid1 < 0) {
        perror("fork() failed for CHILD1\n");
        return 1;
    }

    if (pid1 == 0) {
        printf("[Child 1] Executing date command:\n");
        execlp("date", "date", NULL);
        printf("\n");
        return 0;
    }


    pid_t pid2 = fork();

    if (pid2 < 0) {
        perror("fork() failed for CHILD2\n");
        return 1;
    }


    if (pid2 == 0) {

        printf("[Child 2] Executing whoami command:\n");
        execlp("whoami", "whoami", NULL);
    }


    
    printf("[parent]: waiting for both childs to terminaten\n");
    wait(NULL);
    wait(NULL);
    printf("Parent: Both child processes have completed successfully.\n");


}