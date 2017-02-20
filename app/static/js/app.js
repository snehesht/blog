
// Nav Button Toggle
//

// Toggle the Navigation Menubar based on previous state
function toggleNavbar(){
    const screenWidth = screen.width;

    if(screenWidth > 767){
        if (document.querySelector('#navbar-desktop').style.display == "none"){
            document.querySelector("#navbar-desktop").style.display = "block"
            localStorage.setItem('menu',1);
        } else {
            document.querySelector("#navbar-desktop").style.display = "none"
            localStorage.setItem('menu',0);
        }
    } else {
        if (document.querySelector('#navbar-mobile').style.display == "none"){
            document.querySelector("#navbar-mobile").style.display = "block"
            localStorage.setItem('menu',1);
        } else {
            document.querySelector("#navbar-mobile").style.display = "none"
            localStorage.setItem('menu',0);
        }
    }
}

// Attach an EventListener to the "Menu" icon, to listen for mouse clicks
document.querySelector("#navbutton").addEventListener( "click", function() {
    this.classList.toggle("open");
    toggleNavbar();
});


// Execute the script once the webpage is loaded
document.addEventListener('DOMContentLoaded', function() {
    var menu = localStorage.getItem('menu');
    if(menu != null){
            if(menu == 1){
                document.querySelector("#navbutton").classList.toggle("open");
                toggleNavbar();
            }
    } else {
        localStorage.setItem('menu',0);
    }
});

// Adding target="_blank" to <a href=""></a> URL's in the blogpost
Array.from(document.querySelectorAll(".content a")).forEach(function (a) {
  a.target = "_blank";
});
