// Get the element with id "character"
const characterElement = document.querySelector("#character");

// Fetch data from the URL
fetch("https://swapi-api.hbtn.io/api/people/5/?format=json")
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
    // Extract the character name from the fetched data
    const characterName = data.name;

    // Display the character name in the HTML tag
    characterElement.textContent = characterName;
  })
  .catch((error) => {
    console.error(error);
  });