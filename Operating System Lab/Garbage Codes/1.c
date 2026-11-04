#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>
#include <sys/types.h>

int main() {
    pid_t pid = fork();
wait(NULL);
    if (pid < 0) {
        printf("fork failed.\n");
        return 1;
    } 
    else if (pid == 0) {
        printf("child i am working.\n");
        // execlp replaces the process image. If successful, code below it won't execute.
        execlp("ls", "ls", "-l", NULL);
        
        // If execlp fails, this part will execute
        perror("execlp failed");
        return 1;
    } 
    else {
        int status;
        printf("parent wait for child completion.\n");
        
        // Pass the address of 'status' to capture the exit details
        wait(&status); 
        
        // Check if the child terminated normally
        if (WIFEXITED(status)) {
            // Extract the actual return code or exit code of the child
            int exit_code = WEXITSTATUS(status);
            printf("child process exited normally with code: %d\n", exit_code);
        } else {
            printf("child process did not terminate normally.\n");
        }
        
        printf("parent process completed.\n");
    }
    return 0;
}
