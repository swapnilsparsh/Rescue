// Back to top button
const backToTopButton = document.querySelector("#back-to-top-btn");
window.addEventListener("scroll", () => {
    if(window.pageYOffset > 300) { //make the button visible
        backToTopButton.style.display = "block";
    }
    else { // hide the button
        backToTopButton.style.display = "none";
    }
});

backToTopButton.addEventListener("click", () => {
    window.scrollTo(0,0);
}); 


