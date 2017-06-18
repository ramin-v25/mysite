


from django.http import HttpResponse



def metode(request,params):
    return HttpResponse(params)


a=raw_input("plese select name?")


metode('',a)
