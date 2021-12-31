from app.models import returned_papers
from django.urls import path
from . import views

urlpatterns = [
    path('',views.login,name='Login'),
    path('Candidate_dash',views.candidate_dash,name='Candidate_dashboard'),
    path('Organiser_dash',views.organiser_dash,name='Organiser_dashboard'),
    path('Reviewer_dash',views.reviewer_dash,name='Reviewer_dashboard'),
    path('sentreviewer/<int:id>',views.paper_message),
    path('submitted',views.submitpaper,name='Submitted'),
    path('sentsuccessfully',views.senttoreviewer,name='sentsucess'),
    path('sentorganiser/<int:id>',views.acceptpaper,name='senttoorganiser'),
    path('sentsuccess',views.acceptfinal,name='sentorganiser'),
    path('reviewedpapers',views.reviewedpapers,name='reviewedpapers'),
    path('sentcandidate/<int:id>',views.sendcandidate,name='sendcandidate'),
    path('paymentdetails',views.payment_details,name='paymentdetails'),
    path('sendcandidatefinal',views.sendcandidatefinal,name='sendcandidatefinal'),
    path('returnedpaers',views.returnedpapers,name='returnedpapers'),
    path('payments/<int:id>',views.makepayment,name='payment'),
    path('paidsucessfully',views.paidsuccess,name='paid')
    
]