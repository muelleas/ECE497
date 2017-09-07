#!/usr/bin/env node
var b = require('bonescript');

var led = ["GP1_3", "GP1_4", "RED", "GREEN"];
var state = [0, 0, 0 ,0];
var prev = [1, 1, 1, 1];
var button = ["GP0_3", "GP0_4", "GP0_5", "GP0_6"];

//set pinMode
b.pinMode(led[0], b.OUTPUT);
b.pinMode(led[1], b.OUTPUT);
b.pinMode(led[2], b.OUTPUT);
b.pinMode(led[3], b.OUTPUT);

b.pinMode(button[0], b.INPUT);
b.pinMode(button[1], b.INPUT);
b.pinMode(button[2], b.INPUT);
b.pinMode(button[3], b.INPUT);

b.attachInterrupt(button[0], toggleB0, b.CHANGE);
b.attachInterrupt(button[1], toggleB1, b.CHANGE);
b.attachInterrupt(button[2], toggleB2, b.CHANGE);
b.attachInterrupt(button[3], toggleB3, b.CHANGE);

b.digitalWrite(led[0], 0);
b.digitalWrite(led[1], 0);
b.digitalWrite(led[2], 0);
b.digitalWrite(led[3], 0);

function toggleB0(x) {
  console.log("0");
  setTimeout(function(){
    if (x.value == 0 && prev[0] == 1) {
      (state[0] == 0) ? state[0] = 1 : state[0] = 0;
      b.digitalWrite(led[0], state[0]);
    }
  prev[0] = x.value;
  }, 25); 
}

function toggleB1(x) {
  console.log("1");
  setTimeout(function(){
    if (x.value == 0 && prev[1] == 1) {
      (state[1] == 0) ? state[1] = 1 : state[1] = 0;
      b.digitalWrite(led[1], state[1]);
    }
  prev[1] = x.value;
  }, 25); 
}

function toggleB2(x) {
  console.log("2");
  setTimeout(function(){
    if (x.value == 0 && prev[2] == 1) {
      (state[2] == 0) ? state[2] = 1 : state[2] = 0;
      b.digitalWrite(led[2], state[2]);
    }
  prev[2] = x.value;
  }, 25); 
}

function toggleB3(x) {
  console.log("3");
  setTimeout(function(){
    if (x.value == 0 && prev[3] == 1) {
      (state[3] == 0) ? state[3] = 1 : state[3] = 0;
      b.digitalWrite(led[3], state[3]);
    }
  prev[3]= x.value;
  }, 25); 
}
