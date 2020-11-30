function handleEffectClick() {
    var ele = document.getElementsByName('effect');

    for (i = 0; i < ele.length; i++) {
        if (ele[i].checked) {
            changeEffect(ele[i].value);
            break;
        }
    }
}

function changeEffect(effect) {
    var xhr = new XMLHttpRequest();
    xhr.open('GET', 'change?effect=' + effect);
    xhr.onload = function() {
        if (xhr.status === 200) {
            console.log('Response ' + xhr.responseText);
        } else {
            console.log('Request failed.  Returned status of ' + xhr.status);
        }
    };
    xhr.send();

}