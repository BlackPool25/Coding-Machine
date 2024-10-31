#include<stdio.h>
int main(){
    int arr[] = {1, 2, 3},i;
    for(i = 0; i<(sizeof(arr)/sizeof(arr[0])); i++)
    printf("%d\t", arr[i]);

    return 0;
}