import math
import random
from typing import Dict, Any
import http.client
from django.core.files.storage import FileSystemStorage
from django.shortcuts import *
from django.http import *
from  pymysql import *
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


def adminlogin(request):
    return render(request, 'adminlogin.html')


@csrf_exempt
def adminlogin2(request):
    if request.method == 'POST':
        conn = Connect('127.0.0.1', 'root', '', 'msp')
        email = request.POST["email"]
        password = request.POST["password"]
        s = f"select * from admins where email='{email}' and password='{password}'"
        cr = conn.cursor()
        cr.execute(s)
        result = cr.fetchone()
        print(result)

        if result:
            request.session['adminemail'] = email
            result1 = "1"
        else:
            result1 = "2"
        return HttpResponse(result1)


def admindashboard(request):
    return render(request, 'admindashboard.html')


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

# *********************************************************************************************************************************************************************************************************************
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

# ************************************************************************************************************************************************************************************************
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
            if data == row[0]:
                d = {'email': row[0], 'password': row[1], 'type': row[2], 'mobile': row[3]}
                x.append(d)
        print(x)
    return render(request, 'viewadmin.html', {"ar": x})


@csrf_exempt
def changepassword(request):
    email = request.session['adminemail']
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
    conn = connect('127.0.0.1', 'root', '', 'msp')
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
        returnvalue = "Failed to Send OTP"
    return HttpResponse(returnvalue)
def getallcategory(request):
    print()
    conn = Connect('127.0.0.1', 'root', '', 'msp')
    s = "select distinct categoryname from category"
    cr = conn.cursor()
    cr.execute(s)
    result = cr.fetchall()
    x = []

    for row in result:
        x.append(row[0])
    return JsonResponse(x, safe=False)

@csrf_exempt
def verifyotp(request):
    print(request.session['otp'])
    sendedotp = request.POST['sendedotp']
    if sendedotp == request.session['otp']:
        return HttpResponse("sucess")
    else:
        return HttpResponse('OTP Not Matched')


def usersignup2(request):
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
    password="Your Password is"+password
    try:
        cr = conn.cursor()
        cr.execute(query)
        conn.commit()
        conn = http.client.HTTPConnection('server1.vmm.education')
        conn.request('GET',
                     "/VMMCloudMessaging/AWS_SMS_Sender?username=harmanpreetsingh&password=GO8VBM3L&message=" + password + "&phone_numbers=" + mobile)
        response=response = conn.getresponse()
        print(response)
        result = "Sucessfully Signup"
    except:
        result = "Fail"
    return HttpResponse(result)


@csrf_exempt
def userlogin(request):
    conn = Connect('127.0.0.1', 'root', '', 'msp')
    email = request.POST['email']
    password = request.POST['password']
    opr=request.POST['opr']
    if opr=="simple":
        query = f"select * from users where email='{email}' and password={password}"
        cr = conn.cursor()
        cr.execute(query)
        result = cr.fetchone()
        if result:
            request.session['useremail'] = email
            result1 = "1"
        else:
            result1 = "2"
        return HttpResponse(result1)
    else:
        print()
        query = f"select * from users where email='{email}' and password={password}"
        cr = conn.cursor()
        cr.execute(query)
        result = cr.fetchone()
        if result:
            request.session['useremail'] = email
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
    status = "done"
    s = f"select * from serviceproviders where email='{email}' and password='{password}' and status='{status}'"
    cr = conn.cursor()
    cr.execute(s)
    result = cr.fetchone()
    if result:
        request.session['merchantemail'] = email
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

def fetchcategory(request):
    conn = Connect('127.0.0.1', 'root', '', 'msp')
    cr = conn.cursor()
    type=request.GET['type']
    x = []
    query2=""
    if type=="all":
        query2 = f"select * from category"
    else:
        s=request.GET['search']
        query2 = "select * from category where categoryname LIKE '"+str(s)+"%'"
    cr = conn.cursor()
    cr.execute(query2)
    result = cr.fetchall()
    for row in result:
        categorydict = {
            "catname": row[0],
            "photo": row[2]
        }
        x.append(categorydict)
    return JsonResponse(x,safe=False)


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


