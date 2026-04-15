var container = document.getElementById('container');

let wrongCount = 0;

window.onload = function() {
    container.textContent = add_new_chars(3);
};

function add_new_chars(x) {
    var str = '';
    for (let i = 0; i < x; i++) {
        str += String.fromCharCode(97 + Math.floor(Math.random() * 26));
    }
    return str;
}

window.addEventListener("keyup", function(e) {
    var firstone = container.textContent.substring(0, 1);

    if (e.key === firstone) {
        container.textContent = container.textContent.substring(1);
        container.textContent += add_new_chars(3);
        wrongCount = 0;
        
        console.log("打對了！");
    } else {
        wrongCount++;
        console.log("打錯次數：" + wrongCount);

        if (wrongCount === 3) {
            container.textContent += add_new_chars(3);
            wrongCount = 0;
            alert("連續打錯三次！懲罰增加字數！");
        } else {
            container.textContent += e.key; 
        }
    }
});
