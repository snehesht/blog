function toggleNavbar(){"block"!=document.querySelector(".navbar").style.display?document.querySelector(".navbar").style.display="block":document.querySelector(".navbar").style.display="none"}document.addEventListener("DOMContentLoaded",function(){Array.from(document.querySelectorAll(".post-content a")).forEach(function(e){console.log(e.href),e.target="_blank"})});