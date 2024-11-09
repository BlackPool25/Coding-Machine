#include<stdio.h>
#include<string.h>

int main(){
    int units;
    char user[20];
    float total_charge,surcharge=0;
    printf("Enter the user name: ");
    scanf("%[^\n]s", user);
    printf("Enter the units consumed: ");
    scanf("%d", &units);

    if(units<=200){
        total_charge = units * 0.8;
    }
    else if(units<=300){
        total_charge = 200 * 0.8 + (units-200) * 0.9;
    }
    else{
        total_charge = 200 * 0.8 + 100 * 0.9 + (units-300) * 1;
    }

    if (total_charge<100){
        total_charge = 100;
    }

    if(total_charge>400){
        surcharge = total_charge * 0.15;
        total_charge += surcharge;
    }

    printf("\nElectricity Bill:\n");
    printf("Name: %s\n", user);
    printf("Units Consumed: %d units\n", units);
    printf("Total Charge: Rs %.2f\n", total_charge);
    printf("Surcharge: Rs %.2f\n", surcharge);

    return 0;
}