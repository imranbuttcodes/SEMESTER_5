#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <sys/wait.h>


int main(int argc, char* argv[]) {

    if (argc < 2) {
        printf("Usage: %s num1 num2 num3 ...\n", argv[0]);
        return 1;
    }


    int n = argc - 1;

    int* arr = malloc(n * sizeof(int));

    for (int i = 0; i < n; i++) {
        arr[i] = atoi(argv[i + 1]);
    }
 
    int fd1[2], fd2[2], fd3[2], fd4[2];

    if (pipe(fd1) == -1 ||
        pipe(fd2) == -1 || 
        pipe(fd3) == -1 || 
        pipe(fd4) == -1) {
            perror("Seems like an error so we Couldn't created 4 pipes!\n");
            free(arr);
            return 1;
    }

    pid_t pid1 = fork();

    if (pid1 < 0) {
        perror("an error occured during fork for second child\n");
        free(arr);
        return 1;
    }

    if (pid1 == 0) {
        close(fd1[1]);
        close(fd2[0]);
        
        
        close(fd3[0]);
        close(fd3[1]);
        close(fd4[0]);
        close(fd4[1]);  

        int* recieved = malloc(n * sizeof(int));

        if (recieved == NULL || 
            read(fd1[0], recieved, n * sizeof(int)) != (ssize_t)(n * sizeof(int))
        ) {
            perror("Couldn't recieve arr data in child 1\n");
            exit(1);
        }

        int sum = 0;

        for (int i = 0; i < n; i++)
        {
            sum += recieved[i];
        }

        close(fd1[0]);

        if (write(fd2[1], &sum, sizeof(sum)) != sizeof(sum)) {
            perror("Child 1 Write error");
            free(recieved);
            exit(1);
        }


        free(recieved);

        close(fd2[1]);

        exit(0);


    }


    pid_t pid2 = fork();

    if (pid2 < 0) {
        perror("an error occured during fork for second child\n");
        free(arr);
        exit(1);
    }


    if (pid2 == 0) {
        close(fd1[0]);
        close(fd1[1]);
        close(fd2[0]);
        close(fd2[1]);

        
        
        
        close(fd3[1]);
        close(fd4[0]);
     

        int* recieved = malloc(n * sizeof(int));

        if (recieved == NULL || 
            read(fd3[0], recieved, n * sizeof(int)) != (ssize_t)(n * sizeof(int))) {
               perror("Couldn't recieve arr data in child 2\n");
               exit(1);
            }

        int min = recieved[0];

        for (int i = 0; i < n; i++)
        {
            if (recieved[i] < min) {
                min = recieved[i];
            }
        }

        if (write(fd4[1], &min, sizeof(min)) != (size_t) (sizeof(min))) {
            perror("Child 1 Write error");
            exit(1);
        }

        close(fd3[0]);
        close(fd4[1]);

        free(recieved);
        exit(0);        
    }


    close(fd1[0]);
    close(fd2[1]);
    close(fd3[0]);
    close(fd4[1]);

    write(fd1[1], arr, n * sizeof(int));

    write(fd3[1], arr, n * sizeof(int));


    close(fd1[1]);
    close(fd3[1]);

    int sum, min;

    read(fd2[0], &sum, sizeof(sum));
    read(fd4[0], &min, sizeof(min));

    waitpid(pid1, NULL, 0);
    waitpid(pid2, NULL, 0);

    printf("\nSum = %d\n", sum);
    printf("Minimum = %d\n", min);
    
    free(arr);

    return 0;
}