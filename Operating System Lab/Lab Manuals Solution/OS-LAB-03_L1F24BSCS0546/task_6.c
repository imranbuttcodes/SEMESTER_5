
#include <stdio.h>
#include <stdlib.h>

int main() {
    int n, i;
    int min, secondMin;

    printf("Enter the size of array: ");
    scanf("%d", &n);

    if (n < 2) {
        printf("Array must contain at least 2 elements.\n");
        return 1;
    }

    int *arr = (int *)malloc(n * sizeof(int));

    if (arr == NULL) {
        printf("Memory allocation failed.\n");
        return 1;
    }

    printf("Enter %d integers:\n", n);

    for (i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }

    min = secondMin = 0;

    for (i = 0; i < n; i++) {
        if (i == 0) {
            min = arr[i];
        } else if (arr[i] < min) {
            secondMin = min;
            min = arr[i];
        } else if (arr[i] > min &&
                   (secondMin == 0 || arr[i] < secondMin)) {
            secondMin = arr[i];
        }
    }

    printf("Second minimum number: %d\n", secondMin);

    free(arr);

    return 0;
}
