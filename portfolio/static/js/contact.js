const validateData = (event) => {
    let form = document.forms["contact"];
    const phone = form.phone.value.trim();
    const mobileError = document.getElementById("mobile-error");

    const email = form.email.value
    if (!email.endsWith(".com") && !email.endsWith(".in")) {
        document.querySelector("#email-error").classList.remove("hidden")
        document.querySelector("#email-error").innerHTML = "invalied email "
       return false
    }
    if (!/^[0-9]{10}$/.test(phone)) {
        mobileError.textContent = "Mobile must be 10 digits and numbers only";
        mobileError.classList.remove("hidden");
        return false;
}
 
    else {
    return true
    }

}