import math
import random
from typing import Dict, Any
import http.client

from django.core.files.storage import FileSystemStorage
from django.shortcuts import *
from django.http import *
from pymysql import *
from django.views.decorators.csrf import csrf_exempt


# Main Admin Who handles all Management
def addadmin(request):
    return render(request, "manageadmin.html")


@csrf_exempt
def insertadmin(request):
    conn = Connect('127.0.0.1', 'root', '', 'msp')
    email = request.POST['email']
    password = request.POST['password']
    type = request.POST['type']
    mobile = request.POST['mobile']
    s = f"insert into admins values('{email}','{password}','{type}','{mobile}')"
    cr = conn.cursor()
    cr.execute(s)
    conn.commit()
    return HttpResponseRedirect('viewadmin')


def viewadmin(request):
    conn = Connect('127.0.0.1', 'root', '', 'msp')
    s = "select * from admins"
    cr = conn.cursor()
    cr.execute(s)
    result = cr.fetchall()
    x = []
    for row in result:
        # d = {}
        d: Dict[str, Any] = {'email': row[0], 'password': row[1], 'type': row[2], 'mobile': row[3]}
        x.append(d)
    return render(request, "viewadmin.html", {"ar": x})


def removeadmin(request):
    conn = Connect('127.0.0.1', 'root', '', 'msp')
    s = "delete from admins where email='" + request.GET["p"] + "'"
    cr = conn.cursor()
    cr.execute(s)
    conn.commit()
    return HttpResponseRedirect('viewadmin')


def fetchadmindetailsforupdate(request):
    conn = Connect('127.0.0.1', 'root', '', 'msp')
    s = "select * from admins where email='" + request.GET["email"] + "'"
    cr = conn.cursor()
    cr.execute(s)
    row = cr.fetchone()
    d = {'email': row[0], 'password': row[1], 'type': row[2], 'mobile': row[3]}
    return render(request, 'updateadmin.html', {'ar': d})


def updateadmins(request):
    conn = Connect('127.0.0.1', 'root', '', 'msp')
    s = "update admins set password='" + request.POST['password'] + "',`type`='" + request.POST[
        'type'] + "',`mobile`='" + request.POST['mobile'] + "' WHERE email='" + request.POST['email'] + "'"
    cr = conn.cursor()
    cr.execute(s)
    conn.commit()
    return HttpResponseRedirect('viewadmin')


@csrf_exempt
def adminlogin(request):
    if request.method == 'POST':
        conn = Connect('127.0.0.1', 'root', '', 'msp')
        email = request.POST["email"]
        password = request.POST["password"]
        s = f"select * from admins where email='{email}' and password='{password}'"
        # s = "select * from admins where email='" +  + "' and password='" +  + "'"
        cr = conn.cursor()
        cr.execute(s)
        result = cr.fetchone()
        if result:
            request.session['e'] = email
            return render(request, 'admindashboard.html')
        else:
            return render(request, 'adminlogin.html', {'message': 'Invalid User'})
    return render(request, 'adminlogin.html')


@csrf_exempt
def forgetpassword(request):
    if request.method == 'POST':
        conn = Connect('127.0.0.1', 'root', '', 'msp')
        mobile = request.POST["mob"]
        s = f"select * from admins where mobile='{mobile}'"
        cr = conn.cursor()
        cr.execute(s)
        result = cr.fetchone()
        if result:
            msg = "your password is:" + str(result[1])
            msg = msg.replace(" ", "%20")
            conn = http.client.HTTPConnection('server1.vmm.education')
            conn.request('GET',
                         "/VMMCloudMessaging/AWS_SMS_Sender?username=harmanpreetsingh&password=GO8VBM3L&message=" + msg + "&phone_numbers=" + mobile)
            return HttpResponse('Password Sent Successfully')
        else:
            return HttpResponse('Invalid Mobile')


# Merchant forget password
@csrf_exempt
def forgetmerchantpassword(request):
    if request.method == 'POST':
        conn = Connect('127.0.0.1', 'root', '', 'msp')
        mobile = request.POST["mob"]
        s = f"select * from serviceproviders where mobile='{mobile}'"
        cr = conn.cursor()
        cr.execute(s)
        result = cr.fetchone()
        if result:
            msg = "your password is:" + str(result[2])
            msg = msg.replace(" ", "%20")
            conn = http.client.HTTPConnection('server1.vmm.education')
            conn.request('GET',
                         "/VMMCloudMessaging/AWS_SMS_Sender?username=harmanpreetsingh&password=GO8VBM3L&message=" + msg + "&phone_numbers=" + mobile)
            print(msg)
            return HttpResponse('Password Sent Successfully')
        else:
            return HttpResponse('Invalid Mobile')


