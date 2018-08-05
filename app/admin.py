from django.contrib import admin
from django import forms
from app.models import Participantes

class ParticipantesAdminForm(forms.ModelForm):

    class Meta:
        model = Participantes
        fields = '__all__'


class ParticipantesAdmin(admin.ModelAdmin):
    form = ParticipantesAdminForm
    list_display = ['name', 'email', 'empresa', 'profissao', 'area_atuacao', 'foto']
    # readonly_fields = ['name', 'email', 'empresa', 'profissao', 'area_atuacao', 'foto']

admin.site.register(Participantes, ParticipantesAdmin)

