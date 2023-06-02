// Get the buttons and the target element
var clientgridbtn = document.getElementById("client-grid-btn");
var clientlistbtn = document.getElementById("client-list-btn");
var clientgridtab = document.getElementById("client-grid-tab");
var clientlisttab = document.getElementById("client-list-tab");

// Add event listener to client list button
clientlistbtn.addEventListener("click", function () {
  clientlisttab.classList.replace("el-tab-inactive", "el-tab-active");
  clientgridtab.classList.replace("el-tab-active", "el-tab-inactive");

  // Store the current state in localStorage
  localStorage.setItem("activeTab", "list");
});

// Add event listener to client grid button
clientgridbtn.addEventListener("click", function () {
  clientgridtab.classList.replace("el-tab-inactive", "el-tab-active");
  clientlisttab.classList.replace("el-tab-active", "el-tab-inactive");

  // Store the current state in localStorage
  localStorage.setItem("activeTab", "grid");
});

// Retrieve the state from localStorage when the page loads
window.addEventListener("load", function () {
  const activeTab = localStorage.getItem("activeTab");

  // Check if there is a stored state and apply it
  if (activeTab === "list") {
    clientlisttab.classList.replace("el-tab-inactive", "el-tab-active");
    clientgridtab.classList.replace("el-tab-active", "el-tab-inactive");
  } else if (activeTab === "grid") {
    clientgridtab.classList.replace("el-tab-inactive", "el-tab-active");
    clientlisttab.classList.replace("el-tab-active", "el-tab-inactive");
  }
});

const tooltipTriggerList = document.querySelectorAll(
  '[data-bs-toggle="tooltip"]'
);
const tooltipList = [...tooltipTriggerList].map(
  (tooltipTriggerEl) => new bootstrap.Tooltip(tooltipTriggerEl)
);

const myModal = document.getElementById("createClient");
const myInput = document.getElementById("myInput");

myModal.addEventListener("shown.bs.modal", () => {
  myInput.focus();
});
