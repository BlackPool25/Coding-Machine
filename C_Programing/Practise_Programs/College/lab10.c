#include<stdio.h> 
#include<math.h> 
void main() 
{ 
float x[20],mean,sum=0,*p,sd,var; 
int n,i; 
printf("enter the size of array\n"); 
scanf("%d",&n); 
printf("enter %d elements\n",n); 
for(i=0;i<n;i++) 
scanf("%f",&x[i]); 
p=x; 
for(i=0;i<n;i++) 
{ 
sum=sum+(*p); 
p=p++; 
} 
mean=sum/n; 
printf("sum of %d elements=%f\n",n,sum); 
printf("mean of %d elements=%f\n",n,mean); 
sum=0; 
p=x;   /* updating the pointer to point to the first element*/ 
for(i=0;i<n;i++) 
{ 
sum=sum+pow((*p-mean),2); 
p=p++; 
} 
var=sum/n; 
printf("varience=%f\n",var); 
sd=sqrt(var); 
printf("standard deviation of %d elements=%f\n",n,sd); 
} 