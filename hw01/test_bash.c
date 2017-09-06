#include <stdlib.h> 
#include <stdio.h>
#include <unistd.h>
#include <string.h>

int main(){
  int status = system("./hello");
  FILE *pFile;
  int num;
  pFile = fopen("/sys/class/leds/red/brightness","r");
  if(pFile!=NULL){
  fscanf(pFile, "%d", &num);
  fclose(pFile);
  }
  num--;
  char foo[64];
  char bar[] = " > /sys/class/leds/red/max_brightness";
  char snum[5];
  sprintf(snum, "%d", num);
  printf("%d\n", num);
  fflush(stdout);
  sprintf(foo, "%s%d%s", "echo ", num, " > /sys/class/leds/red/brightness");
  printf("s\n", foo);
  fflush(stdout);
  system(foo);
  /*while (1==1){
    status = system("echo 0 > /sys/class/leds/red/brightness");
    sleep(1);
    status = system("echo 1 > /sys/class/leds/red/brightness");
    sleep(1);
  }*/
}
