from django.shortcuts import render,redirect,HttpResponse
from .models import Orcamento
from .forms import OrcamentoForm

# Create your views here.
def index(request):
    return render(request,"oficina2/index.html")

def cadastro(request):
    if request.method == 'POST':
        try:
            obj = Orcamento.objects.create(cliente=request.POST['cliente'],datahora=request.POST['datahora'],descricao=request.POST['descricao'],valor=request.POST['valor'],vendedor=request.POST['vendedor'])
        except Exception as err:
            return HttpResponse(f'{err}')
        else:
            return redirect('index')        
    else:
        return render(request,"oficina2/cadastro.html")

def pesquisa(request):
    return render(request,'oficina2/pesquisa.html')

def orcamentos(request):
    orcamentos = Orcamento.objects.all()
    return render(request,'oficina2/orcamentos.html',{'orcamentos':orcamentos})

def orcamento(request,orcamento_id):
    orcamento = Orcamento.objects.get(id=orcamento_id)
    if request.method = 'POST':
        form = OrcamentoForm(instance=Orcamento)
    return render(request,'oficina2/orcamento.html',{'orcamento':orcamento})