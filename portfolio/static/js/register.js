const validateData = (event) => {
    let form = document.forms["register"];
    let status = true

    if (form.username.value == "") {
        document.querySelector("#username-error").innerHTML = "Username is Required"
        document.querySelector("#username-error-box").classList.remove("hidden")
        status = false
    }
    if (form.email.value == "") {
        document.querySelector("#email-error").innerHTML = "Email is Required"
        document.querySelector("#email-error-box").classList.remove("hidden")
        status = false
    }
    if (form.password.value == "") {
        document.querySelector("#password-error").innerHTML = "Password is Required"
        document.querySelector("#password-error-box").classList.remove("hidden")
        status = false
    }
    if (form.cpassword.value == "") {
        document.querySelector("#cpassword-error").innerHTML = "Confirm Password is Required"
        document.querySelector("#cpassword-error-box").classList.remove("hidden")
        status = false
    }
    if (form.cpassword.value != "")
        if(form.cpassword.value != form.password.value) {
            document.querySelector("#cpassword-error").innerHTML = "Must be enter same password"
            document.querySelector("#cpassword-error-box").classList.remove("hidden")
            status = false
        }
    else {
        status =  true
    }
    return status

}