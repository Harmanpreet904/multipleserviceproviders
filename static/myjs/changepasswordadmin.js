function changepassrequest() {
    var fromdata=new FormData();
    fromdata.append('oldpassword',document.getElementById('oldpassword').value);
    fromdata.append('newpassword',document.getElementById('newpassword').value);
    var  xml=new XMLHttpRequest();
    xml.onreadystatechange=function () {
        if (this.readyState==4 && this.status==200){
            var output=this.response;
            if (output=="1"){
                alert("Password Changed Successfully");
                $('#myModal').modal('hide')
            }
            else {
                alert("fail to change password")
            }

        }
    };
    xml.open('post','changepassword',true);
    xml.send(fromdata);
}