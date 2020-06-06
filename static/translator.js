

function changeLanguage(){
    var a = document.getElementById("selectedlanguage").value;
    var x = document.getElementById("bahasa-asal"); 
    var y = document.getElementById("bahasa-tujuan");
    if (a === "is") { 
        x.innerHTML = "Bahasa Indonesia"; 
        y.innerHTML = "Bahasa Sunda";
    }else { 
        x.innerHTML = "Bahasa Sunda"; 
        y.innerHTML = "Bahasa Indonesia";
    } 
} 

function postData(){
    let url ="/process?"
    let daribahasa = document.getElementById("daribahasa").value;
    let lang = document.getElementById("selectedlanguage").value;
    let e = document.getElementById("selected");
    let algoritma = e.options[e.selectedIndex].value;
    url = url + "daribahasa=" + daribahasa + "&algoritma=" +algoritma+ "&selectedlanguage=" + lang;
    console.log(url);
    $.get(url, function(response){
        $("#kebahasa").html(response);
    });
}

