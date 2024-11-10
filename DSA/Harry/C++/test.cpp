#include<iostream>
using namespace std;


int sum(int * num){
    return *num * 2;
}


int main(){
    int a = 55;
    cout<<"size of int is "<<sizeof(int)<<endl;
    cout<<&a<<" is the address and "<<sum(&a)<<" is the value.";   
}