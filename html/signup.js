function check_data() {
    let email_input = document.getElementById("email");
    let email = email_input.value;
    let name_input = document.getElementById("name");
    let name = name_input.value;
    let password_input = document.getElementById("password");
    let password = password_input.value;
    // Gather age here
    let dob_input = document.getElementById("dob");
    let dob = dob_input.value;
    dob = new Date(dob);
    let curr = new Date();
    let ageMs = curr - dob;
    let ageYrs = ageMs / (1000 * 60 * 60 * 24 * 365.25);

    let errorDiv1 = document.getElementById("email-error");
    let errorDiv2 = document.getElementById("name-error");
    let errorDiv3 = document.getElementById("password-error");
    let errorDiv4 = document.getElementById("dob-error");

    // Clear the text 
    errorDiv1.textContent = "";
    errorDiv2.textContent = "";
    errorDiv3.textContent = "";
    errorDiv4.textContent = "";

    if (isValidEmail(email))
    {
        console.log("Valid Email: " + email);
    }
    else
    {
        console.log("Invalid Email Entered.");
        errorDiv1.textContent = "Please enter a valid email address.";
    }
    if (isValidName(name))
    {
        console.log("Valid Name: " + name);
    }
    else
    {
        console.log("Invalid Name Entered.");
        errorDiv2.textContent = "Please enter a valid name.";
    }
    if (isValidPassword(password))
    {
        console.log("Valid Password: " + "*".repeat(password.length));
    }
    else
    {
        console.log("Invalid Password Entered.");
        errorDiv3.innerHTML = "Please enter a password at least<br> 4 characters long.";
        errorDiv3.style.lineHeight = "1";
    }
    if (ageYrs>=13)
    {
        console.log("Valid Age: " + ageYrs);
    }
    else
    {
        console.log("Invalid Age Entered.");
        errorDiv4.textContent = "Must be 13 years or older.";
    }
}

function isValidEmail(email) {
    // Ensures there is an @, there is only one @, there is something before, there is something after.
    return email.includes('@') && email.split('@').length === 2 && email.split('@')[0].length > 0 && email.split('@')[1].length > 0;
}

function isValidName(name) {
    const nameSplit = name.split(' ');

    // Regex ensures the string is at least one or more letters and does not contain anything between
    //  except upper and lower case. Note: ^ asserts the start of string and $ denotes the end.
    return nameSplit.length === 2 && /^[A-Za-z]+$/.test(nameSplit[0]) && /^[A-Za-z]+$/.test(nameSplit[1])
        && nameSplit[0].length > 0 
        && nameSplit[1].length > 0;
}

function isValidPassword(password) {
    return password.length > 3;
}
