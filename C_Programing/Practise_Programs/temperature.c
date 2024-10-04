#include<stdio.h>

int main(){
    float temp1,temp2;
    int type;
    printf("Celsius(1) or Faranheit(2): ");
    scanf("%d", &type);
    printf("Enter the temp: ");
    scanf("%f", &temp1);
    if(type == 1){
        temp2 = (temp1*(9.0/5))+32;
    }
    else if(type == 2){
        temp2 = (temp1-32)*(5.0/9);
    }
    else{
        printf("Incorrect something");
        return 0;
    }
    printf("Your converted temp is : %f\n", temp2);
    return 0;


}