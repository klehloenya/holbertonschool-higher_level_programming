// Get the element with id "update_header"
const updateHeaderElement = document.querySelector("#update_header");

// Get the header element
const headerElement = document.querySelector("header");

// Add a click event listener to the "update_header" element
updateHeaderElement.addEventListener("click", function () {
  // Update the text of the header element
  headerElement.textContent = "New Header!!!";
});