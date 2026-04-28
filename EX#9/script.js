var dataUrl = "https://api.flickr.com/services/rest/?method=flickr.photos.getRecent&api_key=ca370d51a054836007519a00ff4ce59e&per_page=10&format=json&nojsoncallback=1";
function getimg() {
    var xhr = new XMLHttpRequest();
    xhr.open("GET", dataUrl, true);
    xhr.send();
    xhr.onload = function () {
        if (xhr.status === 200) {
            var data = JSON.parse(this.responseText);
            add_new_img(data.photos.photo);
        } else {
            alert("API request failed. Status: " + xhr.status);
            console.log(this.responseText);
        }
    };
    xhr.onerror = function () {
        alert("Network error.");
    };
}
function add_new_img(dataset) {
    var gal = document.getElementById("gallery");
    gal.innerHTML = "";
    dataset.forEach(function (item) {
        var img = document.createElement("img");
        var imgSrc = "https://live.staticflickr.com/" +
            item.server + "/" +
            item.id + "_" +
            item.secret + "_q.jpg";
        img.setAttribute("src", imgSrc);
        img.setAttribute("alt", item.title || "flickr photo");
        gal.appendChild(img);
    });
}
