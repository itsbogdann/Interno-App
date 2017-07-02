from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


class Furnizor(models.Model):
    nume = models.CharField(max_length=20)
    class Meta:
    	verbose_name = "Furnizor"
    	verbose_name_plural = "Furnizori"
    def __unicode__(self):
       return 'Furnizor: ' + self.nume

    def __str__(self):
        return self.nume

class Contract(models.Model):
    idFurnizor = models.ForeignKey(Furnizor, on_delete=models.CASCADE)
    dataIncepere = models.DateField(null=True)
    dataExpirare = models.DateField(null=True)
    obligatii = models.CharField(max_length=6000)
    dataEmitereFactura = models.DateField(null=True)
    tipCopie = models.BooleanField()
    modTrimitere = models.BooleanField()
    semnat = models.BooleanField()
    dataPlata = models.DateField(max_length=20)
    dataRapAct = models.DateField(max_length=20)
    dataRapInter = models.DateField(max_length=20)
    numefis = models.CharField(max_length=100)
    extensie = models.CharField(max_length=20)
    class Meta:
    	verbose_name = "Contract"
    	verbose_name_plural = "Contracte"
    def __unicode__(self):
       return 'Contract: #' + str(self.id)



class ContractCustom(models.Model):
    text = models.CharField(max_length=6000)
    class Meta:
    	verbose_name = "Contract Custom"
    	verbose_name_plural = "Contracte Custom"
    def __unicode__(self):
       return 'Contract Custom: #' + str(self.id)



class ModificareCustom(models.Model):
    idContract = models.ForeignKey(ContractCustom, on_delete=models.CASCADE)
    idUser = models.ForeignKey(User, on_delete=models.CASCADE)
    textBefore = models.CharField(max_length=6000)
    textAfter = models.CharField(max_length=6000)
    class Meta:
    	verbose_name = "Modificare Contract Custom"
    	verbose_name_plural = "Modificari Contract Custom"
    def __unicode__(self):
       return 'Modificare Custom: #' + str(self.id)


class Modificare(models.Model):
    idContract = models.ForeignKey(Contract, on_delete=models.CASCADE)
    idUser = models.ForeignKey(User, on_delete=models.CASCADE)
    dataModificare = models.DateTimeField(null=True)
    dataIncepereBefore = models.DateField(null=True)
    dataIncepereAfter = models.DateField(null=True)
    dataExpirareBefore = models.DateField(null=True)
    dataExpirareAfter = models.DateField(null=True)
    obligatiiBefore = models.CharField(max_length=6000, null=True)
    obligatiiAfter = models.CharField(max_length=6000, null=True)
    dataEmitereFacturaBefore = models.DateField(null=True)
    dataEmitereFacturaAfter = models.DateField(null=True)
    tipCopieBefore = models.NullBooleanField()
    tipCopieAfter = models.NullBooleanField()
    modTrimitereBefore = models.NullBooleanField()
    modTrimitereAfter = models.NullBooleanField()
    semnatBefore = models.NullBooleanField()
    semnatAfter = models.NullBooleanField(null=True)
    dataPlataBefore = models.DateField(max_length=20, null=True)
    dataPlataAfter = models.DateField(max_length=20, null=True)
    dataRapActBefore = models.DateField(max_length=20, null=True)
    dataRapActAfter = models.DateField(max_length=20, null=True)
    dataRapInterBefore = models.DateField(max_length=20, null=True)
    dataRapInterAfter = models.DateField(max_length=20, null=True)
    numefisBefore = models.CharField(max_length=100, null=True)
    numefisAfter = models.CharField(max_length=100, null=True)
    extensieBefore = models.CharField(max_length=20, null=True)
    extensieAfter = models.CharField(max_length=20, null=True)
    tip = models.CharField(max_length=6, null=True)
    class Meta:
    	verbose_name = "Modificare"
    	verbose_name_plural = "Modificari"
    def __unicode__(self):
       return 'Modificare: #' + str(self.id)
