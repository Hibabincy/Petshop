
# 1)option 1

# from django import forms

# class Regform(forms.Form):
#     FullName = forms.CharField(max_length = 25)
#     MobileNumber = forms.IntegerField()
#     Email = forms.EmailField()
#     Password = forms.CharField(max_length = 25)



# 2)option 2 ...by meta
# from django import forms
# from . models import Reg_tbl

# class Regform(forms.ModelForm):
#     class Meta:
#         fields = '__all__'
#         model = Reg_tbl
   

# 3)option 3 :call specific field names only instead of all 
# from django import forms
# from . models import Reg_tbl

# class Regform(forms.ModelForm):
#     class Meta:
#         fields = ['fnm','mob']
#         model = Reg_tbl


# 4)css kodukkan
from django import forms
from . models import Reg_tbl

class Regform(forms.ModelForm):
    class Meta:
        fields = ['fnm', 'mob', 'eml', 'psw', 'cpsw']
        model = Reg_tbl
        widgets = {
            'fnm' : forms.TextInput(attrs={'class':'form- control','placeholder':'Full Name','style':'width:500px;max;margin-top:20px;height:40px;margin-left:60px;border-color:lightblue;border-radius:5px;'}),
            'mob' : forms.NumberInput(attrs={'class':'form- control','placeholder':'Mobile Number','style':'width:500px;max;margin-top:20px;height:40px;margin-left:60px;border-color:lightblue;border-radius:5px;'}) , 
            'eml' : forms.EmailInput(attrs={'class':'form- control','placeholder':'Email Address','style':'width:500px;max;margin-top:20px;height:40px;margin-left:60px;border-color:lightblue;border-radius:5px;'}), 
            'psw' : forms.PasswordInput(attrs={'class':'form- control','placeholder':'Password','style':'width:500px;max;margin-top:20px;height:40px;margin-left:60px;border-color:lightblue;border-radius:5px;'}), 
            'cpsw': forms.PasswordInput(attrs={'class':'form- control','placeholder':'Confirm Password','style':'width:500px;max;margin-top:20px;height:40px;margin-left:60px;border-color:lightblue;border-radius:5px;'})  
             }
   