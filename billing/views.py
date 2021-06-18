from django.shortcuts import get_object_or_404, render
from store.models import Category, Product,Risk
import re
# Create your views here.

def find_val(val):
    val=val.split(',')
    lst=[]
    l1=[]
    plantNum=[]
    plantQua=[]
    plantNam=[]
    plantPhoto=[]
    allplant=[]
    plantPrice=[]
    SNo=[]
    count=1
    for i in val:
        a=re.split('-',i)
        plantNum.append(int(a[0]))
        SNo.append(count)
        count+=1
        try:
            plantQua.append(int(a[1]))
        except:
            plantQua.append(1)
    lst.append(SNo)
    lst.append(plantNum)
    tot=sum(plantQua)
    for j in plantNum:
      for i in Product.objects.all():
        if (j == i.pid):
          plantNam.append(i.title)
          plantPhoto.append(i.image.url)
          plantPrice.append(i.price)
          break
    lst.append(plantNam)
    lst.append(plantQua)
    lst.append(plantPhoto)
    lst.append(plantPrice)
    price=0
    for i in range(len(plantQua)):
      price+=plantQua[i]*plantPrice[i]
    return zip(lst[0],lst[1],lst[2],lst[3],lst[4],lst[5]), tot, price



def plantfinder(request):
    return render(request,'store/plantfinder.html')

def plantlist(request):
    val=request.POST['plantnumb']
    lst,l2,price=find_val(val)
    return render(request,'store/plantlist.html',{'plantID':lst,'l2':l2,'price':price})

def local(request):
  pid=[]
  name=[]
  photo=[]
  for i in Product.objects.order_by('pid'):
    name.append(i.Nickname)
    pid.append(i.pid)
    photo.append(i.image.url)
  prod=zip(pid,name,photo)
  return render(request,'store/local.html',{'prod':prod})
