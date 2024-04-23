#!/usr/bin/node

/*
 *  a script that writes a string to a file.
 *  1. The first argument is the file path
 *  The second argument is the string to write
 *  2. The content of the file must be written in utf-8
 *  If an error occurred during the writting, print the error object
 */
const fs = require('fs'); /* load the fs modole */
const filename = process.argv[2]; /* loads the process to access argv */
const content = process.argv[3];

fs.writeFile(filename, content, { encoding: 'utf-8' }, (err) => {
  if (err) {
    console.error(err);
  }
});
