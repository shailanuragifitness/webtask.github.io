from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request, 'base.html')
# def chest(request):
#     return HttpResponse("this is chest page")

def back(request):
    return render(request, 'back.html')
def trisep(request):
    return render(request, 'trisep.html')
def bicep(request):
    return render(request, 'bicep.html')
def shoulder(request):
    return render(request, 'shoulder.html')
def thigh(request):
    return render(request, 'thigh.html')    
def abs(request):
    return render(request, 'abs.html')
def trap(request):
    return render(request, 'trap.html')
def chest(request):
    return render(request, 'chest.html')
def chest(request):
    return render(request, 'chest.html')


def nutrition(request):
    return render(request, 'nutrition.html')
def vitamin(request):
    return render(request, 'vitamin.html')
def supplement(request):
    return render(request, 'supplement.html')
def wgain(request):
    return render(request, 'wgain.html')
def wloss(request):
    return render(request, 'wloss.html')
def mgain(request):
    return render(request, 'mgain.html')

def scare(request):
    return render(request, 'scare.html')
def hcare(request):
    return render(request, 'hcare.html')
def makeup(request):
    return render(request, 'makeup.html')
def nail(request):
    return render(request, 'nail.html')


def family(request):
    return render(request, 'family.html')
def pet(request):
    return render(request, 'pet.html')
def relationship(request):
    return render(request, 'relationship.html')
def style(request):
    return render(request, 'style.html')
def sex(request):
    return render(request, 'sex.html')
def money(request):
    return render(request, 'money.html')
def lifehack(request):
    return render(request, 'lifehack.html')



def chronicpain(request):
    return render(request, 'chronicpain.html')
def backpain(request):
    return render(request, 'backpain.html')
def msoreness(request):
    return render(request, 'msoreness.html')
def mgproblem(request):
    return render(request, 'mgproblem.html')
def digestive(request):
    return render(request, 'digestive.html')
def heart(request):
    return render(request, 'heartproblem.html')





def basic(request):
    return render(request, 'basic.html')
