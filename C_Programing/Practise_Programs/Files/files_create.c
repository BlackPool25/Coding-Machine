#include<stdio.h>

int main(){
    FILE *pf = fopen("C:\\Coding\\C_Programing\\Dummy_Storage\\files_creation.txt", "a");

    if(fprintf(pf, "\nRekha Joshi") >= 0){
        printf("Done successfully.");
    }

    fclose(pf);
    
}