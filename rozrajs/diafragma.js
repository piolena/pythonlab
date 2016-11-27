/**
        Calculate diafragma by distance and focus

**/
var diafragma = function(focus, r_center, r_grip, delta) {
        var r_max =  r_center + r_grip;
        var f2 = Math.pow(focus*1000, 2);
        var ch = r_max / (r_center * f2) + f2;
        return ch/(delta*(r_center - focus))/1000/1000;
};

var calc_and_apply_to_DOM = function() {

    var formd = document.getElementById("deep");

    var focus = +formd.elements["focus"].value;
    var delta = +formd.elements["delta"].value;
    var r_center = +formd.elements["r_center"].value;
    var r_grip = +formd.elements["r_grip"].value;

    document.getElementById("r1").innerHTML = r_center - r_grip;
    document.getElementById("r2").innerHTML = r_center + r_grip;

    var result = diafragma(focus, r_center, r_grip, delta);
    document.getElementById("diafragma_value").innerHTML = (''+result).substr(0,6);
}

var update = function(el, caption_id) {
    document.getElementById(caption_id).innerHTML = el.value;
    calc_and_apply_to_DOM();
}

window.onload = function () {
    calc_and_apply_to_DOM();
};