def getmerchantdetails(request):
    email = request.GET['email']
    conn = Connect('127.0.0.1', 'root', '', 'msp')
    query1 = f"select * from serviceproviders where email='{email}' "
    cr = conn.cursor()
    cr.execute(query1)
    result = cr.fetchone()
    m = []
    m.append(result)
    return JsonResponse(m, safe=False)


def getmerchantavailbality(request):
    # usermob=request.GET['usermob']
    email = request.GET['email']
    date = request.GET['date']
    conn = Connect('127.0.0.1', 'root', '', 'msp')
    query1 = f"select * from booking where memail='{email}' and bookingdate='{date}' "
    cr = conn.cursor()
    cr.execute(query1)
    result = cr.fetchone()
    if result != None:
        return HttpResponse('notavailable')
    else:
        return HttpResponse('available')


def gotopaymentpage(request):
    merchantmobile = request.GET['mobile']
    totalcharges = request.GET['totalcharges']
    memail = request.GET['memail']
    serviceid = request.GET['serviceid']
    date = request.GET['date']
    d = {}
    d['totalcharges'] = (float)(totalcharges) * (100)
    d['memail'] = memail
    d['serviceid'] = serviceid
    d['date'] = date
    d['merchantmobile'] = merchantmobile
    return render(request, 'bookserviceandpay.html', {"ar": d})


def inserttodb(request):
    conn = Connect('127.0.0.1', 'root', '', 'msp')
    merchantmobile = request.GET['merchantmobile']
    memail = request.GET['memail']
    serviceid = request.GET['serviceid']
    totalcharges = request.GET['totalcharges']
    usermobile = request.GET['usermobile']
    useremail = request.GET['useremail']
    useraddress = request.GET['useraddress']
    bookingdate = request.GET['date']
    status = "pending"
    total = (float)(totalcharges) / 100

    query2 = f"insert into booking values (NULL ,'{memail}','{serviceid}','{usermobile}','{useremail}','{useraddress}','{total}','{status}','{bookingdate}')"
    cr = conn.cursor()
    cr.execute(query2)
    conn.commit()
    print(type(bookingdate))
    usermessage = "Your service is booked  service id " + str(serviceid) + "payment done online total charges" + str(
        total) + "Merchant Mobile" + str(merchantmobile) + "BookingDate" + bookingdate
    usermessage = usermessage.replace(" ", "%20")

    conn = http.client.HTTPConnection('server1.vmm.education')
    conn.request('GET',
                 "/VMMCloudMessaging/AWS_SMS_Sender?username=harmanpreetsingh&password=GO8VBM3L&message=" + usermessage + "&phone_numbers=" + usermobile)
    response = conn.getresponse()
    print(response)

    merchantmessage = "You have an appointment on date " + str(bookingdate) + "Service ID " + str(
        serviceid) + "Customer Mobile " + str(usermobile) + " Address " + str(useraddress)
    merchantmessage = merchantmessage.replace(" ", "%20")
    conn = http.client.HTTPConnection('server1.vmm.education')
    conn.request('GET',
                 "/VMMCloudMessaging/AWS_SMS_Sender?username=ishagupta&password=RNDKN5XK&message=" + merchantmessage + "&phone_numbers=" + merchantmobile)
    response = conn.getresponse()
    print(response)

    d = {
        "serviceid": serviceid, "totalcharges": total, "merchantmobile": merchantmobile, "bookingdate": bookingdate
    }
    return render(request, 'Bookingdetail.html', {"ar": d})


def viewappointments(request):
    conn = Connect('127.0.0.1', 'root', '', 'msp')
    memail = request.session['merchantemail']
    datefrom = request.GET['datefrom']
    dateto = request.GET['dateto']
    query1 = f"select * from booking where memail='{memail}' and bookingdate BETWEEN '{datefrom}' and '{dateto}'"
    cr = conn.cursor()
    cr.execute(query1)
    result = cr.fetchall()
    x = []
    print(x)
    for row in result:
        x.append(row)
    return JsonResponse(x, safe=False)


