const usernameField = document.querySelector("#usernameField");
const feedbackArea = document.querySelector(".invalid-feedback");

// event handler to know when user types something
usernameField.addEventListener("keyup", (e) => {
    const usernameValue = e.target.value; //what user types in

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
            if(data.username_error) {
                usernameField.classList.add('is-invalid');
                feedbackArea.style.display = 'block';
                feedbackArea.innerHTML = `<p>${data.username_error}</p>`;
                
            }
        });
    }
    
});