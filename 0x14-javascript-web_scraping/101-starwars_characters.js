#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request(apiUrl, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    const movieData = JSON.parse(body);
    const charactersUrls = movieData.characters;
    
    // Function to fetch character data
    const fetchCharacterData = (charUrl) => {
      return new Promise((resolve, reject) => {
        request(charUrl, function (charError, charResponse, charBody) {
          if (!charError && charResponse.statusCode === 200) {
            const characterData = JSON.parse(charBody);
            resolve(characterData.name);
          } else {
            reject(charError || new Error('Failed to fetch character data'));
          }
        });
      });
    };

    // Fetch character data for each character URL
    Promise.all(charactersUrls.map(fetchCharacterData))
      .then((characters) => {
        characters.forEach((character) => {
          console.log(character);
        });
      })
      .catch((err) => {
        console.error('Error:', err);
      });
  } else {
    console.error('Error fetching movie data:', error);
  }
});
