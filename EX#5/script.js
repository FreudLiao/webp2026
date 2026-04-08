function getRandomString(length) {
    let result = '';
    const characters = 'abcdefghijklmnopqrstuvwxyz';
    for (let i = 0; i < length; i++) {
        result += characters.charAt(Math.floor(Math.random() * characters.length));
    }
    return result;
}

const container = document.getElementById('container');

window.onload = function() {
    const initialCount = Math.floor(Math.random() * 3); // 0, 1, 2
    container.textContent = getRandomString(initialCount);
};

window.addEventListener('keyup', function(e) {
    let currentText = container.textContent;
    let typedKey = e.key.toLowerCase();

    if (currentText.length > 0 && typedKey === currentText[0]) {
        container.textContent = currentText.substring(1);
    }

    const addCount = Math.floor(Math.random() * 3) + 1; // 1, 2, 3
    container.textContent += getRandomString(addCount);
});
