function loads() {
    let y = document.querySelector('.loadm');
    let z = document.querySelector('.latestx');
    var x = document.querySelector('.latesty');

    if (x.style.display == "none") {
        x.style.display = "block";
        y.innerHTML = "SHOW LESS";
        z.style.height = "200vh";


    } else {
        x.style.display = "none";
        z.style.height = "120vh";
        y.innerHTML = "SHOW MORE";
    }
}