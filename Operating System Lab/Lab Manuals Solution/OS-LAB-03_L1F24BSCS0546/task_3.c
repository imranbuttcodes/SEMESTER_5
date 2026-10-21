#include <stdio.h>



int main(){
    int arr[20];
    printf("%d %d ", arr[0], arr[2]);
    printf("Enter Array Elements (max 20, ) enter -99 to stop: ");

    int garbage, len = 0;
    for(int i = 0; i < 20; i++) {
        
        scanf("%d", &garbage);
        arr[i] = garbage;
        if (garbage == -99){
            break;
        }
        len += 1;
    }

    printf("\nOriginal Array: ");
    for (int i = 0; i < len; i++) {
        printf("%d ", arr[i]);
    }
    
    printf("\n");
// Bubble Sort Algorithm
    for (int i = 0; i < len - 1; i++) {
        for (int j = 0; j < len - i - 1; j++) {
                if (arr[j] > arr[j + 1]) {
                    int temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;
                }
        }
    }

    printf("\nSorted Array: ");
    
    for (int i = 0; i < len; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
}

