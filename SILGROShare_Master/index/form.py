from django import forms
from .models import *
class ProductForm(forms.Form):
    name = forms.CharField(max_length=20,label='name')
    weight = forms.CharField(max_length=50,label='weight')
    size = forms.CharField(max_length=50,label='size')
    choices_list = [(i+1,v['type_name']) for i,v in enumerate(Type.objects.values('type_name'))]
    type = forms.ChoiceField(choices = choices_list,label='type')

class Listings(forms.Form):
    description = models.TextField(max_length=1000)
#自定义验证函数
def weight_validate(value):
    if not str(value).isdigit():
        raise ValueError('Please input again!')


