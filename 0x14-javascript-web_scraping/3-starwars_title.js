#!/usr/bin/node

/*
 * script that prints the title of a Star Wars movie
 * where the episode number matches a given integer.
 * 1. The first argument is the movie ID
 * 2. You must use the Star wars API with the endpoint h
 * 3. You must use the module request
 */
const request = require('request'); /* importing the request module */
const movieId = process.argv[2]; /* used to get the movie id from the command line */
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;
request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const data = JSON.parse(body);
    console.log(data.title);
  }
});
