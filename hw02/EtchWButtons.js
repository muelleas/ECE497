#!/usr/bin/env node

var b = require('bonescript');
var button = ["GP0_3", "GP0_4", "GP0_5", "GP0_6"];
var rbutton = "PAUSE";
var prev = [1,1,1,1];

b.pinMode(button[0], b.INPUT);
b.pinMode(button[1], b.INPUT);
b.pinMode(button[2], b.INPUT);
b.pinMode(button[3], b.INPUT);
b.pinMode(rbutton, b.INPUT);

//Attaching interrups
b.attachInterrupt(button[0], toggleB0, b.CHANGE);  //Could potetally be changesto falling edge but that would mess with my debounce method
b.attachInterrupt(button[1], toggleB1, b.CHANGE);
b.attachInterrupt(button[2], toggleB2, b.CHANGE);
b.attachInterrupt(button[3], toggleB3, b.CHANGE);
b.attachInterrupt(rbutton, reset, b.CHANGE);

var size = 8;
var xPos = 1;
var yPos = 1;
var array = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]


reset();

function reset() {
  for (i=0; i<size+1; i++){
    for (j=0; j<size+1; j++){
      array[i][j] = ' ';
    }
  }
  for (i=0; i<size; i++){
  	array[0][i+1] = i;
  	array[i+1][0] = i;
  }
  array[xPos][yPos] = 'o';
  printArray();
}

function printArray() {
  for (i=0; i<size+1; i++){
    var string = array[i].join("");
    console.log(string);
  }
}

//The interups to be used by the buttons
function toggleB0(x) {   //left
  setTimeout(function(){ // debounces the button
    if (x.value == 0 && prev[0] == 1) { //checks for falling edge
      if (yPos > 1) yPos--;
      array[xPos][yPos] = 'o';
      printArray();
    }
  prev[0] = x.value;  // updates the previous value
  }, 25); 
}

function toggleB1(x) {   //up
  setTimeout(function(){
    if (x.value == 0 && prev[1] == 1) {
      if (xPos > 1) xPos--;
      array[xPos][yPos] = 'o';
      printArray();
    }
  prev[1] = x.value;
  }, 25); 
}

function toggleB2(x) {    //right
  setTimeout(function(){
    if (x.value == 0 && prev[2] == 1) {
      if (yPos < size) yPos++;
      array[xPos][yPos] = 'o';
      printArray();
    }
  prev[2] = x.value;
  }, 25); 
}

function toggleB3(x) {  //down
  setTimeout(function(){
    if (x.value == 0 && prev[3] == 1) {
      if (xPos < size) xPos++;
      array[xPos][yPos] = 'o';
      printArray();
    }
  prev[3]= x.value;
  }, 25); 
}
