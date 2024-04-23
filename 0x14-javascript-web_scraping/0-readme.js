#!/usr/bin/node

/*
 *  a script that reads and prints the content of a file.
 *  1. The first argument is the file path
 *  2. The content of the file must be read in utf-8
 *  If an error occurred during the reading, print the error object
 */

const fs = require('fs'); /* load the fs modole */

const process = require('process'); /* loads the process to access argv */

const filePath = process.argv[2] /* gets the path of the file o read */

fs.readFile (filePath, 'utf-8', (err, data) => {
	if (err) {
		console.error(err);
	}
	else {
		console.log(data);
	}
});
