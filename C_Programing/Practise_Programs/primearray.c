#include<stdio.h>
#include<stdbool.h>
#include<math.h>

bool is_prime(int);


bool is_prime(int num){
    for(int i = 2; i< sqrt(num); i++){
        if(num % i ==0){
            return false;
        }
    }
    return true;
}

int main(){
    int prime_arr[100];
    int current_num = 2;
    int array_loc = 0;
    for(int j=0;j<100;){
        if(is_prime(current_num)){
            prime_arr[array_loc] = current_num;
            array_loc++;
            current_num++;
            j++;
        }
        else{
            current_num++;
        }
    }
    for(int i = 0;i<100;i++){
        printf("%d ", prime_arr[i]);
    }
    return 0;
}