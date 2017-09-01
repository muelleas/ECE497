#include <stdio.h>
/* Etchasketch
 * Author: Andrew Mueller
 *
 * This is an Etch-a-sketch clone controlled by key strokes through the terminal.
 * */

int size = 9;  /*size of the square*/

void pArray(char array[size+1][size+1]);
void reset(char array[size+1][size+1]);
int main()
{
  printf("Welcome to the Etch-a-sketch. \nBelow is the play field. Use wasd to move around and Enter to confirm movement \nAny amount fo instruction can be entered before confirming and they will be executed in order. \nr can be used to reset to board.\n");
  char array[size+1][size+1];   /*creates array*/
  reset(array);                 /*set the array to inital position*/
  char in;                      /*Variable used for tracking cursor*/
  int posX = 1;
  int posY = 1;
  array[1][1] = 'o';
  while (1==1)
  { 
    pArray(array);                    /*shows the array*/
    scanf(" %c", &in);                /*read the used input*/
    if (in == 's' && posX < size){    /*take the input and moves the cursor*/
      posX++;
    }else if (in == 'w' && posX > 1 ){
      posX--;
    }else if (in == 'a' && posY > 1){
      posY--;
    }else if (in == 'd' && posY < size){
      posY++;
    }else if (in == 'r'){
      reset(array);
    }
    array[posX][posY] = 'o';         /*marks the location*/
  }
  return 0;
}

void reset(char array[size+1][size+1]){
  for (int i=0; i<size+1; i++) {    /*sets the whole array to be 'x'*/
    for( int j=0; j<size+1; j++) {
      array[i][j] = 'x';
    }
  }
  for(int i=0; i<size; i++) {       /*puts the numbers on the sides of the array*/
    char num = (char)(i+'0');
    array[0][i+1] = num;
    array[i+1][0] = num;
  }
}

void pArray(char array[size+1][size+1]){
  for(int i = 0; i < size+1; i++) {        /*prints the array to the terminal*/
    for(int j = 0; j < size+1; j++) {
      printf("%c ", array[i][j]);
    }
    printf("\n");
  }
  printf("\n");
}
