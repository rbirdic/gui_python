#include <wiringPi.h>

#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

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
   int oldValue, calculatedValue, index;
   int message[30] = {[0 ... 29] = 0};
   wiringPiSetup();
   pinMode( RS, INPUT );
   pinMode( RW, INPUT );
   pinMode( EN, INPUT );
   pinMode( BIT0, INPUT );
   pinMode( BIT1, INPUT );
   pinMode( BIT2, INPUT ); 
   pinMode( BIT3, INPUT );
   pinMode( BIT4, INPUT );
   pinMode( BIT5, INPUT );
   pinMode( BIT6, INPUT );
   pinMode( BIT7, INPUT );

   oldValue = 0;
   calculatedValue = 0;
   index = 0;	
   
   while(1){
       if(digitalRead(EN) == 1 && digitalRead(RS) == 1){
		calculatedValue = digitalRead(BIT0) + 2*digitalRead(BIT1) + 4*digitalRead(BIT2) + 8*digitalRead(BIT3) + 16*digitalRead(BIT4) + 32*digitalRead(BIT5) + 64*digitalRead(BIT6) + 128*digitalRead(BIT7);
		if(oldValue != calculatedValue){
				
			if((calculatedValue > 64 && calculatedValue < 91) || (calculatedValue > 96 && calculatedValue < 123) || calculatedValue == 32){
				//message[index] = calculatedValue;
				index++;
				printf("%c", calculatedValue);
				fflush(stdout);
				oldValue = calculatedValue;
			}
			if(calculatedValue == 32){
				printf("\tIndex: %d\n", index);
			}
		}
	/*for(int i = 0; i < index; i++){
			printf("%c", message[i]);
			}*/
		
	}
			
   }
   return(0);
}