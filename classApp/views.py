from django.shortcuts import render
from django. shortcuts import render, redirect 
from django. views. generic import ListView, DetailView, CreateView, DeleteView, UpdateView 
from django. urls import reverse_lazy 
from django. contrib. auth. models import User 
from django. db import IntegrityError
from django.core.exceptions import ValidationError
from django. contrib. auth import authenticate, login ,logout 

from .models import PersonalDataModel 
from .forms import  PersonalDataForm 

def make_context( md, ctx ):
        
        labels= PersonalDataForm.LABELS

        # インスタンスの各フィールドの値を取得
        fields = md._meta.get_fields()
        objcect2 =[]

        for field in fields:
            field_name = field.name
            field_value = getattr( ctx["object"], field_name)
            print(f"{field_name}: {field_value}")

            lbl_name = ""
            if field_name in labels:       
                lbl_name = labels[field_name]

            value = field_value
            if type(value) is list:
                value = "、".join(value)
                
            objcect2.append( {"name": lbl_name, "value":value})
        
        ctx["obj2"] = objcect2
        return ctx


class PersonalList( ListView ):
    model = PersonalDataModel 
    # テンプレートは、PersonalDataModel_list.html

class PersonalDetail( DetailView ):
    model = PersonalDataModel 
    # テンプレートは、PersonalDataModel_detail.html

    def get_context_data(self, **kwargs):

        ctx = super().get_context_data(**kwargs)
        ctx =make_context( PersonalDataModel, ctx )
        return ctx

class PersonalDelete( DeleteView ): 
    model = PersonalDataModel
    # テンプレートは、PersonalDataModel_confirm_delete.html
    success_url = reverse_lazy('list_url')

    def get_context_data(self, **kwargs):

        ctx = super().get_context_data(**kwargs)
        ctx =make_context( PersonalDataModel, ctx )
        return ctx


# テンプレートは、PersonalDataModel_form.html
class PersonalCreate(CreateView):
    model = PersonalDataModel 
    form_class = PersonalDataForm
    success_url = reverse_lazy('list_url')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['label_suffix'] = ''
        return kwargs    

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["title"] = "登録"
        return ctx

# テンプレートは、PersonalDataModel_form.html
class PersonalUpdate(UpdateView):
    model = PersonalDataModel 
    form_class = PersonalDataForm
    success_url = reverse_lazy('list_url')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["title"] = "修正"
        return ctx





