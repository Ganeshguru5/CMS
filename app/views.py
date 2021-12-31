from typing import ContextManager
from django.http import request
from django.shortcuts import render
from .models import Candidate_details,Organiser_details,Reviewer_details, returned_papers,submitted_papers,selected_paper,reviewed_papers,paymentdetails

# Create your views here.
def login(request):
    return render(request,'loginoption.html')

def dashlogin(request):
    if request.method =='POST':
      if  request.POST['position']=='candidate':
          candidate_dash()


def organiser_dash(request):
    if request.method =='POST':
        username=request.POST['username']
        password=request.POST['password']
        if Organiser_details.objects.filter(username=username).exists() and Organiser_details.objects.filter(password=password).exists():
            context={'papers':submitted_papers.objects.all()}
            return render(request,'organiser_dashboard.html',context)

def reviewer_dash(request):
    if request.method =='POST':
        username=request.POST['username']
        password=request.POST['password']
        if Reviewer_details.objects.filter(username=username).exists() and Reviewer_details.objects.filter(password=password).exists():
            context={'papers':selected_paper.objects.all()}
            return render(request,'reviewer_dashboard.html',context)

def candidate_dash(request):
    if request.method =='POST':
        username=request.POST['username']
        password=request.POST['password']
        if Candidate_details.objects.filter(username=username).exists() and Candidate_details.objects.filter(password=password).exists():
            return render(request,'candidate_dashboard.html',)

def submitpaper(request):
    if request.method=='POST':
        savepaper=submitted_papers()
        savepaper.Name=request.POST.get('Name')
        savepaper.Topic=request.POST.get('Topic')
        savepaper.Url=request.POST.get('Url')
        savepaper.Department=request.POST.get('Department')
        savepaper.emaiid=request.POST.get('emailid')
        savepaper.save()
        return render(request,'candiadate_success.html')



def paper_message(request,id):
    context={'paper':submitted_papers.objects.get(id=id)}
    return render(request,'sent_to_reviewer.html',context)

def senttoreviewer(request):
    if request.method=='POST':
        savepaper=selected_paper()
        savepaper.Name=request.POST.get('Name')
        savepaper.Topic=request.POST.get('Topic')
        savepaper.Url=request.POST.get('Url')
        savepaper.Department=request.POST.get('Department')
        savepaper.emaiid=request.POST.get('emailid')
        savepaper.Reviewer=request.POST.get('reviewer')
        savepaper.save()
        return render(request,'sent_to_reviewer.html')

def acceptpaper(request,id):
    context={'paper':selected_paper.objects.get(id=id)}
    return render (request,'sent_to_organiser.html',context)

def acceptfinal(request): 
    if request.method=='POST':
        savepaper=reviewed_papers()
        savepaper.Name=request.POST.get('Name')
        savepaper.Topic=request.POST.get('Topic')
        savepaper.Url=request.POST.get('Url')
        savepaper.Department=request.POST.get('Department')
        savepaper.emaiid=request.POST.get('emailid')
        savepaper.comment=request.POST.get('comment')
        savepaper.save()
        return render(request,'sent_to_organiser.html')

def reviewedpapers(request):
    context={'papers':reviewed_papers.objects.all()}
    return render(request,'reviewed_papers.html',context)

def sendcandidate(request,id):
    context={'paper':reviewed_papers.objects.get(id=id)}
    return render(request,'sent_to_candidate.html',context)

def payment_details(request):
    context={'papers':paymentdetails.objects.all()}
    return render (request,'payment_details.html',context)
def sendcandidatefinal(request):
    savepaper=returned_papers()
    savepaper.Name=request.POST.get('Name')
    savepaper.Topic=request.POST.get('Topic')
    savepaper.Url=request.POST.get('Url')
    savepaper.Department=request.POST.get('Department')
    savepaper.emaiid=request.POST.get('emailid')

    savepaper.save()
    return render(request,'sent_to_candidate.html')

def returnedpapers(request):
    context={'papers':returned_papers.objects.all()}
    return render (request,'returned_papers.html',context)

def makepayment(request,id):
    context={'paper':reviewed_papers.objects.get(id=id)}
    return render(request,'payment.html',context)

def paidsuccess(request):
    savepaper=paymentdetails()
    savepaper.Name=request.POST.get('Name')
    savepaper.Topic=request.POST.get('Topic')
    savepaper.emaiid=request.POST.get('emaiid')
    savepaper.amountpaid=request.POST.get('amountpaid')
    savepaper.card_number=request.POST.get('card_number')

    savepaper.save()
    return render(request,'payment.html')