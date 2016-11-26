
var noway = function(el) {
    el.style['margin-top'] = 50 + "px";
}

var show = function(el) {
    el.style['margin-top'] = "0px";
}

var bw_image = function(img_id) {
    var img = document.getElementById(img_id);

    if (img.className.indexOf('grayscale') < 0 ) {
        img.className += " grayscale";
    } else {
        img.classList.remove('grayscale');
    }
}