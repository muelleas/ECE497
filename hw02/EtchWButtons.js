#!/usr/bin/env node
/* File: EtchWButtons.js
 * Author: Andrew Mueller
 *
 * This file takes inputs from four directional buttons and control an etchasketch.
 */
var b = require('bonescript');

//set up need button variables
var button = ["GP0_3", "GP0_4", "GP0_5", "GP0_6"];
var remap = ["GPIO1_25", "GPIO1_17", "GPIO3_20", "SPI1_CS0"];
var rbutton = "PAUSE";
var prev = [1,1,1,1];

//set pin modes
b.pinMode(button[0], b.INPUT);
b.pinMode(button[1], b.INPUT);
b.pinMode(button[2], b.INPUT);
b.pinMode(button[3], b.INPUT);
b.pinMode(rbutton, b.INPUT);

//Attaching interrups
b.attachInterrupt(button[0], toggle, b.CHANGE);  //Could potetally be changesto falling edge but that would mess with my debounce method
b.attachInterrupt(button[1], toggle, b.CHANGE);
b.attachInterrupt(button[2], toggle, b.CHANGE);
b.attachInterrupt(button[3], toggle, b.CHANGE);
b.attachInterrupt(rbutton, reset, b.FALLING);

// set up the etch board
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
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']];

//init the board
reset();

// functions
function reset() {
  for (i=0; i<size+1; i++){   //clear a board
    for (j=0; j<size+1; j++){
      array[i][j] = ' '; 
    }
  }
  for (i=0; i<size; i++){    //number number the edges
  	array[0][i+1] = i;
  	array[i+1][0] = i;
  }
  array[xPos][yPos] = 'o';   //place the curser
  printArray();              //print the array
}

function printArray() {
  for (i=0; i<size+1; i++){
    var string = array[i].join("");  //create the line
    console.log(string);             //print the line
  }
}

//The interup to be used by the buttons
function toggle(x) {   
  setTimeout(function(){ // debounces the button
    var num = remap.indexOf(x.pin.name);
    var print = 0;
    if (num == 0 && x.value == 0 && prev[0] == 1) { //checks for falling edge
      if (yPos > 1) yPos--;       //check bounds
      print = 1;
    }
    else if (num == 1 && x.value == 0 && prev[1] == 1) {
      if (xPos > 1) xPos--;       //check bounds
      print = 1;
    }
    else if (num == 2 && x.value == 0 && prev[2] == 1) {
      if (yPos < size) yPos++;    //check bounds
      print = 1;
    }
    else if (num == 3 && x.value == 0 && prev[3] == 1) {
      if (xPos < size) xPos++;    //check bounds
      print = 1;
    }
    prev[num] = x.value;  // updates the previous value
    array[xPos][yPos] = 'o';    //place curser
    if (print) printArray();               //print array
  }, 25); 
}
