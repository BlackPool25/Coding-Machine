#include<stdio.h>

int main(){
    FILE *pf = fopen("C:\\Coding\\C_Programing\\Dummy_Storage\\poem.txt", "r");

    char buffer[255];

    if(pf == NULL){
        printf("Unable to open file.\n");
        return 0;
    }
    else{
        while(fgets(buffer, 255, pf) != NULL)
        {
            printf("%s", buffer);
        }
    }
    fclose(pf);
    return 0;
}