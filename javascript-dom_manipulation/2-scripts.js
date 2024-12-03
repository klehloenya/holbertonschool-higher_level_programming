// Get the element with id "red_header"
const redHeaderElement = document.querySelector("#red_header");

// Add a click event listener to the "red_header" element
redHeaderElement.addEventListener("click", function () {
  // Get the header element
  const headerElement = document.querySelector("header");

  // Add the "red" class to the header element
  headerElement.classList.add("red");
});