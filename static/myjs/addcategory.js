function addcategory() {
    var categoryname=document.getElementById('categoryname').value;
    var description=document.getElementById('description').value;
    var photo=document.getElementById('image').files[0];
    if(categoryname=="" || description=="" || photo==""){
        alert("Fill all required fields")
        return false;
    }else {
        var fromdata = new FormData();
        fromdata.append('categoryname', document.getElementById('categoryname').value);
        fromdata.append('description', document.getElementById('description').value);
        fromdata.append('image', document.getElementById('image').files[0]);
        var xml = new XMLHttpRequest();
        xml.onreadystatechange = function () {
            if (this.readyState == 4 && this.status == 200) {
                var output = this.response;
                alert(output);
                $("#myaddcateogry").modal('hide');
                viewcategory()
            }
        };
        xml.open('post', 'addcategoryaction', true);
        xml.send(fromdata);
    }
}
//-----------------------------------------------------------------------------------------------------------
function viewcategory() {
    var xml = new XMLHttpRequest();
    xml.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            var output = JSON.parse(this.response);
            s = "";
            for (var i = 0; i < output.length; i++) {
                s += "<tr>";
                s += "<td>" + (i + 1) + "</td>";
                s += "<td>" + output[i]['category'] + "</td>";
                s += "<td>" + output[i]['desc'] + "</td>";
                s += "<td><img src='static/media/Categoryphotos/" + output[i]['image'] + "' width='100'></td>";
                s += "<td ><button type='button' class='btn btn-danger' onclick='deletecategory(" + '"' + output[i]["category"] + '"' + ")'><strong class='fas fa-trash-alt'></strong></button></td> ";
                s += "<td><button type='button' class='btn btn-warning' onclick='editcategory(" + '"' + output[i]["category"] + '"' + ")'><strong class='fas fa-edit'></strong></button></td> ";
                s += "</tr>";
            }
            document.getElementById('viewdata').innerHTML = s;
        }
    };
    xml.open('GET', 'viewcateogry', true);
    xml.send();
}
//-------------------------------------------------------------------------------------------------------------------------------------------------
function deletecategory(category) {
    // alert(category);
    if (confirm("Are you Sure to Delete?")) {
        var fordata = new FormData();
        fordata.append('catname', category);
        var xml = new XMLHttpRequest();
        xml.onreadystatechange = function () {
            if (this.readyState == 4 && this.status == 200) {
                var output = this.response;
                alert(output);
                viewcategory();
            }
        };
        xml.open("POST", "deletecategory", true);
        xml.send(fordata);
    }
}

//---------------------------------------------------------------------------------------------------------------------------------------------------
function editcategory(category) {
        $("#editcategory").modal('show');
        var fordata = new FormData();
        fordata.append('catname', category);
        var xml = new XMLHttpRequest();
        xml.onreadystatechange = function () {
            if (this.readyState == 4 && this.status == 200) {
                var output = this.response;
                alert(output);
                viewcategory();
            }
        };
        xml.open("POST", "editcategory", true);
        xml.send(fordata);
}



//Send OTP For UserSignUP