# Search Registered Users
@csrf_exempt
def searchuser(request):
    x = []
    if request.method == 'POST':
        conn = Connect('127.0.0.1', 'root', '', 'msp')
        data = request.POST['search']
        s = f"select * from admins where email='{data}'"
        cr = conn.cursor()
        cr.execute(s)
        result = cr.fetchall()
        for row in result:
            if data == row[0:]:
                d = {'email': row[0], 'password': row[1], 'type': row[2], 'mobile': row[3]}
                x.append(d)
        print(x)
    return render(request, 'viewadmin.html', {"ar": x})


@csrf_exempt
def changepassword(request):
    email = request.session['e']
    oldpassword = request.POST['oldpassword']
    newpassword = request.POST['newpassword']
    conn = Connect('127.0.0.1', 'root', '', 'msp')
    query = f"Select * from admins where email='{email}' and password='{oldpassword}'"
    cr = conn.cursor()
    cr.execute(query)
    result = cr.fetchall()
    if result:
        query = f"update admins set password='{newpassword}' where email='{email}' and password='{oldpassword}'"
        cr.execute(query)
        conn.commit()
        result1 = "1"
    else:
        result1 = "2"
    return HttpResponse(result1)


# Category of Services
@csrf_exempt
def addcategoryaction(request):
    conn = Connect('127.0.0.1', 'root', '', 'msp')
    categoryname = request.POST['categoryname']
    description = request.POST['description']
    photo = request.FILES['image']
    fs = FileSystemStorage()
    myfile = request.FILES['image']
    fs.save(str('Categoryphotos/' + myfile.name), myfile)
    query = f"insert into category values ('{categoryname}','{description}','{photo}')"
    print(query)
    try:
        cr = conn.cursor()
        cr.execute(query)
        conn.commit()
        result = "Sucess Full Insert"
    except:
        result = "Fail"
    return HttpResponse(result)


def addcategory(request):
    return render(request, 'addcategory.html')


def viewcateogry(request):
    conn = Connect('127.0.0.1', 'root', '', 'msp')
    s = "select * from category"
    cr = conn.cursor()
    cr.execute(s)
    result = cr.fetchall()
    x = []

    for row in result:
        Dict = {'category': row[0], 'desc': row[1], 'image': row[2]}
        x.append(Dict)
    return JsonResponse(x, safe=False)


@csrf_exempt
def deletecategory(request):
    conn = connect('127.0.0.1', 'root', '', 'msp')
    categoryname = request.POST['catname']
    query = f"delete from category where categoryname='{categoryname}'"
    cr = conn.cursor()
    cr.execute(query)
    conn.commit()
    return HttpResponse("Deleted Successfull")


def otp(request):
    return render(request, 'signup1.html')


def sendotp(request):
    phone = request.GET['phone']
    digits = "0123456789"
    OTP = ""
    for i in range(6):
        OTP += digits[math.floor(random.random() * 10)]
    print(OTP)
    if OTP:
        msg = "your OTP is:" + str(OTP)
        msg = msg.replace(" ", "%20")
        conn = http.client.HTTPConnection('server1.vmm.education')
        conn.request('GET',
                     "/VMMCloudMessaging/AWS_SMS_Sender?username=harmanpreetsingh&password=GO8VBM3L&message=" + msg + "&phone_numbers=" + phone)
        request.session['otp'] = OTP
        request.session['phone'] = phone
        returnvalue = 'OTP Sent Successfully'
    else:
        returnvalue = "Failed to Send OPT"
    return HttpResponse(returnvalue)


@csrf_exempt
def verifyotp(request):
    print(request.session['otp'])
    sendedotp = request.POST['sendedotp']
    if sendedotp == request.session['otp']:
        return HttpResponse("sucess")
    else:
        return HttpResponse('OTP Not Matched')


def usersignup2(request):
    # mobile=request.GET['mobile']
    return render(request, "signup2.html")


@csrf_exempt
def insertuserdata(request):
    conn = Connect('127.0.0.1', 'root', '', 'msp')
    mobile = request.POST["mobile"]
    email = request.POST['email']
    digits = "0123456789"
    password = ""
    for i in range(6):
        password += digits[math.floor(random.random() * 10)]

    address = request.POST['address']
    city = request.POST['city']
    fs = FileSystemStorage()
    myfile = request.FILES['image']
    fs.save(str('Userphotos/' + myfile.name), myfile)
    query = f"insert into users values ('{mobile}','{email}','{password}','{address}','{city}','{myfile}')"
    print(query)
    try:
        cr = conn.cursor()
        cr.execute(query)
        conn.commit()
        result = "Sucess Full Insert"
    except:
        result = "Fail"
    return HttpResponse(result)


@csrf_exempt
def userlogin(request):
    conn = Connect('127.0.0.1', 'root', '', 'msp')
    email = request.POST['email']
    password = request.POST['password']
    query = f"select * from users where email='{email}' and password={password}"
    cr = conn.cursor()
    cr.execute(query)
    result = cr.fetchone()
    if result:
        result1 = "1"
    else:
        result1 = "2"
    return HttpResponse(result1)


def userindex(request):
    return render(request, 'userindex.html')


