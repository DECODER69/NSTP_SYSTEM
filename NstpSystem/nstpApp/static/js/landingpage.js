<<<<<<< HEAD
var a = true;


function loads() {
    console.log("saqui");
    let y = document.querySelector('.loadm');
    let z = document.querySelector('.latestx');
    var x = document.getElementById("card-deck1");
    if (a) {
        x.style.display = "block";
        y.innerHTML = "SHOW LESS";
        z.style.height = 1500 + 'px';
        console.log("saqui2");
        a = false;
=======
function loads() {
    let y = document.querySelector('.loadm');
    let z = document.querySelector('.latestx');
    var x = document.querySelector('.latesty');

    if (x.style.display == "none") {
        x.style.display = "block";
        y.innerHTML = "SHOW LESS";
        z.style.height = "200vh";
>>>>>>> db7afe168e6d0af4020469237ef6ab17cf4df33e


    } else {
        x.style.display = "none";
        z.style.height = "120vh";
        y.innerHTML = "SHOW MORE";
<<<<<<< HEAD
        console.log("saqui3");
        a = true;
=======
>>>>>>> db7afe168e6d0af4020469237ef6ab17cf4df33e
    }
}