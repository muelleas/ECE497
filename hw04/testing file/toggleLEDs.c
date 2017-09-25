// From : http://stackoverflow.com/questions/13124271/driving-beaglebone-gpio-through-dev-mem
//
// Be sure to set -O3 when compiling.
// Modified by Mark A. Yoder  26-Sept-2013
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
    volatile void *gpio01_addr;
    volatile unsigned int *gpio01_oe_addr;
    volatile unsigned int *gpio01_setdataout_addr;
    volatile unsigned int *gpio01_cleardataout_addr;
    unsigned int reg;
    
    // Set the signal callback for Ctrl-C
	signal(SIGINT, signal_handler);

    int fd = open("/dev/mem", O_RDWR);

    printf("Mapping %X - %X (size: %X)\n", GPIO1_START_ADDR, GPIO1_END_ADDR, GPIO1_SIZE);

    gpio01_addr = mmap(0, GPIO1_SIZE, PROT_READ | PROT_WRITE, MAP_SHARED, fd, GPIO1_START_ADDR);

    gpio01_oe_addr           = gpio01_addr + GPIO_OE;
    gpio01_setdataout_addr   = gpio01_addr + GPIO_SETDATAOUT;
    gpio01_cleardataout_addr = gpio01_addr + GPIO_CLEARDATAOUT;

    if(gpio01_addr == MAP_FAILED) {
        printf("Unable to map GPIO01\n");
        exit(1);
    }

    // Set USR to be an output pin
    reg = *gpio01_oe_addr;
    printf("GPIO1 configuration: %X\n", reg);
    reg &= ~USR3;       // Set USR3 bit to 0
    reg &= ~USR2;	// Set USR2 bit to 0
    *gpio01_oe_addr = reg;
    printf("GPIO1 configuration: %X\n", reg);

    printf("Start blinking LED USR3\n");
    while(keepgoing) {
        // printf("ON\n");
        *gpio01_setdataout_addr = USR3;
	*gpio01_cleardataout_addr = USR2;
        usleep(250000);
        // printf("OFF\n");
        *gpio01_cleardataout_addr = USR3;
	*gpio01_setdataout_addr = USR2;
        usleep(250000);
    }

    munmap((void *)gpio01_addr, GPIO1_SIZE);
    close(fd);
    return 0;
}
