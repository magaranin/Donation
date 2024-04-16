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
    if (imgs) {
        imgs.style.transform = `translateX(${-idx * 100}%)`
    }
}

if (amountButtonsContainer) {
    amountButtonsContainer.addEventListener('click', (e) => {
    removeSelected(amountButtons);
    e.target.classList.add('selected');
});
}

if (paymentFrequency) {
paymentFrequency.addEventListener('click', (e) => {
    removeSelected(donationFrequencyButtons);
    const button = e.target;
    button.classList.add('selected');
    const forms = document.querySelectorAll('form');
    forms.forEach((form) => {
        if (button.id === "monthly") {
            form.action = form.action.replace("/transaction", "/subscription");
        } else {
            form.action = form.action.replace("/subscription", "/transaction");
        }
        console.log(form.action);
    });
});
}

if (input) {
input.addEventListener("focus", (event) => {
    removeSelected(amountButtons);
  });
}

if (donateBtn) {
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
});
}

function removeSelected(buttons) {
    for (let i = 0; i < buttons.length; i++) {
        buttons[i].classList.remove('selected');
    }
}

if(window.location.href.indexOf('subscription') > 0) {
    donateMonthly.click();
}

function editListing(listing_id){
    const titleElement = document.getElementById("listing_title");
    const oldTitle = titleElement.innerText;
    const descriptionElement = document.getElementById("listing_description");
    const oldDescription = descriptionElement.innerText;
    let titleTextbox = document.createElement("textarea");
    titleTextbox.value = oldTitle;
    titleTextbox.id = "title_textarea";
    titleTextbox.className = "";
    let descriptionTextbox = document.createElement("textarea");
    descriptionTextbox.value = oldDescription;
    descriptionTextbox.id = "description_textarea";
    descriptionTextbox.className = "";
    let submitButton = document.createElement("button");
    submitButton.className = "btn btn-primary btn-sm saveBtn";
    submitButton.innerHTML = "Save";
    submitButton.onclick = () => { 
        const newTitle = document.querySelector('#title_textarea').value;
        const newDescription = document.querySelector('#description_textarea').value;
        updateListing(listing_id, newTitle, newDescription);     
    }

    titleElement.innerHTML = "";
    titleElement.appendChild(titleTextbox);
    descriptionElement.innerHTML = "";
    descriptionElement.appendChild(descriptionTextbox);
    const contentElement = document.querySelector('.listing-content');
    contentElement.appendChild(submitButton);
    document.querySelector('.edit_button').style.display = 'none';

}

function updateListing(listing_id, newTitle, newDescription) {
    fetch(`/listings/${listing_id}`, {
        method: "PUT",
        body: JSON.stringify({
            title: newTitle,
            description: newDescription
        })
    })
    .then(response => response.json())
    .then(result => {
        if (result.error) {
            alert(result.error);
        }
        else {
            document.querySelector(`#listing_title`).innerHTML = newTitle;
            document.querySelector(`#listing_description`).innerHTML = newDescription;
        }
    })
    document.querySelector('.edit_button').style.display = 'block';
    document.querySelector('.saveBtn').style.display = 'none';
}