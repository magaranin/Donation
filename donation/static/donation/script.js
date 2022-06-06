const imgs = document.getElementById('imgs');
const img = document.querySelectorAll('#imgs img');

const amountButtons = document.querySelectorAll('.amount_buttons .button');
const donateBtn = document.querySelector('.donate');
const amountButtonsContainer = document.querySelector('.amount_buttons');
const amountOtherForm = document.querySelector('.amount_other form');
const input = document.querySelector('#value_price');

let idx = 0;
let interval = setInterval(run, 2000);

function run() {
    idx++;
    changeImage();
}

function changeImage() {
    if (idx > img.length - 1) {
        idx = 0;
    }
    else if (idx < 0) {
        idx = img.length - 1;
    }
    imgs.style.transform = `translateX(${-idx * 900}px)`
}

amountButtonsContainer.addEventListener('click', (e) => {
    removeSelected();
    e.target.classList.add('selected');
})

input.addEventListener("focus", (event) => {
    removeSelected();
  });


donateBtn.addEventListener('click', (e) => {
    const form = amountButtonsContainer.querySelector('.button.selected form');
    const otherValue = Number(document.getElementById('value_price').value);
    if (form !== null) {
        form.submit();
    }
    else {
        if (!isNaN(otherValue) && otherValue >= 1 && otherValue <= 100000) {
            removeSelected()
            amountOtherForm.submit();
        }
        else {
            alert("Please enter an amount that you would like to donate!");
        }
    }
})

function removeSelected() {
    for (let i = 0; i < amountButtons.length; i++) {
        amountButtons[i].classList.remove('selected');
    }
}