from django.shortcuts import render,redirect
from contact.models import book

# Create your views here.
def homepage(request):
    # msg=""
    # if 'user_id' in request.session:
    #     return redirect('/view-data')
    # if 'login' in request.POST:
    #     email=request.POST['email']
    #     password=request.POST['password']
    #     obj=book.objects.filter(email=email,password=password)
    #     if obj.count()==1:
    #         print("Sucess")
    #         row=obj.get()
    #         request.session['user_id']=row.id
    #         return redirect('/welcome')
    #     else:
    #         print("failure")
    #         msg="invalid email or password"
    return render(request,'home.html')
def contactpage(request):
    s=''
    if 'save' in request.POST:
        a_name=request.POST['name']
        a_email=request.POST['email']
        a_password=request.POST['password']
        a_contact=request.POST['contact']
        obj=book(
            name=a_name,
            email=a_email,
            password=a_password,
            contact=a_contact,
        )
        obj.save()
        s="Created"
        return redirect('/view-data')
       
    return render(request,'contact.html',{'s':s})
def view_data(request):
    con=book.objects.all()
    return render(request,'view-data.html',{'con':con})
def delete_data(request,del_id):
    print("Del==",del_id)
    book.objects.filter(id=del_id).delete()
    return redirect('/view-data')
def edit_data(request,edit_id):
    obj=book.objects.filter(id=edit_id).get()
    if 'save' in request.POST:
        a_name=request.POST['name']
        a_email=request.POST['email']
        a_password=request.POST['password']
        a_contact=request.POST['contact']
        obj.name=a_name
        obj.email=a_email
        obj.password=a_password
        obj.contact=a_contact
        obj.save()
        return redirect('/view-data')
    return render(request,'contact.html',{'obj':obj})
def insert(request,insert_id):
    obj=book.objects.filter(id=insert_id).get()
    j=''
    if 'submit' in request.POST:
        a_name=request.POST['name']
        a_email=request.POST['email']
        a_password=request.POST['password']
        a_contact=request.POST['contact']
        obj=book(
            name=a_name,
            email=a_email,
            password=a_password,
            contact=a_contact,
        )
        obj.save()
        j="Created"
        return redirect('/view-data/')  
    return render(request,'insert.html',{'j':j})
def login(request):
        msg=""
        if 'user_id ' in request.session:
            return redirect('/welcome')
        if 'login' in request.POST:
            email=request.POST['email']
            password=request.POST['password']
            obj=book.objects.filter(email=email,password=password)
            if obj.count()==1:
                print("suceess")
                row=obj.get()
                request.session['user_id']=row.id
                return redirect('/view-data/')  
            else:
                print("Failure")
                msg='invalid id or password'
        return render(request,'login.html',{'msg':msg})
def welcome(request):
    if 'user_id' not in request.session:
        return redirect('login/')
    user_id=request.session['user_id']
    print(user_id)
    return render(request,'welcome.html')
def logout(request):
    del request.session['user-id']
    return redirect(' http://127.0.0.1:8000/')

    
