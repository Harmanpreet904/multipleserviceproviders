function sendotp() {
    var phone = document.getElementById('phone').value;
    var mobi = /^\(?([0-9]{3})\)?[-. ]?([0-9]{3})[-. ]?([0-9]{4})$/;
    if (phone == "") {
        alert("Please enter mobile No");
        return false;
    } else if (!(phone).match(mobi)) {
        alert("Mobile no must contain minimum and not more than 10 digits ")
    } else {
        var xml = new XMLHttpRequest();
        xml.onreadystatechange = function () {
            if (this.readyState == 4 && this.status == 200) {
                var output = this.response;
                alert(output);
                $("#myModal").modal("show")

            }
        };
        xml.open('GET', 'sendotp?phone=' + phone, true);
        xml.send(phone);
    }
}

function verifyotp() {
    var fromdata = new FormData();
    fromdata.append('sendedotp', document.getElementById('sendedotp').value);
    // var sendedotp=document.getElementById('sendedotp').value;
    var xml = new XMLHttpRequest();
    xml.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            var output = this.response;
            if (output == "sucess") {
                alert(output);
                var mobile = document.getElementById('phone').value;
                window.location.href = "usersignup2?mobile=" + mobile;
            } else {
                alert("otp Not Matched")
            }

        }
    };
    xml.open('POST', 'verifyotp', true);
    xml.send(fromdata);

}

//----------------------------------------------------------------------------------------------------------------------

function signup() {
    var valmob = document.getElementById('mobile').value;
    var email = document.getElementById('email').value;
    var address = document.getElementById('address').value;
    var city = document.getElementById('city').value;
    var photo = document.getElementById('image').files[0];
    var emailReg = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
    var mobi = /^\(?([0-9]{3})\)?[-. ]?([0-9]{3})[-. ]?([0-9]{4})$/;
    if (valmob == "" || email == "" || address == "" || city == "" || photo == "") {
        alert("Please Fill All Required Fields");
        return false;
    } else if (!(valmob).match(mobi)) {
        alert("Mobile no must contain minimum and not more than 10 digits ");
        return false;
    } else if (!(email).match(emailReg)) {
        alert("Invalid Email...!!!!!!");
        return false;
    } else {
        var adduserdata = new FormData();
        adduserdata.append('mobile', document.getElementById('mobile').value);
        adduserdata.append('email', document.getElementById('email').value);
        adduserdata.append('address', document.getElementById('address').value);
        adduserdata.append('city', document.getElementById('city').value);
        adduserdata.append('image', document.getElementById('image').files[0]);
        var xml = new XMLHttpRequest();
        xml.onreadystatechange = function () {
            if (this.readyState == 4 && this.status == 200) {
                var output = this.response;
                alert(output);
            }
        };
        xml.open('POST', 'insertuserdata', true);
        xml.send(adduserdata);
    }
}

//----------------------------------------------------------------------------------------------------------------------
function serviceprovidersignup() {
    var valmob = document.getElementById('mobile').value;
    var email = document.getElementById('email').value;
    var password = document.getElementById('password').value;
    var repass = document.getElementById('cnfpassword').value;
    var business = document.getElementById('business').value;
    var address = document.getElementById('address').value;
    var timing = document.getElementById('timing').value;
    var price = document.getElementById('price').value;
    var servicearea = document.getElementById('servicearea').value;
    var stt = document.getElementById('sts').value;
    var city = document.getElementById('state').value;
    var emailReg = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
    var passw = /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{6,20}$/;
    var mobi = /^\(?([0-9]{3})\)?[-. ]?([0-9]{3})[-. ]?([0-9]{4})$/
    if (valmob == "" || email == "" || password == "" || business == "" || address == "" || timing == "" || price == "" || servicearea == "" || stt == "" || city == "") {
        alert("Please Fill all Required Field");
        return false;
    } else if (!(valmob).match(mobi)) {
        alert("Mobile no must contain minimum and not more than 10 digits ");
        return false;
    } else if (!(email).match(emailReg)) {
        alert("Invalid Email...!!!!!!");
        return false;
    } else if (!(password).match(passw)) {
        alert("Enter atleast one Capital & one special symbol and length minimum 6");
        return false;
    } else if (password != repass) {
        alert("Passwords don't Matched");
        return false;
    } else {
        var adduserdata = new FormData();
        adduserdata.append('mobile', document.getElementById('mobile').value);
        adduserdata.append('email', document.getElementById('email').value);
        adduserdata.append('password', document.getElementById('password').value);
        adduserdata.append('business', document.getElementById('business').value);
        adduserdata.append('category', document.getElementById('category').value);
        adduserdata.append('address', document.getElementById('address').value);
        adduserdata.append('timing', document.getElementById('timing').value);
        adduserdata.append('price', document.getElementById('price').value);
        adduserdata.append('servicearea', document.getElementById('servicearea').value);
        adduserdata.append('stt', document.getElementById('sts').value);
        adduserdata.append('city', document.getElementById('state').value);
        adduserdata.append('csrfmiddlewaretoken', '{{ csrf_token }}');
        alert(document.getElementById('mobile').value);
        var xml = new XMLHttpRequest();
        xml.onreadystatechange = function () {
            if (this.readyState == 4 && this.status == 200) {
                var output = this.response;
                alert(output);
                window.location.href = "index"
            }
        };
        xml.open('POST', 'insertserviceprovider', true);
        xml.send(adduserdata);
    }
}