# Service Provider Signup
def serviceprovidersignup(request):
    conn = Connect('127.0.0.1', 'root', '', 'msp')
    query = f"select * from category"
    cr = conn.cursor()
    cr.execute(query)
    result = cr.fetchall()
    x = []
    print(x)
    for row in result:
        x.append(row[0])
    return render(request, 'serviceproviders.html', {'category': x})


def serviceprovidersignin(request):
    return render(request, 'serviceprovidersignIn.html')


@csrf_exempt
def serviceproviderlogin(request):
    conn = Connect('127.0.0.1', 'root', '', 'msp')
    email = request.POST['email']
    password = request.POST['password']
    s = f"select * from serviceproviders where email='{email}' and password='{password}'"
    cr = conn.cursor()
    cr.execute(s)
    result = cr.fetchone()
    if result:
        request.session['e'] = email
        result1 = "1"
    else:
        result1 = "2"
    return HttpResponse(result1)


def merchantdashboaard(request):
    return render(request, "merchantdashboard.html")


def merchantservices(request):
    conn = Connect('127.0.0.1', 'root', '', 'msp')
    query = f'select * from serviceproviders'
    cr = conn.cursor()
    cr.execute(query)
    result = cr.fetchall()
    x = []
    print(x)
    for row in result:
        x.append(row[4])
    # email=request.GET['email']
    return render(request, 'merchantservices.html', {'category': x})


@csrf_exempt
def addmerchantservices(request):
    conn = Connect('127.0.0.1', 'root', '', 'msp')
    email = request.POST['email']
    services = request.POST['services']
    price = request.POST['price']
    description = request.POST['description']
    fs = FileSystemStorage()
    myfile = request.FILES['photo']
    fs.save(str('merchantservices/' + myfile.name), myfile)
    query = f"insert into merchantservices values ('','{email}','{services}','{price}','{description}','{myfile}')"
    print(query)
    cr = conn.cursor()
    cr.execute(query)
    conn.commit()
    result = "Sucess Full Insert"
    # try:
    #     cr = conn.cursor()
    #     cr.execute(query)
    #     conn.commit()
    #     result = "Sucess Full Insert"
    # except:
    #     result = "Fail"
    return HttpResponse(result)


@csrf_exempt
def insertserviceprovider(request):
    conn = Connect('127.0.0.1', 'root', '', 'msp')
    mobile = request.POST['mobile']
    email = request.POST['email']
    password = request.POST['password']
    business = request.POST['business']
    category = request.POST['category']
    address = request.POST['address']
    timing = request.POST['timing']
    price = request.POST['price']
    servicearea = request.POST['servicearea']
    stt = request.POST['stt']
    city = request.POST['city']
    status = "pending"
    query = f"insert into serviceproviders values ('{mobile}','{email}','{password}','{business}','{category}','{address}','{timing}','{price}','{servicearea}','{stt}','{city}','{status}')"
    cr = conn.cursor()
    cr.execute(query)
    conn.commit()
    return HttpResponse("SIGN UP SUCCESSFULLY PLEASE WAIT FOR VERIFICATION")


def searchservice1(request):
    conn = Connect('127.0.0.1', 'root', '', 'msp')
    query1 = f"select DISTINCT city from serviceproviders"
    cr = conn.cursor()
    cr.execute(query1)
    result = cr.fetchall()
    x = []
    for city in result:
        x.append(city[0])

    query2 = f"select * from category"
    cr = conn.cursor()
    cr.execute(query2)
    result = cr.fetchall()
    y = []
    for row in result:
        categorydict = {
            "catname": row[0],
            "photo": row[2]
        }
        y.append(categorydict)

    return render(request, 'searchservice1.html', {"city": x, "category": y})


def searchservice2(request):
    conn = Connect('127.0.0.1', 'root', '', 'msp')
    city = request.GET['city']
    categoryname = request.GET['catname']
    query1 = f"select * from serviceproviders where city='{city}' and category='{categoryname}'"
    cr = conn.cursor()
    cr.execute(query1)
    result = cr.fetchall()
    m = []
    for merchant in result:
        m.append(merchant[1])
    s = []
    for row in m:
        query2 = f"select * from merchantservices where email='{row}'"
        cr.execute(query2)
        result2 = cr.fetchall()
        for r in result2:
            s.append(r)
    return render(request, 'searchservice2.html', {'ar': s})




def bookservice(request):
    conn = Connect('127.0.0.1', 'root', '', 'msp')
    s1=request.GET['s1']
    s2=request.GET['s2']
    s3=request.GET['s3']
    s4=request.GET['s4']
    s5=request.GET['s5']
    mobile = request.GET['mobile']
    email = request.GET['email']
    address= request.GET['address']
    pincode = request.GET['pincode']
    return

def demomodel(request):
    return render(request, 'demomodel.html')


def index(request):
    return render(request, 'index.html')


def services(request):
    return render(request, 'services.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def error(request):
    return render(request, 'error.html')


def gallery(request):
    return render(request, 'gallery.html')


def typography(request):
    return render(request, 'typography.html')
