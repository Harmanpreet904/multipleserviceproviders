function sendotp() {
    var phone = document.getElementById('phone').value;
    var xml = new XMLHttpRequest();
    xml.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            var output = this.response;
            alert(output);
            $("#myModal").modal("show")
            // document.getElementById('')
        }
    };
    xml.open('GET', 'sendotp?phone=' + phone, true);
    xml.send(phone);
}

function verifyotp() {
    var fromdata = new FormData();
    fromdata.append('sendedotp', document.getElementById('sendedotp').value);
    // var sendedotp=document.getElementById('sendedotp').value;
    var xml = new XMLHttpRequest();
    xml.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            var output = this.response;
            alert(output);
            var mobile=document.getElementById('phone').value;
            window.location.href="usersignup2?mobile="+mobile;
            // document.getElementById('')

        }
    };
    xml.open('POST', 'verifyotp', true);
    xml.send(fromdata);

}

function signup() {

    var adduserdata=new FormData();
    // alert(document.getElementById('mobile').value);
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
            // $("#myaddcateogry").modal('hide');
            // viewcategory()
        }
    };
    xml.open('POST', 'insertuserdata', true);
    xml.send(adduserdata);

}

function serviceprovidersignup() {
    var adduserdata=new FormData();
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

    var xml = new XMLHttpRequest();
    xml.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            var output = this.response;
            alert(output);
            window.location.href="index"
        }
    };
    xml.open('POST', 'insertserviceprovider', true);
    xml.send(adduserdata);
}

function serviceproviderlogin() {
    var merchantlogin=new FormData();
    merchantlogin.append('email', document.getElementById('email').value);
    merchantlogin.append('password', document.getElementById('password').value);
    var xml = new XMLHttpRequest();
    xml.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            var output = this.response;
            if (output=="1"){
                // var memail=document.getElementById('email').value;
                window.location.href="merchantdashboaard?";
            }
            else{
                alert("Invalid Login")
            }


        }
    };
    xml.open('POST', 'serviceproviderlogin', true);
    xml.send(merchantlogin);


}

function addmerchantservices() {
    var addserivces=new FormData();
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


function forgetmerchantpassword() {
    var adduserdata=new FormData();
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

//ADMIN LOGIN FORGET PASSWORD
function forget() {
    var adduserdata=new FormData();
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
/////////////////////////////////////////////////////////////////////


function userlogin(){
    var userlogin=new FormData();
    userlogin.append('email',document.getElementById('email').value);
    userlogin.append('password',document.getElementById('password').value);
    var xml = new XMLHttpRequest();
    xml.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            var output = this.response;
            if (output=="1"){
                window.location.href="userindex"
            }
            else{
                alert("Invalid Login")
            }

        }
    };
    xml.open('POST', 'userlogin', true);
    xml.send(userlogin);
}


///////////////////////////////////////////////////////////////////////////////////////////////////////////////
