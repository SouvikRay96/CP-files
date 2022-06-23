#include <stdio.h>
#include <math.h>
#include<string.h>
#include<stdlib.h>
int main(){
	int n, t;
	scanf("%d", &t);
	int result[t];
	for(int i=1; i<=t; i++){
    	// for each testcase
        scanf("%d", &n);
		char arr[n][n+1];
		int mid = floor(n/2);
		int pos_v , pos_h, total_step;
		//input + scaning '*'
		for(int j=0; j<n; j++){
			// printf("outer loop\n");
			scanf("%s", &arr[j]);
			for(int k=0; k<strlen(arr[j]); k++){
				// printf("inner loop\n");
				//scanf("%c", &arr[j][k]);
				if(arr[j][k] == '*'){
					pos_h = j;
					pos_v = k;
                }
			}
		}
        total_step = abs(mid - pos_h) + abs(mid - pos_v);
        result[i-1] = total_step;
	}

	for(int i=0; i<t; i++){
		printf("%d\n", result[i]);
	}
    return 0;
}
