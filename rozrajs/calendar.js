/**
        Update current date and time every second

**/

function update_calendar() {
    document.getElementById("current_date").innerHTML = new Date().toLocaleDateString();
    document.getElementById("current_time").innerHTML = new Date().toLocaleTimeString();
}
