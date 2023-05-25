// Get the buttons and the target element
var clientgridbtn = document.getElementById("client-grid-btn");
var clientlistbtn = document.getElementById("client-list-btn");
var clientgridtab = document.getElementById("client-grid-tab");
var clientlisttab = document.getElementById("client-list-tab");

clientlistbtn.addEventListener("click", function () {
  clientgridtab.classList.remove("el-tab-active");
  clientlisttab.classList.remove("el-tab-inactive");
  clientgridtab.classList.add("el-tab-inactive");
  clientlisttab.classList.add("el-tab-active");
});

clientgridbtn.addEventListener("click", function () {
  clientlisttab.classList.remove("el-tab-active");
  clientgridtab.classList.remove("el-tab-inactive");
  clientlisttab.classList.add("el-tab-inactive");
  clientgridtab.classList.add("el-tab-active");
});
