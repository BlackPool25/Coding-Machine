#include<stdio.h>

enum Day{Sun, Mon, Tue, Wed, Thu, Fri, Sat};

int main(){
    enum Day today = Sat;

    if(today == Sun || today == Sat){
        printf("\nIt's the weekend! Party time!");
    }
    else{
        printf("\nI have to work today :(");
    }
    return 0;
}