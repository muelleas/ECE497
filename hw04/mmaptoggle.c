// From : http://stackoverflow.com/questions/13124271/driving-beaglebone-gpio-through-dev-mem
// File mmaptoggle.c
// Author: Andrew Mueller
//
// This file takes two bvuttons on GPIO4 and two leds on GPIO1 and when the buttons are pressed the LEDs toggle on and off.


#include <stdio.h>
#include <stdlib.h>
#include <sys/mman.h>
#include <sys/stat.h>
#include <fcntl.h> 
#include <signal.h>    // Defines signal-handling functions (i.e. trap Ctrl-C)
#include "beaglebone_gpio.h"

/****************************************************************
 * Global variables
 ****************************************************************/
int keepgoing = 1;    // Set to 0 when ctrl-c is pressed

/****************************************************************
 * signal_handler
 ****************************************************************/
void signal_handler(int sig);
// Callback called when SIGINT is sent to the process (Ctrl-C)
void signal_handler(int sig)
{
	printf( "\nCtrl-C pressed, cleaning up and exiting...\n" );
	keepgoing = 0;
}

int main(int argc, char *argv[]) {
    //GPIO1 variables
    volatile void *gpio1_addr;
    volatile unsigned int *gpio1_oe_addr;
    volatile unsigned int *gpio1_setdataout_addr;
    volatile unsigned int *gpio1_cleardataout_addr;
    //GPIO3 variables
    volatile void *gpio3_addr;
    volatile unsigned int *gpio3_oe_addr;
    volatile unsigned int *gpio3_datain;
    
    unsigned int reg;
    
    // Set the signal callback for Ctrl-C
	signal(SIGINT, signal_handler);

    int fd = open("/dev/mem", O_RDWR);

    printf("Mapping %X - %X (size: %X)\n", GPIO1_START_ADDR, GPIO1_END_ADDR, GPIO1_SIZE);

    gpio1_addr = mmap(0, GPIO1_SIZE, PROT_READ | PROT_WRITE, MAP_SHARED, fd, GPIO1_START_ADDR);
    gpio3_addr = mmap(0, GPIO3_SIZE, PROT_READ | PROT_WRITE, MAP_SHARED, fd, GPIO3_START_ADDR);

    gpio1_oe_addr           = gpio1_addr + GPIO_OE;
    gpio1_setdataout_addr   = gpio1_addr + GPIO_SETDATAOUT;
    gpio1_cleardataout_addr = gpio1_addr + GPIO_CLEARDATAOUT;
    
    gpio3_oe_addr           = gpio3_addr + GPIO_OE;
    gpio3_datain	    = gpio3_addr + GPIO_DATAIN;

    if(gpio1_addr == MAP_FAILED) {
        printf("Unable to map GPIO1\n");
        exit(1);
    }
    if(gpio3_addr == MAP_FAILED) {
        printf("Unable to map GPIO3\n");
        exit(1);
    }

    printf("running:");

    // Set USR3 to be an output pin
    while(keepgoing) {
	if(*gpio3_datain & GPIO_20) {  // if gpio3_20 is pushed
		*gpio1_setdataout_addr = USR3;  //turn on led
	} else {
		*gpio1_cleardataout_addr = USR3;  // turn off led
	}
	if(*gpio3_datain & GPIO_17) {  // if gpio3_17 is pushed
		*gpio1_setdataout_addr = USR2;  // turn on led
	} else {
		*gpio1_cleardataout_addr = USR2; //turn off led
	}
    }

    munmap((void *)gpio1_addr, GPIO1_SIZE);
    munmap((void *)gpio3_addr, GPIO3_SIZE);
    close(fd);
    return 0;
}
