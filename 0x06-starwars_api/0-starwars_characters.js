#!/usr/bin/node
// star wars api

const request = require('request');
const { promisify } = require('util');
const asyncRequestGet = promisify(request.get);

const film = process.argv[2];

const apiUrl = `https://swapi-api.alx-tools.com/api/films/${film}`; // Example REST API endpoint

// Making a GET request
request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else {
    try {
      const parsedBody = JSON.parse(body);

      // Accessing the character value
      const characters = parsedBody.characters;

      // retrieving the name of characters in film
      async function fetchCharacters () {
        for (const item of characters) {
          try {
            const charApi = item;
            const response = await asyncRequestGet(charApi);

            const parsedBody = JSON.parse(response.body);
            const name = parsedBody.name;
            console.log(name);
          } catch (error) {
            console.error('Error:', error);
          }
        }
      }

      fetchCharacters();
    } catch (parseError) {
      console.error('JSON Parse Error:', parseError);
    }
  }
});
