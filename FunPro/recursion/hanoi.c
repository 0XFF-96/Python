* file name: hannoi.c

#include <stdio.h>

void move_singel_disk(int dist, char src, char dest)
{
	static step=1;
	fprintf(stdout, "step%d: disk%d %c -- %c \n", step++,disk,src,dest);
}

void hannoi(int n, int disk, char A, char B, char c)
{

	// bash situation
	if (1 == n){

		move_single_disk(disk, A, c);
	}
	else{
		// problem 1
		hanoi(n-1, disk -1, A, C, B);
		
		//solve problem 2
		hanoi(1, disk, A, B, C);

		//solve problem3
		hanoi(n-1, disk-1, B, A, C);
	}
}

int main(int argc, char *argv[])
{
	int n = atoi(argv[1]);
	fprintf(stdout, "======hanoi(%d): \n", n);

	hanoi(n,n,'A','B','C');
	fprintf(stdout,"======hannoi finished\n");
	
	return 0;
}



	


