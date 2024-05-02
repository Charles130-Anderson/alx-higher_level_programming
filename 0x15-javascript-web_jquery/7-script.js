$(document).ready(function() {
  // URL to fetch the character data
  let url = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';

  // Fetch the character data
  $.get(url, function(data, status) {
    // Display the character's name in the DIV#character
    $('#character').text(data.name);
  });
});
