#!/usr/bin/node

/*
 * Write a script that prints the first argument passed to it:

If no arguments are passed to the script, print “No argument”
You must use console.log(...) to print all output
You are not allowed to use var
You are not allowed to use length
*/
console.log(typeof process.argv[2] === 'undefined' ? 'No argument' : process.argv[2]);
