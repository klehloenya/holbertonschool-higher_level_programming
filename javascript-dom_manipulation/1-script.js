// Get the element with id "red_header"
const redHeaderElement = document.querySelector("#red_header");

// Add a click event listener to the "red_header" element
redHeaderElement.addEventListener("click", function () {
  // Get the header element
  const headerElement = document.querySelector("header");

  // Update the text color of the header element to red (#FF0000)
  headerElement.style.color = "#FF0000";
});