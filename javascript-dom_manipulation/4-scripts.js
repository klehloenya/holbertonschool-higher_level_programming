// Get the element with id "add_item"
const addItemElement = document.querySelector("#add_item");

// Get the ul element with class "my_list"
const myListElement = document.querySelector(".my_list");

// Add a click event listener to the "add_item" element
addItemElement.addEventListener("click", function () {
  // Create a new li element
  const newItem = document.createElement("li");
  newItem.textContent = "Item"; // Set the text content of the new item

  // Append the new li element to the ul with class "my_list"
  myListElement.appendChild(newItem);
});