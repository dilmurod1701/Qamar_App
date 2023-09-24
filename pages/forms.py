from django import forms
from .models import Category, products

choices = Category.objects.all().values_list('name', 'name')
choice_list = []
for i in choices:
    choice_list.append(i)


class PostForm(forms.ModelForm):
    class Meta:
        model = products
        fields = ['product_img', 'product_name', 'description', 'category', 'price', 'phone_number', 'location']
        widgets = {
            'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'})
        }
