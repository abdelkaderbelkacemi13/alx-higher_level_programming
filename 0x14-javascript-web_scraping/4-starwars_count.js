#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (errors, responses, body) {
  if (!errors) {
    const results = JSON.parse(body).results;
    console.log(results.reduce((count, movie) => {
      return movie.characters.find((character) => character.endsWith('/18/'))
        ? count + 1
        : count;
    }, 0));
  }
});
