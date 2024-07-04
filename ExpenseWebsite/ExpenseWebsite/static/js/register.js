const usernameField = document.querySelector("#usernameField");
const feedbackArea = document.querySelector(".Username-invalid-feedback");
const emailField = document.querySelector("#emailField");
const EmailfeedbackArea = document.querySelector(".Emailinvalid-feedback");
const usernameSuccessOutput = document.querySelector(".username-success-output");
const emailSuccessOutput = document.querySelector(".email-success-output");

// event handler to know when user types something
usernameField.addEventListener("keyup", (e) => {
    const usernameValue = e.target.value; //what user types in

    usernameSuccessOutput.style.display = 'block';
    usernameSuccessOutput.textContent = `Checking ${usernameValue}`

    usernameField.classList.remove('is-invalid');
    feedbackArea.style.display = 'none';

    if (usernameValue.length > 0) {
        fetch("/auth/validate-username/", {
            body: JSON.stringify({username: usernameValue}), //send data to server in json format
            method: 'POST',
        })
        .then((res) => res.json())
        .then((data) => {
            console.log('data', data);
            usernameSuccessOutput.style.display = 'none';
            if(data.username_error) {
                usernameField.classList.add('is-invalid'); //display red border
                feedbackArea.style.display = 'block';
                feedbackArea.innerHTML = `<p>${data.username_error}</p>`;
                
            }
        });
    }
    else
    {
        usernameSuccessOutput.style.display = 'none';
    }
    
});


emailField.addEventListener("keyup", (e) => {
    const emailValue = e.target.value; //what user types in
    
    emailSuccessOutput.style.display = 'block';
    emailSuccessOutput.textContent = `Checking ${emailValue}`
    
    emailField.classList.remove('is-invalid');
    EmailfeedbackArea.style.display = 'none';

    if (emailValue.length > 0) {
        fetch("/auth/validate-email/", {
            body: JSON.stringify({email: emailValue}), //send data to server in json format
            method: 'POST',
        })
        .then((res) => res.json())
        .then((data) => {
            console.log('data', data);
            emailSuccessOutput.style.display = 'none';
            if(data.email_error) {
                emailField.classList.add('is-invalid'); //display red border
                EmailfeedbackArea.style.display = 'block';
                EmailfeedbackArea.innerHTML = `<p>${data.email_error}</p>`;
                
            }
        });
    }
    else
    {
        emailSuccessOutput.style.display = 'none';
    }
    
});



// static files not getting refreshed: ctrl+shift+r to refresh