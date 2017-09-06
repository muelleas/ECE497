#!/usr/bin/env node
var b = require('bonescript');

var led = ["GP1_3", "GP1_4", "GP1_5", "GP1_6"];
var state = [0, 0, 0 ,0]
var button = ["GP0_4", "GP0_4", "GP0_5", "GP0_6"];

//set pinMode
//b.pinMode(led[0], b.OUTPUT);
//b.pinMode(led[1], b.OUTPUT);
//b.pinMode(led[2], b.OUTPUT);
//b.pinMode(led[3], b.OUTPUT);

b.pinMode(button[0], b.INPUT);
//b.pinMode(but[1], b.INPUT);
//b.pinMode(but[2], b.INPUT);
//b.pinMode(but[3], b.INPUT);

//b.attachInterrupt(but[0], toggle(0), b.RISING);
//b.attachInterrupt(but[1], toggle(1), b.RISING);
//b.attachInterrupt(but[2], toggle(2), b.RISING);
//b.attachInterrupt(but[3], toggle(3), b.RISING);

// Init
for (i = 0; i < 4; i++) {
  //b.digitalWrite(led[0], state[0]);
}


function main() {
    console.log(button[0].digitalRead());
}

function toggle(x) {
  console.log("push" + x);
}
