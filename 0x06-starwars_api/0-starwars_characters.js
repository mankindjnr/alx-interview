#!/usr/bin/node

const request = require('request');

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
      const numChar = characters.length;

      // retrieving the name of characters in film
      for (let i = 0; i < numChar; i++) {
        const charApi = characters[i];
        request.get(charApi, (error, response, body) => {
          if (error) {
            console.error('Error:', error);
          } else {
            const parsedBody = JSON.parse(body);
            const name = parsedBody.name;
            console.log(name);
          }
        });
      }
    } catch (parseError) {
      console.error('JSON Parse Error:', parseError);
    }
  }
});
