#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <sys/wait.h>


int main(int argc, char* argv[]) {

    if (argc < 2) {
        perror("Please enter an array!");
        return 1;
    }
    int fd1[2], fd2[2], fd3[2], fd4[2];
    if (pipe(fd1) == -1 || pipe(fd2) == -1 || pipe(fd3) == -1 || pipe(fd4) == -1)  {
        perror("Couldn't Create ");
        return 1;
    }

    int n = argc - 1;

    int* arr = malloc(n * sizeof(int));

    for (int i = 0; i < n; i++) {
        arr[i] = atoi(argv[i + 1]);
    }

  
    pid_t child1 = fork();

    if (child1 < 0) {
        printf("Error creating Child1 !\n");
        return 1;
    }

    if (child1 == 0) {
        close(fd1[1]);
        close(fd2[0]);

        close(fd3[0]);
        close(fd3[1]);
        close(fd4[0]);
        close(fd4[1]);

        int* buffer = malloc(n * sizeof(int));

        read(fd1[0], buffer, n * sizeof(int));

        close(fd1[0]);

        int sum = 0;

        for (int i = 0; i < n; i++)
        {
            sum += buffer[i];
          
        }

        write(fd2[1], &sum, sizeof(sum));

        close(fd2[1]);
        
        exit(0);
    }

    pid_t child2 = fork();

    
    if (child2 < 0) {
        printf("Error creating Child2 !\n");
        return 1;
    }

    if (child2 == 0) {
        close(fd1[1]);
        close(fd1[0]);
        close(fd2[0]);
        close(fd2[1]);

        
        close(fd3[1]);
        close(fd4[0]);
        
        int* buffer = malloc(n * sizeof(int));

        read(fd3[0], buffer, n * sizeof(int));    
        
        close(fd3[0]);

        int min = buffer[0];

        for (int i = 0; i < n; i++)
        {
            if (buffer[i] < min) {
                min = buffer[i];
            }

        }
        
        write(fd4[1], &min, sizeof(min));

        close(fd4[1]);
        exit(0);

    }


    close(fd1[0]);
    close(fd2[1]);
    close(fd3[0]);
    close(fd4[1]);

    write(fd1[1], arr, n * sizeof(int));
    write(fd3[1], arr, n * sizeof(int));

    waitpid(child1, NULL, 0);
    waitpid(child2, NULL, 0);

    int sum, min;
    read(fd2[0], &sum, sizeof(sum));
    read(fd4[0], &min, sizeof(min));

    printf("SUM: %d\n", sum);
    printf("MIN: %d\n", min);
    
    close(fd1[1]);
    close(fd3[1]);
    close(fd2[0]);
    close(fd4[0]);

    return 0;
}