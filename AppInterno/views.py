from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.core.urlresolvers import reverse
from django.views.generic.edit import DeleteView, UpdateView
from django.views.generic.list import ListView
from django.contrib.auth.models import User, Group
from .models import Contract
from .models import Furnizor
from .models import Modificare
import datetime
from django.http import JsonResponse
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist

from django.core.mail import send_mail
from django.http import HttpResponse
from django.core.mail import EmailMessage

# cod de trimis mail
# email = EmailMessage('title', 'body', to=['dearhitectura17@gmail.com'])
# email.send()

from django.http import HttpResponse

from . import models
from . import forms
from itertools import chain

import json


def edit(request):
    if request.is_ajax():
        message = "Yes, AJAX!"
    else:
        message = "Not Ajax"
    return HttpResponse(message)


def index(request):
    ad = ""
    mng = ""
    contexthome = {}
    lista_contracte = models.Contract.objects.all()
    contexthome['lista'] = lista_contracte
    contexthome['nume_fisier'] = "pdftest"

    if request.POST.get('sterg') == 'da':
        contract = Contract(id=request.POST.get('id'))
        user_curent=request.user
        modificare = Modificare(idContract=contract, idUser=user_curent, dataModificare=datetime.datetime.now(),tip='sterg')
        modificare.save()
        contract.delete()
        response_data={}
        response_data['id'] = contract.id
        response_data['msg']='STERS'
        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )

    if request.method == 'POST':


        contract_id = request.POST.get('id')
        contract_obligatii=request.POST.get('obligatii')
        contract_incepere = request.POST.get('data_incepere')
        contract_expirare = request.POST.get('data_expirare')
        contract_platii = request.POST.get('data_platii')
        contract_rap_inter = request.POST.get('data_rap_inter')
        contract_rap_act = request.POST.get('data_rap_act')
        contract_emitere_factura = request.POST.get('data_emitere_factura')
        contract_semnat = request.POST.get('semnat')
        contract_tip_copie = request.POST.get('tip_copie')
        contract_mod_trimitere = request.POST.get('mod_trimitere')
        contract_obligatii2=request.POST.get('obligatii2')
        contract_incepere2 = request.POST.get('data_incepere2')
        contract_expirare2 = request.POST.get('data_expirare2')
        contract_platii2 = request.POST.get('data_platii2')
        contract_rap_inter2 = request.POST.get('data_rap_inter2')
        contract_rap_act2 = request.POST.get('data_rap_act2')
        contract_emitere_factura2 = request.POST.get('data_emitere_factura2')
        contract_semnat2 = request.POST.get('semnat2')
        contract_tip_copie2 = request.POST.get('tip_copie2')
        contract_mod_trimitere2 = request.POST.get('mod_trimitere2')
        furnizor_id=request.POST.get('furnizor')
        furnizor=request.POST.get('nume_furnizor')
        contract_numefis=request.POST.get('numefis')
        contract_extensie=request.POST.get('extensie')
        contract_fis=request.POST.get('numefis2')
        contract_ext=request.POST.get('extensie2')


        user_curent=request.user

        response_data = {}

        if contract_fis is None:
          contract_fis=contract_numefis
          contract_ext=contract_extensie

        furnizor = Furnizor(id=furnizor_id,nume=furnizor)

        contract = Contract(id=contract_id,idFurnizor=furnizor,dataIncepere=contract_incepere2,dataExpirare=contract_expirare2,obligatii=contract_obligatii2,
                            dataPlata=contract_platii2,dataRapInter=contract_rap_inter2,dataRapAct=contract_rap_act2,dataEmitereFactura=contract_emitere_factura2,
                            tipCopie=contract_tip_copie2,semnat=contract_semnat2,modTrimitere=contract_mod_trimitere2,numefis=contract_fis,extensie=contract_ext)

        contract.save()

        modificare = Modificare(idContract=contract,idUser=user_curent,dataModificare=datetime.datetime.now(),dataIncepereBefore=contract_incepere,
                                dataIncepereAfter=contract_incepere2,dataExpirareBefore=contract_expirare,dataExpirareAfter=contract_expirare2,
                                obligatiiBefore=contract_obligatii,obligatiiAfter=contract_obligatii2,dataEmitereFacturaBefore=contract_emitere_factura,dataEmitereFacturaAfter=contract_emitere_factura2,
                                tipCopieBefore=contract_tip_copie,tipCopieAfter=contract_tip_copie2,modTrimitereBefore=contract_mod_trimitere,modTrimitereAfter=contract_mod_trimitere2,
                                semnatBefore=contract_semnat,semnatAfter=contract_semnat2,dataPlataBefore=contract_platii,dataPlataAfter=contract_platii2,dataRapActBefore=contract_rap_act,
                                dataRapActAfter=contract_rap_act2,dataRapInterBefore=contract_rap_inter,dataRapInterAfter=contract_rap_inter2,numefisBefore=contract_numefis,numefisAfter=contract_fis,
                                extensieBefore=contract_extensie,extensieAfter=contract_ext,tip='modif')

        modificare.save()

        response_data['id'] = contract.id
        response_data['numefis']=contract.numefis
        response_data['extensie']=contract.extensie
        response_data['incepere'] = contract.dataIncepere
        response_data['expirare'] = contract.dataExpirare
        response_data['obligatii'] = contract.obligatii
        response_data['emitere_factura'] = contract.dataEmitereFactura
        response_data['plata']=contract.dataPlata
        response_data['rap_act']=contract.dataRapAct
        response_data['rap_inter']=contract.dataRapInter
        response_data['semnat']=contract.semnat
        response_data['tip_copie']=contract.tipCopie
        response_data['mod_trimitere']=contract.modTrimitere

        json.dumps(response_data)

        return HttpResponse(
          json.dumps(response_data),
          content_type="application/json"
         )

    return render(request, 'AppInterno/home.html', contexthome)


