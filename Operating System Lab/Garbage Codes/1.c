// // #include <stdio.h>
// // #include <unistd.h>
// // #include <sys/wait.h>
// // #include <sys/types.h>

// // int main() {
// //     pid_t pid = fork();
// // wait(NULL);
// //     if (pid < 0) {
// //         printf("fork failed.\n");
// //         return 1;
// //     } 
// //     else if (pid == 0) {
// //         printf("child i am working.\n");
// //         // execlp replaces the process image. If successful, code below it won't execute.
// //         execlp("ls", "ls", "-l", NULL);
        
// //         // If execlp fails, this part will execute
// //         perror("execlp failed");
// //         return 1;
// //     } 
// //     else {
// //         int status;
// //         printf("parent wait for child completion.\n");
        
// //         // Pass the address of 'status' to capture the exit details
// //         wait(&status); 
        
// //         // Check if the child terminated normally
// //         if (WIFEXITED(status)) {
// //             // Extract the actual return code or exit code of the child
// //             int exit_code = WEXITSTATUS(status);
// //             printf("child process exited normally with code: %d\n", exit_code);
// //         } else {
// //             printf("child process did not terminate normally.\n");
// //         }
        
// //         printf("parent process completed.\n");
// //     }
// //     return 0;
// // }


// // #include <stdio.h>
// // #include <stdlib.h>

// // int main() {

// //     char *home = getenv("HOME");
// //     setenv("LAB_MODE", "fork-exec", 1);
// //     if (home != NULL) {
// //         printf("HOME: %s\n", home);
// //     }
// //     else {
// //         printf("HOME not found!\n");
// //     }

// //     return 0;
// // }


// #include <stdio.h>
// #include <unistd.h>
// #include <stdlib.h>

// int main() {
//     setenv("IMRAN_BRO", "imranbuttcodes", 1);

//     pid
// }


#include <stdio.h>
#include <string.h>
int main() {
// char input[100] = {"IMRAN"};

// printf("Enter something: \n");
// fgets(input, sizeof(input), stdin);

// printf("%s\n", input);

char input[] = "ls -l /home";

char* token = strtok(input, " ");

printf("%s\n\n", token);


while (token != NULL) {
    printf("%s\n", token);
    token = strtok(NULL, " ");
}

}