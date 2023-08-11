const request = require('request');

const apiUrl = 'https://swapi-api.alx-tools.com/api/films/3'; // Example REST API endpoint

// Making a GET request
request.get(apiUrl, (error, response, body) => {
    if (error) {
        console.error('Error:', error);
    } else {
        try {
            const parsedBody = JSON.parse(body);

            // Accessing the character value
            const characters = parsedBody.characters;
            const num_char = characters.length;

            // retrieving the name of characters in film
            for (let i = 0; i < num_char; i++){
                const charApi = characters[i];
                request.get(charApi, (error, response, body) => {
                    if (error) {
                        console.error('Error:', error);
                    } else {
                        const parsedBody = JSON.parse(body);
                        const name = parsedBody.name
                        console.log(name)
                    }
                });
            }

        } catch (parseError) {
            console.error('JSON Parse Error:', parseError);
        }
    }
});
