#!/usr/bin/node

/*
 *  a script that prints the number of movies where the
 *  character “Wedge Antilles” is present.
 *  1. The first argument is the API URL
 *  2. Wedge Antilles is character ID 18 -
 *  3.  You must use the module request
 */
const movieCharacterId = '18';
let countMovies = 0;
const request = require('request'); /* importing the request module */
const url = process.argv[2]; /* used to get the url  from the command line */

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const data = JSON.parse(body);
    data.results.forEach((film) => {
      film.characters.forEach((character) => {
        if (character.includes(movieCharacterId)) {
          countMovies = countMovies + 1;
        }
      });
    });
    console.log(countMovies);
  }
});
