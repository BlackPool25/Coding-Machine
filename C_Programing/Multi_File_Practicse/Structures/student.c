#include<stdio.h>

typedef struct Student{
    char name[20];
    float gpa;
}Student;

int main(){
    Student student1 = {"Shreyas", 4.0};
    Student student2 = {"Rohit", 4.2};
    Student student3 = {"Lakshmi", 3};
    Student student4 = {"Gowtham", 3.7};

    struct Student students[] = {student1, student2, student3, student4};

    for(int i = 0; i < sizeof(students)/sizeof(students[0]); i++){
        printf("%-8s : %.2f\n", students[i].name, students[i].gpa);
    }
    return 0;
}