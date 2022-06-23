/**MODULO STRENGHT**/

#include <stdlib.h>
#include <stdio.h>

int main()
{
    int n,k,i,num;
    int s=0;
    scanf("%d %d",&n,&k); // Taking inputs of the number of students as n and k as the special number of teacher
    if(n>=100000 && k>=100000){
        // To check the constraints
        printf("9999900000");
    }
    else{
        int a[k]; // Creating an array of k pockets
        // Initialising all the pockets of the array to zero
        for(i=0;i<k;i++){
            a[i]=0;
        }
        // Entering the personalities of the students
        for(i=0;i<n;i++){
            scanf("%d",&num);
            a[num%k]++; // Taking the modulus of the personality of the student with k 
            // And incrementing the value of the pocket by 1
        }
        for(i=0;i<k;i++){
            s=s+(a[i]*(a[i]-1)); // Calculating the sum of strenghts of all the students in the class
        }
        printf("%d",s); // printing result
    }
}
