from django.shortcuts import render,redirect
from . models import Reg_tbl,pet_tbl,cart_tbl
from random import randint
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from . forms import Regform
# Create your views here.

def index(request):
    return render(request,'index.html')


def signup(request):
    if request.method == 'POST':
      fname= request.POST.get('name')
      mobile= request.POST.get('mobile')
      email= request.POST.get('mail')
      password= request.POST.get('pass')
      cpassword= request.POST.get('cpass')
      obj= Reg_tbl.objects.create(fnm=fname,mob=mobile,eml=email,psw=password,cpsw=cpassword)
      obj.save()
      if obj:
        # return render(request,'login.html')
        return redirect("/log")
      else:
        return render(request,'signup.html')
    return render(request,'signup.html')

def login(request):
  if request.method =='POST':
    email=request.POST.get('name')
    pas=request.POST.get('pas')
    obj= Reg_tbl.objects.filter(eml=email, psw=pas)
    if obj:
      request.session['ema']=email
      request.session['psa']=pas
      for m in obj:
        idl = m.id
      request.session['idn']=idl
      return render(request,'home.html')  
    else:
      msg = 'Invalid Credentials'
      return render(request,'login.html',{"error":msg}) 
  return render(request,'login.html')    
 

def changepass(request):
    return render(request,'changepassword.html')  

def users(request):
  obb=Reg_tbl.objects.all()
  return render(request,'users.html',{"data":obb})  

def edit(request,pk):
  ob=Reg_tbl.objects.filter(id=pk)
  if request.method=='POST':
    fnm=request.POST.get('fn')
    idl=request.POST.get('idn')
    email=request.POST.get('em')
    mob=request.POST.get('mb')
    pas=request.POST.get('ps')
    obc=Reg_tbl.objects.filter(id=idl)
    obc.update(fnm=fnm, mob=mob, eml=email, psw=pas)
    return redirect("/users")

  return render(request,"oneuser.html",{"data":ob})        

def delete(request,pk):
  obt=Reg_tbl.objects.filter(id=pk)
  obt.delete()
  return redirect("/users")
  
def addpets(request):
  if request.method=='POST':
    pname=request.POST.get('pn')
    pimag=request.FILES.get('im')
    price=request.POST.get('pr')
    desc=request.POST.get('ds')
    obj=pet_tbl.objects.create(pnm=pname,pim=pimag,prc=price,des=desc)
    obj.save()
    return render(request,'addpets.html',{'msg':'details uploaded..'})
  return render(request,"addpets.html") 

def allpets(request):
  pob=pet_tbl.objects.all()
  return render(request,'allpets.html',{"data":pob}) 

def addtocart(request,pid):
  pobj=pet_tbl.objects.get(id=pid)
  cid=request.session['idn']
  cobj=Reg_tbl.objects.get(id=cid)
  cartitem,created=cart_tbl.objects.get_or_create(customer=cobj,product=pobj)
  if not created:
    cartitem.qty+=1
    cartitem.save()
    messages.success(request,"quandity incremented...")  
  messages.success(request,"item added to cart...")  
  return redirect('/allpets')
                     
def viewcart(request):
  idn = request.session['idn']
  cobj = Reg_tbl.objects.get(id=idn)
  cartobj = cart_tbl.objects.filter(customer=cobj)
  if cartobj:
    total_price = 0
    for m in cartobj:
      pro = m.product.prc*m.qty
      total_price+=pro
    return render(request,"cart.html",{"cartitem":cartobj,"total":total_price})  
  else:
    return render(request,"cart.html",{"em":"Your cart is empty.."})
    # message.success(request,"Your cart is empty") 
    # return redirect("/viewcart")

def cartdelete(request,cid):
  cartobj=cart_tbl.objects.filter(id=cid)
  cartobj.delete()
  return redirect("/viewcart")

def sendmail(request):
  if request.method=='POST':
    em=request.POST.get('em')
    sb=request.POST.get('sb')
    msg=request.POST.get('msg')
    send_mail(sb,msg,settings.EMAIL_HOST_USER,[em],fail_silently=False)
    return render(request,'email.html',{"success":"Mail send successfully..."}) 
  return render(request,'email.html')

def formview(request):
  form = Regform()
  if request.method == 'POST':
    form = Regform(request.POST)
    if form.is_valid():
      fn = form.cleaned_data.get('fnm')
      mb = form.cleaned_data.get('mob')
      em = form.cleaned_data.get('eml')
      ps = form.cleaned_data.get('psw')
      cps = form.cleaned_data.get('cpsw')
      obz = Reg_tbl.objects.create(fnm=fn,mob=mb,eml=em,psw=ps,cpsw=cps)
      obz.save()
      if obz:
        msg = 'Registration successful...'
        return render(request,'formview.html',{"form":form,"success":msg})
  return render(request,'formview.html',{"form":form})











  # .order_by('-id')