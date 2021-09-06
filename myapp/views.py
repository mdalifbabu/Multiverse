from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
import os
from django.conf import settings

# Create your views here.
def home(request):
    return render(request, 'first/home.html', {'key':'home'})

def about(request):
    return render(request, 'first/about.html', {'key':'about'})

def contact(request):
    return render(request, 'first/contact.html', {'key':'contact'})


def calculator(request):
    # ans = 0
    # if request.method == 'POST':
    #     n1 = request.GET['n1']
    #     n2 = request.GET['n2']
    #     op = request.GET['operator']

    #     print(n1)
    #     if op == 'sum':
    #         ans = n1+n2
    #     elif op == 'sub':
    #         ans = n1-n2
    #     elif op == 'mul':
    #         ans = n1*n2
    #     elif op == 'div':
    #         ans = n1/n2
    
    # print('alif')
    # if ans == 0:      
    #     return render(request, 'first/calculator.html', {'key':'calculator'})
    # else:
    #     return render(request, 'first/calculator.html', {'key':'calculator', 'ans':ans})
    return render(request, 'first/calculator.html', {'key':'calculator'})


def replace_text(request):
    url = "/"
    if request.method == 'POST':
        first_word = request.POST['replaceable']
        second_word = request.POST['toreplace']
        uploaded_file = request.FILES['document']
        print(first_word, second_word)
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        url = fs.url(name)
  
        text = open(os.path.join(settings.MEDIA_ROOT, uploaded_file.name), 'r').read().replace(first_word, second_word)
        print(text)
        with open('D:\Replace.txt', 'w') as f:
            f.write(text)

    context = {
        'url' : url,
        
        'key' : 'replace_text',
    }
    return render(request, 'first/replace_text.html', context)

def calculate(request):
    n1 = int(request.GET["n1"])
    n2 = int(request.GET["n2"])
    op = request.GET["operator"]
    
    if op == 'sum':
        res = n1+n2
    elif op == 'sub':
        res = n1-n2
    elif op == 'mul':
        res = n1*n2
    elif op == 'div':
        res = n1/n2
    else:
        res = 'Error'
    return render(request, 'first/calculate.html', {'res' : res, 'k' : op, 'key':'calculator'})

def result(request):
    name = request.GET["name"]
    email = request.GET["email"]
    password = request.GET["pwd"]
    message = request.GET["message"]

    flag = False
    if password[0] >= '0' and password[0] <= '9': 
        flag = True

    if len(password) < 8:
        flag = True
    #print(password)

    up = lo = nu = sp = 0
    for c in password:
        #print(c)
        if c >= 'a' and c <= 'z': lo += 1
        elif c >= 'A' and c <= 'Z': up += 1
        elif c >= '0' and c <= '9': nu += 1
        else: sp += 1
    
    if lo == 0 or up == 0 or nu == 0 or sp == 0:
        flag = True
        #print('Alif')
    return render(request, 'first/result.html', {'name' : name, 'email' : email, 'message' : message, 'flag' : flag, 'key' : 'contact'})