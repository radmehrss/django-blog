from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django import forms
from django.contrib import messages
from website.forms import contact
from website.forms import ContactForm,NewsLetterForm

def index_view(request):
    context = {'title':'پر طرفدار','content':'این پایینیا بدجور پر طرفدارن'}
    return render(request,'website/index.html',context)
def about_view(request):
    return render(request,'website/about.html')

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'your message submited')
        else:
            messages.add_message(request,messages.ERROR,"your message didn't submited")
    form = ContactForm()
    return render(request,'website/contact.html',{'form':form})

def forms_view(request):
    if request.method =='POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('done')
        else:
            return HttpResponse('not valid')

    form = ContactForm()
    return render(request,'test.html',{'form':form})

def newsletter_view(request):
    if request.method == 'POST':
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')
        