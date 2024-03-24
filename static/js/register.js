
/* for eye button */
var a;
function pass() {
    if (a == 1) {
        document.querySelector(".password").type = "password";
        var togglepassword = document.querySelector(".togglepassword");
        togglepassword.className = "fa-sharp fa-solid fa-eye-slash togglepassword"
        a = 0;
    }
    else {
        document.querySelector(".password").type = 'text';
        var togglepassword = document.querySelector(".togglepassword");
        togglepassword.className = "fa-sharp fa-solid fa-eye togglepassword"
        a = 1;
    }
}
var b;
function pass2() {
    if (b == 1) {
        document.querySelector(".password").type = "password";
        document.querySelector(".confirm_password").type = "password";
        var togglepassword2 = document.querySelector(".togglepassword2");
        togglepassword2.className = "fa-sharp fa-solid fa-eye-slash togglepassword2"
        b = 0;
    }
    else {
        document.querySelector(".password").type = 'text';
        document.querySelector(".confirm_password").type = 'text';
        var togglepassword2 = document.querySelector(".togglepassword2");
        togglepassword2.className = "fa-sharp fa-solid fa-eye togglepassword2"
        b = 1;
    }
}
function close()
{
    document.querySelector(".message").display="none";
}
/*for day night transiyion */
function day(){
    var switchB=document.getElementById("switchB");
    switchB.style.left="0px";
    
}
function night(){
    var switchB=document.getElementById("switchB");
    switchB.style.left="50%";
    
}

