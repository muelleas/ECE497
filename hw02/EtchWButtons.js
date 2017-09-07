#!/usr/bin/env node

var b = require('bonescript');
var button = ["GP0_3", "GP0_4", "GP0_5", "GP0_6"];

b.pinMode(button[0], b.INPUT);
b.pinMode(button[1], b.INPUT);
b.pinMode(button[2], b.INPUT);
b.pinMode(button[3], b.INPUT);

//Attaching interrups
b.attachInterrupt(button[0], toggleB0, b.CHANGE);  //Could potetally be changesto falling edge but that would mess with my debounce method
b.attachInterrupt(button[1], toggleB1, b.CHANGE);
b.attachInterrupt(button[2], toggleB2, b.CHANGE);
b.attachInterrupt(button[3], toggleB3, b.CHANGE);

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
array[1][1] = 'o';
printArray();


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
}

function printArray() {
  for (i=0; i<size+1; i++){
    var string = array[i].join("");
    console.log(string);
  }
  console.log(array[0]);
}

//The interups to be used by the buttons
function toggleB0(x) {   //left
  setTimeout(function(){ // debounces the button
    if (x.value == 0 && prev[0] == 1) { //checks for falling edge
      (state[0] == 0) ? state[0] = 1 : state[0] = 0;  //toggles the state
      
    }
  prev[0] = x.value;  // updates the previous value
  }, 25); 
}

function toggleB1(x) {   //up
  setTimeout(function(){
    if (x.value == 0 && prev[1] == 1) {
      (state[1] == 0) ? state[1] = 1 : state[1] = 0;
      
    }
  prev[1] = x.value;
  }, 25); 
}

function toggleB2(x) {    //right
  setTimeout(function(){
    if (x.value == 0 && prev[2] == 1) {
      (state[2] == 0) ? state[2] = 1 : state[2] = 0;
      
    }
  prev[2] = x.value;
  }, 25); 
}

function toggleB3(x) {  //down
  setTimeout(function(){
    if (x.value == 0 && prev[3] == 1) {
      (state[3] == 0) ? state[3] = 1 : state[3] = 0;
      
    }
  prev[3]= x.value;
  }, 25); 
}