@csrf_exempt
def statusdone(request):
    conn = Connect('127.0.0.1', 'root', '', 'msp')
    memail = request.session['merchantemail']
    stsdone = "done"
    bookingid = request.POST['bookingid']
    query = f"update booking set status='{stsdone}' where bookingid='{bookingid}' and memail='{memail}'"
    cr = conn.cursor()
    cr.execute(query)
    conn.commit()
    return HttpResponse('viewappointments')


def viewuserorders(request):
    return render(request, 'viewuserorders.html')


def vieworders(request):
    conn = Connect('127.0.0.1', 'root', '', 'msp')
    useremail = request.session['useremail']
    query = f"select * from booking where useremail='{useremail}'"
    cr = conn.cursor()
    cr.execute(query)
    result = cr.fetchall()
    x = []
    print(x)
    for row in result:
        x.append(row)
    return JsonResponse(x, safe=False)


def demomodel(request):
    return render(request, 'demomodel.html')


def index(request):
    conn = Connect('127.0.0.1', 'root', '', 'msp')
    query=f"select DISTINCT city from serviceproviders"
    cr=conn.cursor()
    cr.execute(query)
    result=cr.fetchall()
    cities=[]
    for city in result:
        cities.append(city[0])

    return render(request, 'index.html',{'ar':cities})


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


def viewserviceforrating(request):
    serviceid = request.GET['serviceid']
    conn = Connect("127.0.0.1", "root", "", "msp")
    query = f"select * from merchantservices where serviceid='{serviceid}'"
    cr = conn.cursor()
    cr.execute(query)
    row = cr.fetchone()
    d = {
        "serviceid": row[0], "merchant": row[1], "services": row[2], "price": row[3], "servicedescription": row[4],
        "photo": row[5],
    }
    return render(request, 'servicedescription.html', {"row": d})


def ratingdemo(request):
    return render(request, 'ratingdemo.html')


def AddRating(request):
    conn = Connect("127.0.0.1", "root", "", "msp")
    serviceid = request.GET['serviceid']
    print(serviceid)
    score = (float)(request.GET['score'])
    review = request.GET['review']
    s = f"insert into rating values (NULL ,'{score}','{serviceid}','{review}')"
    print(s)
    cr = conn.cursor()
    cr.execute(s)
    conn.commit()
    return HttpResponse('success')


def getAverageRating(request):
    conn = Connect("127.0.0.1", "root", "", "msp")
    serviceid = request.GET['serviceid']
    avg = 0
    s = f"SELECT avg(rating) FROM rating where serviceid='{serviceid}'"
    cr = conn.cursor()
    cr.execute(s)
    result = cr.fetchone()
    print('fffffffffffffff ', result[0])
    avg = result[0]
    return HttpResponse(avg)


def viewmerchants(request):
    conn = Connect("127.0.0.1", "root", "", "msp")
    stspending = "pending"
    query = f"select * from serviceproviders where status='{stspending}'"
    cr = conn.cursor()
    cr.execute(query)
    result = cr.fetchall()
    merchants = []
    for row in result:
        merchants.append(row)
    return JsonResponse(merchants, safe=False)


def approvedmerchants(request):
    conn = Connect("127.0.0.1", "root", "", "msp")
    stsdone = "done"
    query1 = f"select * from serviceproviders where status='{stsdone}'"
    cr = conn.cursor()
    cr.execute(query1)
    result = cr.fetchall()
    merchants = []
    for row in result:
        merchants.append(row)
    return JsonResponse(merchants, safe=False)


@csrf_exempt
def merchantstatuspending(request):
    conn = Connect("127.0.0.1", "root", "", "msp")
    merchantemail = request.POST['merchantemail']
    stspending = "pending"
    query1 = f"update serviceproviders set status='{stspending}' where email='{merchantemail}'"
    cr = conn.cursor()
    cr.execute(query1)
    conn.commit()
    stsdone = "done"
    query2 = f"select * from serviceproviders where status='{stsdone}'"
    result = cr.fetchall()
    merchants = []
    for row in result:
        merchants.append(row)
    return JsonResponse(merchants, safe=False)

    return JsonResponse(merchants, safe=False)


