#!/usr/bin/env node
/* File: fourbuttons.js
 * Author: Andrew Mueller
 *
 * This file takes fur buttons and toggles four LEDs, One for each button.
 * The buttons are plugged in to GP0 while the LEDs are plugged in through GP! 
 * making use of  220 ohm resistors.
*/

//Setting up required variables
var b = require('bonescript');

var led = ["GP1_3", "GP1_4", "RED", "GREEN"];
var state = [0, 0, 0 ,0];
var prev = [1, 1, 1, 1];
var button = ["GP0_3", "GP0_4", "GP0_5", "GP0_6"];
var remap = ["GPIO1_25", "GPIO1_17", "GPIO3_20", "SPI1_CS0"];  // x.pin.name returns these names for the pins so this array lets me convert between the names used

//set pinMode
b.pinMode(led[0], b.OUTPUT);
b.pinMode(led[1], b.OUTPUT);
b.pinMode(led[2], b.OUTPUT);
b.pinMode(led[3], b.OUTPUT);

b.pinMode(button[0], b.INPUT);
b.pinMode(button[1], b.INPUT);
b.pinMode(button[2], b.INPUT);
b.pinMode(button[3], b.INPUT);

//Attaching interrups
b.attachInterrupt(button[0], toggle, b.CHANGE);  //Could potetally be changesto falling edge but that would mess with my debounce method
b.attachInterrupt(button[1], toggle, b.CHANGE);
b.attachInterrupt(button[2], toggle, b.CHANGE);
b.attachInterrupt(button[3], toggle, b.CHANGE);

//Init the leds (on)
b.digitalWrite(led[0], 0);
b.digitalWrite(led[1], 0);
b.digitalWrite(led[2], 0);
b.digitalWrite(led[3], 0);

//The interup to be used by the buttons
function toggle(x) {
  var num = remap.indexOf(x.pin.name);
  setTimeout(function(){ // debounces the button
    if (x.value == 0 && prev[num] == 1) { //checks for falling edge
      (state[num] == 0) ? state[num] = 1 : state[num] = 0;  //toggles the state
      b.digitalWrite(led[num], state[num]);  //changes the light
    }
  prev[num] = x.value;  // updates the previous value
  }, 25); 
}
