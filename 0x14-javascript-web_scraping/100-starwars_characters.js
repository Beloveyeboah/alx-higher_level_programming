#!/usr/bin/node
/**
 *  script that prints all characters of a Star Wars movie:
 *  The first argument is the Movie ID - example: 3 = “Return of the Jedi”
 *  Display one character name by line
 *  You must use the Star wars API
 *  You must use the module request
 **/
const movieId = process.argv[2];
const request = require('request'); /* import the request module */
const url = `https://swapi.dev/api/films/${movieId}/`; /* star wars api url */

request(url, { json: true }, (err, response, body) => {
  if (err) {
    console.log(err);
    return;
  }
  const charactersUrl = body.characters;
  charactersUrl.forEach(url => {
    request(url, { json: true }, (error, res, content) => {
      if (error) {
        console.log(error);
        return;
      }
      console.log(content.name);
    });
  });
});
