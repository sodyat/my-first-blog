from django.shortcuts import render
 from django.shortcuts import HttpResponse

 def show_blog(request):

     return HttpResponse(u'Hello World')

