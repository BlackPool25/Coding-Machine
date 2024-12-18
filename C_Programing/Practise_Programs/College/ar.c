#include<stdio.h>

int main(){
    int arr[5];
    printf("Enter the elements: ");
    for(int i=1;i<=5;i++){
        scanf("%d", &arr[i]);
    }

    for(int i=1;i<=5;i++){
        printf("%d\n", arr[i]);
    }

    return 0;    
}