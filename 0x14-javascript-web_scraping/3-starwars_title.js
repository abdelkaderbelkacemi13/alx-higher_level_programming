#!/usr/bin/node

const request = require('request');
const swEpNumber = process.argv[2];
const baseUrl = 'https://swapi-api.hbtn.io/api/films/';

request(baseUrl + swEpNumber, function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    const responseJSON = JSON.parse(body);
    console.log(responseJSON.title);
  } else {
    console.log('Error code: ' + response.statusCode);
  }
});
