#include <stdio.h>
#include <stdlib.h>

int main() {
     int l;
     printf("Enter len of array");
     scanf("%d",&l);
    int val;

   int* arr = (int* )malloc(4 * l);

    for(int i=0;i<l;i++){
          scanf("%d",&val);
          arr[i]=val;
     }

     for(int i=0;i<l;i++){
        printf("%d",arr[i]);
     }

    free(arr);
    return 0;
}
