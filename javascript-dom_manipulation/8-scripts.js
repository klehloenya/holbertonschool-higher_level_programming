// Wait for the DOM to be fully loaded
document.addEventListener("DOMContentLoaded", function () {
    // Get the element with id "hello"
    const helloElement = document.querySelector("#hello");
  
    // Fetch data from the URL
    fetch("https://hellosalut.stefanbohacek.dev/?lang=fr")
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
        // Get the translation of "hello" from the fetched data
        const translation = data.hello;
  
        // Display the translation in the HTML element
        helloElement.textContent = translation;
      })
      .catch((error) => {
        console.error(error);
      });
  });
  