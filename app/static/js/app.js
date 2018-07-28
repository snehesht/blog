
// Nav Button Toggle
//


// Toggle the Navigation Menubar based on previous state
function toggleNavbar() {
    if (document.querySelector('.navbar').style.display != "block") {
        document.querySelector(".navbar").style.display = "block"
    } else {
        document.querySelector(".navbar").style.display = "none"
    }
}

// Attach an EventListener to the "Menu" icon, to listen for mouse clicks
// document.querySelector("#mobile-menu").addEventListener("click", function () {
//     console.log('Clicked Menu')
//     // this.classList.toggle("open");
//     // toggleNavbar();
// });


// Execute the script once the webpage is loaded
document.addEventListener('DOMContentLoaded', function () {
    Array.from(document.querySelectorAll(".post-content a")).forEach(function (a) {
        console.log(a.href)
        a.target = "_blank";
    });
});

// Adding target="_blank" to <a href=""></a> URL's in the blogpost
// Array.from(document.querySelectorAll(".content a")).forEach(function (a) {
//     a.target = "_blank";
// });
