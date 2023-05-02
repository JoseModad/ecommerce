window.addEventListener("load", function () {
    const passwordField = document.getElementById("password");
    const repasswordField = document.getElementById("repassword");
    let isPasswordFieldValid = false;
    let isPasswordMatch = false;

    repasswordField.readOnly = true;
    repasswordField.style.color = "gray";
    
    passwordField.addEventListener("input", function () {
        isPasswordFieldValid = this.value.length > 5;
        repasswordField.readOnly = !isPasswordFieldValid;
        repasswordField.style.color = isPasswordFieldValid ? "initial" : "gray";
        isPasswordMatch = false;
        repasswordField.style.backgroundColor = "";
    });

    // Comparar las contraseñas al cambiar de campo en el repassword
    repasswordField.addEventListener("input", function () {
        if (isPasswordFieldValid) {
            if (this.value.length === passwordField.value.length && this.value === passwordField.value) {
                isPasswordMatch = true;
                this.style.backgroundColor = "lightgreen";
            } else {
                isPasswordMatch = false;
                this.style.backgroundColor = "lightcoral";
            }
        }
    });

    repasswordField.addEventListener("blur", function () {
        if (isPasswordFieldValid && !isPasswordMatch) {            
            this.value = "";
            passwordField.value = "";
            this.readOnly = true;
            this.style.color = "gray";
        }
    });
});







