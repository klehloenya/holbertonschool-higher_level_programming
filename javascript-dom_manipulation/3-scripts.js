// Get the element with id "toggle_header"
const toggleHeaderElement = document.querySelector("#toggle_header");

// Get the header element
const headerElement = document.querySelector("header");

// Add a click event listener to the "toggle_header" element
toggleHeaderElement.addEventListener("click", function () {
  // Toggle the class between "red" and "green" on the header element
  if (headerElement.classList.contains("red")) {
    headerElement.classList.remove("red");
    headerElement.classList.add("green");
  } else {
    headerElement.classList.remove("green");
    headerElement.classList.add("red");
  }
});