def login_view(request):
    context = {}
    adm = 0
    mng = 0

    if request.method == 'GET':
        form = forms.LoginForm()
    elif request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            usr = form.cleaned_data['username']
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'])

            # daca utilizatorul este in grupul de admini:
            if (is_member(usr) == 1):
                adm = 1
            else:
                adm = 0
            '''
            #daca este manager de proiect
            if (is_member2(usr) == 1):
                mng = 1
            else:
                mng = 0
            '''
            request.session['adm'] = adm

            request.session['mng'] = mng



            if user:
                login(request=request, user=user)
                return redirect('index')
            else:
                context['error_message'] = 'Date incorecte!'

    context['form'] = form
    return render(request, 'AppInterno/login.html', context)
    
def is_member(user):
    gr = Group.objects.get(name="Administrator").user_set.all()
    este_in_lista = gr.filter(username=user).exists()
    return este_in_lista
'''
def is_member2(user):
    gr = Group.objects.get(name="Manager").user_set.all()
    este_in_lista = gr.filter(username=user).exists()
    return este_in_lista
'''
def deleteContract(request, del_id):
    #to_delete = get_object_or_404(Contract, pk=del_id).delete()
    return redirect('index')

def logout_view(request):
    if request.method == 'GET':
        logout(request)
        return redirect('index')

def statistici_view(request):
    context = {}
    form = forms.StatisticiForm
    context['form'] = form
    if request.method == 'GET':
        #print(request.GET)
        if 'stat1' in request.GET:
            #form = forms.ContractePlataLunaForm(request.GET['an'])
            #an = form['an']
            an = request.GET['an']
            print(an)
            contracte = models.Contract.objects.all()
            luni = set([c.dataPlata.strftime("%Y-%m-%d")[5:7] for c in contracte if c.dataPlata.strftime("%Y-%m-%d")[:4] == an])
            print(luni)
            lista_contracte_luna = []
            for l in luni:
                if sum(1 for c in contracte if c.dataPlata.strftime("%Y-%m-%d")[5:7] == l) != 0:
                    lista_contracte_luna.append([l, str(sum(1 for c in contracte if c.dataPlata.strftime("%Y-%m-%d")[5:7] == l))])
                print(lista_contracte_luna)
            context['lista_contracte_luna'] = lista_contracte_luna
        if 'stat2' in request.GET:
            an = request.GET['an']
            print(an)
            contracte = models.Contract.objects.all()
            luni = set([c.dataPlata.strftime("%Y-%m-%d")[5:7] for c in contracte if
                    c.dataPlata.strftime("%Y-%m-%d")[:4] == an])
            lista_contracte_luna = []
            for l in luni:
                if sum(1 for c in contracte if c.dataIncepere.strftime("%Y-%m-%d")[5:7] == l) !=0:
                    lista_contracte_luna.append(
                        [l, str(sum(1 for c in contracte if c.dataIncepere.strftime("%Y-%m-%d")[5:7] == l))])
                print(lista_contracte_luna)
            context['lista_contracte_luna'] = lista_contracte_luna
    else:
        context = {}
    return render(request, 'AppInterno/statistici.html', context)


def istoric_view(request):
    context = {}
    listaModificari = models.Modificare.objects.all()
    context['listaModificari'] = listaModificari
    return render(request, 'AppInterno/istoric.html', context)
