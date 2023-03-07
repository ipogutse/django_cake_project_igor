from django.shortcuts import render

# Create your views here.
def setcookie(request):
    response=render(request,'setcookie.html')
    #instead of returning it, we will save it in a response variable
    response.set_cookie('name','django')
    return response

def getcookie(request):
    nm=request.COOKIES['name']
    return render(request,'getcookie.html',{'xyz':nm})

def delcookie(request):
     response=render(request,'delcookie.html')
     response.delete_cookie('name')
     return response


def session_store(request):
    # Store a value in the session
    request.session['session_key1'] = 'session_value1'
    return render(request,'session_store.html',{'xyz':'session_value1'})
    
def session_get(request):
    # Retrieve a value from the session
    my_value = request.session.get('session_key1')
    return render(request,'session_get.html', {'xyz':my_value})
    
def session_del(request):
    # Remove a value from the session
    del request.session['session_key']
    return render(request,'session_del.html', {'xyz':'session_key'})
    
