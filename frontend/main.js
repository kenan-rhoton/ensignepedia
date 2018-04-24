function retorna(url) {
    var el = document.getElementById("resultat");
    if (url == "SenseResultat") {
        el.innerHTML += "No la tenim registrada";
    } else {
        el.innerHTML +=
            "<img width=250 height=auto src='" + url + "'>";
    }
}

var idx = location.href.indexOf("=");
if (idx !== -1) {
    var paraula = location.href.substring(idx+1); //agafa tot el que hi ha després del '='
    httpGetAsync(
            "http://127.0.0.1:5000/diccionari/" + paraula,
            retorna); //GET 
}

