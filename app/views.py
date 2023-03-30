from django.shortcuts import render,redirect
from django.http import HttpResponse
from yahoo_fin.stock_info import *
from threading import Thread
import queue
from asgiref.sync import sync_to_async
from .forms import *
from django.views import View
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request,"home.html")


def login(request):
    if request.user.is_authenticated:
        return redirect("/stockpicker/")
    return render(request, "login.html")

class RegistrationView(View):
    def get(self, request):
        form = RegistrationForm()
        return render(request, "registration.html", {"form": form})
    
    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "congratulations! Registred successfully!!")
        return render(request, "registration.html", {"form": form})

@login_required
def stock_picker(request):
    stk_pikr = tickers_nifty50()
    print(stk_pikr)
    return render(request, 'stockpicker.html', {'context': stk_pikr})


# @sync_to_async
# def checkAuthenticated(request):
#     if not request.user.is_authenticated:
#         return False
#     else:
#         return True

@login_required
def stock_tracker(request):
    selected_stocks = request.GET.getlist('stockpicker')
    stockshare=str(selected_stocks)[1:-1]
    data = {}
    all_stocks = tickers_nifty50()
    for i in selected_stocks:
        if i in all_stocks:
            pass
        else:
            return HttpResponse('ERROR')
        
    n_threads = len(selected_stocks)
    thread_list = []
    que = queue.Queue()


    # for i in selected_stocks:
    #     result = get_quote_table(i)
    #     data.update({i:result})
    for i in range(n_threads):
        thread = Thread(target=lambda q, arg1:q.put({selected_stocks[i]: get_quote_table(arg1)}) , args=(que, selected_stocks[i]))
        thread_list.append(thread)
        thread_list[i].start()
        print("########################",thread_list[i])
    print("######################## Forloop Ran")
    print("######################### Thread List2",thread_list )

    for thread in thread_list:
        thread.join()

    while not que.empty():
        result = que.get()
        data.update(result)

    print(">>>>>>>>>>>>>>>>>> DATA",data)
    return render(request, 'stocktracker.html', {'context': data, 'room_name': 'track','selectedstock':stockshare})