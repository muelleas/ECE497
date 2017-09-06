#!/usr/bin/env node
var b = require('bonescript');

var button = "GP0_3";
var LED = "GP0_5";

b.pinMode(button, b.INPUT);
b.pinMode(LED, b.OUTPUT);

b.attachInterrupt(button, toggle, b.CHANGE);
var state = 0;
var prev = 1;

function toggle(x) {
  console.log("push");
  setTimeout(function(){
    if (x.value == 0 && prev == 1) {
      (state == 0) ? state = 1 : state = 0;
      b.digitalWrite(LED, state);
    }
  prev = x.value;
  }, 25); 
}