@csrf_exempt
def merchantstatusdone(request):
    conn = Connect("127.0.0.1", "root", "", "msp")
    merchantemail = request.POST['merchantemail']
    stsdone = "done"
    query1 = f"update serviceproviders set status='{stsdone}' where email='{merchantemail}'"
    cr = conn.cursor()
    cr.execute(query1)
    conn.commit()
    stspending = "pending"
    query2 = f"select * from serviceproviders where status='{stspending}'"
    cr = conn.cursor()
    cr.execute(query2)
    result = cr.fetchall()
    merchants = []
    for row in result:
        merchants.append(row)
    return JsonResponse(merchants, safe=False)

@csrf_exempt
def userenquiry(request):
    conn = Connect("127.0.0.1", "root", "", "msp")
    contactusername=request.POST['contactusername']
    contactemail=request.POST['contactemail']
    contactmessage=request.POST['contactmessage']
    query=f"insert into userenquiry values (Null ,'{contactusername}','{contactemail}','{contactmessage}')"
    cr=conn.cursor()
    cr.execute(query)
    conn.commit()
    return HttpResponse('1')

def carpenter(request):
    conn = Connect("127.0.0.1", "root", "", "msp")
    carpenter='Carpenter'
    query=f"select DISTINCT city from serviceproviders where category='{carpenter}'"
    cr=conn.cursor()
    cr.execute(query)
    result=cr.fetchall()
    c=[]
    for row in result:
        c.append(row[0])
    return render(request,'carpenter.html',{'ar':c})

def gotocarpenter(request):
    conn = Connect('127.0.0.1', 'root', '', 'msp')
    carpenter = 'Carpenter'
    city = request.GET['city']
    query1 = f"select * from serviceproviders where city='{city}' and category='{carpenter}'"
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

def electrician(request):
    conn = Connect("127.0.0.1", "root", "", "msp")
    electrician = 'Electrician'
    query = f"select DISTINCT city  from serviceproviders where category='{electrician}'"
    cr = conn.cursor()
    cr.execute(query)
    result = cr.fetchall()
    c = []
    for row in result:
        c.append(row[0])
    return render(request, 'electrician.html', {'ar': c})


def gotoelectrician(request):
    conn = Connect('127.0.0.1', 'root', '', 'msp')
    electrician = 'Electrician'
    city = request.GET['city']
    query1 = f"select * from serviceproviders where city='{city}' and category='{electrician}'"
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

def plumber(request):
    conn = Connect("127.0.0.1", "root", "", "msp")
    electrician = 'Plumber'
    query = f"select DISTINCT city  from serviceproviders where category='{electrician}'"
    cr = conn.cursor()
    cr.execute(query)
    result = cr.fetchall()
    c = []
    for row in result:
        c.append(row[0])
    return render(request, 'plumber.html', {'ar': c})


def gotoplumber(request):
    conn = Connect('127.0.0.1', 'root', '', 'msp')
    plumber = 'Plumber'
    city = request.GET['city']
    query1 = f"select * from serviceproviders where city='{city}' and category='{plumber}'"
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

def welder(request):
    conn = Connect("127.0.0.1", "root", "", "msp")
    welder = 'Welder'
    query = f"select DISTINCT city  from serviceproviders where category='{welder}'"
    cr = conn.cursor()
    cr.execute(query)
    result = cr.fetchall()
    c = []
    for row in result:
        c.append(row[0])
    return render(request, 'welder.html', {'ar': c})

def painter(request):
    conn = Connect("127.0.0.1", "root", "", "msp")
    painter = 'Painter'
    query = f"select DISTINCT city  from serviceproviders where category='{painter}'"
    cr = conn.cursor()
    cr.execute(query)
    result = cr.fetchall()
    c = []
    for row in result:
        c.append(row[0])
    return render(request, 'painter.html', {'ar': c})

def fitter(request):
    conn = Connect("127.0.0.1", "root", "", "msp")
    fitter = 'Fitter'
    query = f"select DISTINCT city  from serviceproviders where category='{fitter}'"
    cr = conn.cursor()
    cr.execute(query)
    result = cr.fetchall()
    c = []
    for row in result:
        c.append(row[0])
    return render(request, 'fitter.html', {'ar': c})


def usersignup(request):
    return render(request,'usersignup.html')

def logout(request):
        del request.session['useremail']
        return redirect(index)

# def logout2(request):
#     del request.session['merchantemail']
#     return redirect(merchantdashboaard)