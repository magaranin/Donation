const imgs = document.getElementById('imgs');
const img = document.querySelectorAll('#imgs img');

const amountButtons = document.querySelectorAll('.amount_buttons .button');
const donateBtn = document.querySelector('.donate');
const amountButtonsContainer = document.querySelector('.amount_buttons');
const amountOtherForm = document.querySelector('.amount_other form');
const input = document.querySelector('#value_price');

const paymentFrequency = document.querySelector('.paymentFrequency');
const donationFrequencyButtons = document.querySelectorAll('.paymentFrequency .button');

const mainPagePaymentFrequency = document.querySelector('.main_page_payment_frequency');

const donateMonthly = document.getElementById('monthly');

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
    removeSelected(amountButtons);
    e.target.classList.add('selected');
});

paymentFrequency.addEventListener('click', (e) => {
    removeSelected(donationFrequencyButtons);
    const button = e.target;
    button.classList.add('selected');
    const forms = document.querySelectorAll('form');
    forms.forEach((form) => {
        if (button.id === "monthly") {
            form.action = form.action.replace("/payment", "/subscription");
        } else {
            form.action = form.action.replace("/subscription", "/payment");
        }
        console.log(form.action);
    });
});

input.addEventListener("focus", (event) => {
    removeSelected(amountButtons);
  });

donateBtn.addEventListener('click', (e) => {
    const form = amountButtonsContainer.querySelector('.button.selected form');
    const otherValue = Number(document.getElementById('value_price').value);
    if (form !== null) {
        form.submit();
    }
    else {
        if (!isNaN(otherValue) && otherValue >= 1 && otherValue <= 100000) {
            removeSelected(amountButtons);
            amountOtherForm.submit();
        }
        else {
            alert("Please enter an amount that you would like to donate!");
        }
    }
})

function removeSelected(buttons) {
    for (let i = 0; i < buttons.length; i++) {
        buttons[i].classList.remove('selected');
    }
}

if(window.location.href.indexOf('subscription') > 0) {
    donateMonthly.click();
}