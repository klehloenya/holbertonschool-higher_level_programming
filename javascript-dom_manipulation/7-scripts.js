// Get the ul element with id "list_movies"
const listMoviesElement = document.querySelector("#list_movies");

// Fetch data from the URL
fetch("https://swapi-api.hbtn.io/api/films/?format=json")
  .then((response) => {
    // Check if the response status is OK (200)
    if (response.ok) {
      // Parse the response JSON data
      return response.json();
    } else {
      throw new Error("Failed to fetch data");
    }
  })
  .then((data) => {
    // Extract the list of movies from the fetched data
    const movies = data.results;

    // Create an empty string to store the list items
    let moviesListHTML = "";

    // Iterate through the movies and build the list items
    movies.forEach((movie) => {
      moviesListHTML += `<li>${movie.title}</li>`;
    });

    // Set the HTML content of the ul element to the generated list
    listMoviesElement.innerHTML = moviesListHTML;
  })
  .catch((error) => {
    console.error(error);
  });