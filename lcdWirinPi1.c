#include <wiringPi.h>

#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

//pinList = [7,11,13,15,19,21,23,29,31,33,35]

#define RS 7    //GPIO 7
#define RW 0	//GPIO 11
#define EN 2	//GPIO 13		
#define BIT0 3	//GPIO 15
#define BIT1 12	//GPIO 19
#define BIT2 13 //GPIO 21
#define BIT3 14 //GPIO 23
#define BIT4 21 //GPIO 29
#define BIT5 22 //GPIO 31
#define BIT6 23 //GPIO 33
#define BIT7 24 //GPIO 35





main()
{
   FILE *f1, *fopen();
   //char testbit, dht11_dat[samples];
   f1 = fopen("results.txt", "w+");
   int i;
   int old, sum;
   wiringPiSetup();
   delay (500);
   pinMode( RS, INPUT );
   pinMode( RW, INPUT );
   pinMode( EN, INPUT );
   pinMode( BIT0, INPUT );
   pinMode( BIT1, INPUT );
   pinMode( BIT2, INPUT ); 
   pinMode( BIT3, INPUT );
   pinMode( BIT4, INPUT ); //NA 1 je
   pinMode( BIT5, INPUT ); //NA 1 je
   pinMode( BIT6, INPUT );
   pinMode( BIT7, INPUT );
   pullUpDnControl(BIT2, PUD_DOWN);

   old = 0;
   
   while(1){
	//if (old == 1 & GPIO.input(pinList[0]) == 1 & GPIO.input(pinList[1]) == 1 & GPIO.input(pinList[2]) == 0)
	//if(digitalRead(BIT3) == 0){
		//printf("Cao!");
	//}*/
	sum = 0;
	if(digitalRead(BIT0)+ digitalRead(BIT1) + digitalRead(BIT2) + digitalRead(BIT3) + digitalRead(BIT4) + digitalRead(BIT5) + digitalRead(BIT6) + digitalRead(BIT7) != 0){
	printf(" old : %d, RS : %d, RW : %d, EN : %d\n", old, digitalRead(RS), digitalRead(RW), digitalRead(EN));
	//printf(" old : %d, RS : %d, RW : %d, EN : %d\n", old, analogRead(RS), analogRead(RW), analogRead(EN));
	sum = digitalRead(BIT0)+ 2*digitalRead(BIT1) + 4*digitalRead(BIT2) + 8*digitalRead(BIT3) + 16*digitalRead(BIT4) + 32*digitalRead(BIT5) + 64*digitalRead(BIT6) + 128*digitalRead(BIT7);
	//printf(" %d%d%d%d%d%d%d%d \n", digitalRead(BIT0), digitalRead(BIT1), digitalRead(BIT2), digitalRead(BIT3), 
	//			       digitalRead(BIT4), digitalRead(BIT5), digitalRead(BIT6), digitalRead(BIT7));
	//fprintf(f1, " %d%d%d%d%d%d%d%d \n", digitalRead(BIT0), digitalRead(BIT1), digitalRead(BIT2), digitalRead(BIT3), 
	//			       digitalRead(BIT4), digitalRead(BIT5), digitalRead(BIT6), digitalRead(BIT7));
	printf("Sum : %d, ascii : %c\n", sum, sum);
	fprintf(f1, "Sum : %d ascii : %c\n", sum, sum);
	//fprintf(f1, "RS : %d, RW : %d, EN : %d\n", old, digitalRead(RS), digitalRead(RW), digitalRead(EN));
	}
	if(old == 1 && digitalRead(RS) == 0  && digitalRead(RW) == 1 && digitalRead(EN) == 0){
	//if(digitalRead(EN) == 0){
		if(digitalRead(BIT0) == 1) {
			sum += 1;
			}
		if(digitalRead(BIT1) == 1) {
			sum += 2;
			}
		if(digitalRead(BIT2) == 1) {
			sum += 4;
			}
		if(digitalRead(BIT3) == 1) {
			sum += 8;
			}
		if(digitalRead(BIT4) == 1) {
			sum += 16;
			}
		if(digitalRead(BIT5) == 1) {
			sum += 32;
			}
		if(digitalRead(BIT6) == 1) {
			sum += 64;
			}
		if(digitalRead(BIT7) == 1) {
			sum += 128;
			}
		printf("Suma je :%d\n", sum);
		old = digitalRead(EN);
		
		
	}
		
  	}

   fclose(f1);
   return(0);
}