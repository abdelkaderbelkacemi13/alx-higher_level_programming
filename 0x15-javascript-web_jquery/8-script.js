$.get('https://swapi.co/api/films/?format=json', function (data) {
  const movies = data.results;
  const listItems = movies.map(movie => `<li>${movie.title}</li>`);
  $('UL#list_movies').append(listItems);
});