//----------------------------------------------------------------------------------------------------------------------------------------------------------------------
function serviceproviderlogin() {
    var email = document.getElementById('email').value;
    var password = document.getElementById('password').value;
    var emailReg = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
    var passw = /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{6,20}$/;
    if (email == "" || password == "") {
        alert("Fill all required Fields");
        return false;
    } else if (!(email).match(emailReg)) {
        alert("Invalid E-mail !!!!!");
        return false;
    } else if (!(password).match(passw)) {
        alert("Enter atleast one Capital & one special symbol and length minimum 6");
        return false;
    } else {
        var merchantlogin = new FormData();
        merchantlogin.append('email', document.getElementById('email').value);
        merchantlogin.append('password', document.getElementById('password').value);
        var xml = new XMLHttpRequest();
        xml.onreadystatechange = function () {
            if (this.readyState == 4 && this.status == 200) {
                var output = this.response;
                if (output == "1") {
                    // var memail=document.getElementById('email').value;
                    window.location.href = "merchantdashboaard?";
                } else {
                    alert("Invalid Login")
                }


            }
        };
        xml.open('POST', 'serviceproviderlogin', true);
        xml.send(merchantlogin);
    }
}

//--------------------------------------------------------------------------------------------------------------------------------------
function addmerchantservices() {
    var email = document.getElementById('email').value;
    var services = document.getElementById('services').value;
    var price = document.getElementById('price').value;
    var description = document.getElementById('description').value;
    var photo = document.getElementById('photo').files[0];
    var emailReg = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
    if (email == "" || services == "" || price == "" || description == "" || photo == "") {
        alert("Please fill all required fields")
        return false;
    }else if(!(email).match(emailReg)){
        alert("Invalid Email !!!!!")
        return false;
    }
    else{
        var addserivces = new FormData();
        addserivces.append('email', document.getElementById('email').value);
        addserivces.append('services', document.getElementById('services').value);
        addserivces.append('price', document.getElementById('price').value);
        addserivces.append('description', document.getElementById('description').value);
        addserivces.append('photo', document.getElementById('photo').files[0]);
        var xml = new XMLHttpRequest();
        xml.onreadystatechange = function () {
            if (this.readyState == 4 && this.status == 200) {
                var output = this.response;
                alert(output);
            }
        };
        xml.open('POST', 'addmerchantservices', true);
        xml.send(addserivces);
    }
}

//-------------------------------------------------------------------------------------------------------------------------------------
function forgetmerchantpassword() {
    var mobile=document.getElementById('mob').value;
    var mobi = /^\(?([0-9]{3})\)?[-. ]?([0-9]{3})[-. ]?([0-9]{4})$/;
    if(mobile==""){
        alert("Please Enter mobile no")
        return false;
    }
    else if(!(mobile).match(mobi)){
        alert("Enter atleast one Capital & one special symbol and length minimum 6");
        return false;
    }
    else{
        var adduserdata = new FormData();
        adduserdata.append('mob', document.getElementById('mob').value);
        var xml = new XMLHttpRequest();
        xml.onreadystatechange = function () {
            if (this.readyState == 4 && this.status == 200) {
                var output = this.response;
                alert(output);
            }
        };
        xml.open('POST', 'forgetmerchantpassword', true);
        xml.send(adduserdata);
    }
}
//-------------------------------------------------------------------------------------------------------------------------------------------------------
//ADMIN LOGIN FORGET PASSWORD
function forget() {
    var mobile=document.getElementById('mob').value;
    var mobi = /^\(?([0-9]{3})\)?[-. ]?([0-9]{3})[-. ]?([0-9]{4})$/;
    if(mobile==""){
        alert("Please Enter mobile no")
        return false;
    }
    else if(!(mobile).match(mobi)){
        alert("Enter atleast one Capital & one special symbol and length minimum 6");
        return false;
    }
    else{
    var adduserdata = new FormData();
    adduserdata.append('mob', document.getElementById('mob').value);
    var xml = new XMLHttpRequest();
    xml.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            var output = this.response;
            alert(output);
        }
    };
    xml.open('POST', 'forgetpassword', true);
    xml.send(adduserdata);
    }
}

//--------------------------------------------------------------------------------------------------------------------------------------------------------------


function userlogin() {
    var email = document.getElementById('email').value;
    var password = document.getElementById('password').value;
    var emailReg = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
    var passw = /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{6,20}$/;
    if (email == "" || password == "") {
        alert("Fill all required Fields");
        return false;
    } else if (!(email).match(emailReg)) {
        alert("Invalid E-mail !!!!!");
        return false;
    } else if (!(password).match(passw)) {
        alert("Enter atleast one Capital & one special symbol and length minimum 6");
        return false;
    } else {
        var userlogin = new FormData();
        userlogin.append('email', document.getElementById('email').value);
        userlogin.append('password', document.getElementById('password').value);
        var xml = new XMLHttpRequest();
        xml.onreadystatechange = function () {
            if (this.readyState == 4 && this.status == 200) {
                var output = this.response;
                if (output == "1") {
                    window.location.href = "userindex"
                } else {
                    alert("Invalid Login")
                }

            }
        };
        xml.open('POST', 'userlogin', true);
        xml.send(userlogin);
    }
}


///////////////////////////////////////////////////////////////////////////////////////////////////////////////
