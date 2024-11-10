#include<stdio.h>

// int check_spaces(int num){
//     if(num<10){
//         return 1;
//     }
//     else if(num<100){
//         return 2;
//     }
//     else{
//         return 3;
//     }
// }


int main(){
    int size;

    printf("Enter the size: ");
    scanf("%d", &size);

    int spaces = (size-1);

    for(int i = 1;i<=size;i++){
        int k = spaces;
        while(k>0){
            printf(" ");
            k--;
        }
        int j = i;
        while(j>1){
            printf("%d", j);
            j--;
        }
        printf("1");
        j++;
        while(j<=i){
            printf("%d",j);
            j++;
        }

        printf("\n");
        spaces--;
    }

    return 0;
}