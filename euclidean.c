#include<stdio.h>

int euclidean(int *a, int *b){

	int quotient = *a / *b; 
	int remainder = *a % *b;
	
	*a = *b; //update the value 
	*b = remainder;

}


void main(){

int a,b;

printf("enter a value:");
scanf("%d",&a);
printf("enter b value:");
scanf("%d",&b);

while(1){

	if(a == 0){
		printf("the GCD is %d\n", b);
		break;
	}else if(b == 0){
		printf("the GCD is %d\n", a);
		break;
	}else{
		euclidean(&a,&b); //c cannot return multiple return value so you 
				// should use pointer to update the value of the variable
	}
}

}
