from django.shortcuts import render,redirect,HttpResponse
from .models import Orcamento
from .forms import OrcamentoForm
from django.contrib import messages
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
            messages.success(request,'Orçamento cadastrado com sucesso')
            return redirect('index')        
    else:
        return render(request,"oficina2/cadastro.html")

def pesquisa(request):
    return render(request,'oficina2/pesquisa.html')

def orcamentos(request):
    if request.method == 'GET':
        orcamentos = Orcamento.objects.all()
        return render(request,'oficina2/orcamentos.html',{'orcamentos':orcamentos})
    else:
        tipo = request.POST['tipo']
        orcamentos = Orcamento.objects.all().order_by(tipo)
        return render(request, 'oficina2/orcamentos.html', {'orcamentos': orcamentos})

def orcamento(request,orcamento_id):
    orcamento = Orcamento.objects.get(id=orcamento_id)
    return render(request,'oficina2/orcamento.html',{'orcamento':orcamento})

def edit_orcamento(request,orcamento_id):
    orcamento = Orcamento.objects.get(id=orcamento_id)
    form_v = OrcamentoForm(instance=orcamento)
    if request.method == 'POST':
        form = OrcamentoForm(instance=orcamento,data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Orçamento editado com sucesso')
            return redirect('index')
    else:
        return render(request,'oficina2/orcamento_edit.html',{'form':form_v,'orcamento':orcamento})

def excluir_orcamento(request,orcamento_id):
    if request.method == 'POST':
        obj = Orcamento.objects.get(id=orcamento_id)
        obj.delete()
        messages.success(request,'Orcamento deletado com sucesso')
        return redirect('index')
    else:
        return redirect('index')