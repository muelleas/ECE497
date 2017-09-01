#include <stdio.h>

int size = 6;  /*size of the square*/

void pArray(int array[size+1][size+1]);
int main(int argc, char **argv)
{
  int array[size+1][size+1];
  for (int i=0; i<size+1; i++) {
    for( int j=0; j<size+1; j++) {
      array[i][j] = 0;
    }
  }
  for(int i=0; i<size;i++) {
    array[0][i+1] = i;
    array[i+1][0] = i;
  }
  
  pArray(array);
  return 0;
}

void pArray(int array[size+1][size+1]){
  for(int i = 0; i < size+1; i++) {
    for(int j = 0; j < size+1; j++) {
      printf("%d ", array[i][j]);
    }
    printf("\n");
  }
}
