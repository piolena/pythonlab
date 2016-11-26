/**
        Calculate diafragma by distance and focus

**/
var diafragma = function(focus, r_max, r_centr, delta) {
        var f2 = Math.pow(focus, 2);
        var ch = r_max / (r_centr * f2) - f2;
        return ch/(delta*(r_centr - focus));
};

var calc_and_apply_to_DOM = function() {

    var formd = document.getElementById("deep");

    var focus = formd.elements["focus"].value;
    var delta = formd.elements["delta"].value;
    var r_min = formd.elements["r_min"].value;
    var r_center = formd.elements["r_center"].value;
    var r_max = formd.elements["r_max"].value;

    var result = diafragma(focus, r_max, r_center, delta);

    var dia = document.getElementById("diafragma_value");
    dia.innerHTML = (''+result).substr(0,6);
}

var update = function(el, caption_id) {
    document.getElementById(caption_id).innerHTML = el.value;
    calc_and_apply_to_DOM();
}

window.onload = function () {
    calc_and_apply_to_DOM();
};


