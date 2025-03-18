from django.db import models
import os

from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        abstract = True


class Region(BaseModel):
    title = models.CharField(max_length=50,validators=[RegexValidator(r"^[A-Z][a-zA-Z]{2,24}$", "Title faqat harflardan iborat bo‘lishi va bosh harfi katta bo‘lishi kerak!")])


    def __str__(self):
        return self.title
    




class Departament(BaseModel):
    d_title = models.CharField(max_length=50,validators=[RegexValidator(r"^[A-Z][a-zA-Z]{2,24}$", "Title faqat harflardan iborat bo‘lishi va bosh harfi katta bo‘lishi kerak!")])


    def __str__(self):
        return self.d_title
    

class Employes(BaseModel):
    last_name = models.CharField(max_length=40,validators=[RegexValidator(r"^[A-Z][a-zA-Z]{2,24}$", "Familya faqat harflardan iborat bo‘lishi va bosh harfi katta bo‘lishi kerak!")])
    first_name = models.CharField(max_length=40,validators=[RegexValidator(r"^[A-Z][a-zA-Z]{2,24}$", "Ism faqat harflardan iborat bo‘lishi va bosh harfi katta bo‘lishi kerak!")])
    midle_name = models.CharField(max_length=40,validators=[RegexValidator(r"^[A-Z][a-zA-Z]{2,24}$","Ism faqat harflardan iborat bo‘lishi va bosh harfi katta bo‘lishi kerak!" )])
    email = models.EmailField(unique=True)
     

    phone_regix = RegexValidator(
        regex=r'^\+998\d{9}$',
        message= "Telefon raqami +998 bilan boshlanib, jami 13 ta belgidan iborat bo‘lishi kerak!"
    )


    phone = models.CharField(validators=[phone_regix],max_length=13,unique=True)



    def validate_file_extension(value):
        ext = os.path.splitext(value.name)[1]
        valid = ['.pdf','.doc','docx']
        if ext.lower() not in valid:
            raise ValidationError('"Faqat .pdf yoki .docx fayllarga ruxsat beriladi!"')

                                       


    data_fild = models.FileField(upload_to='uplods/',validators=[validate_file_extension])
   

    fk_departamen = models.ForeignKey(Departament,on_delete=models.CASCADE)
    fk_region = models.ForeignKey(Region,on_delete=models.CASCADE)


    def __str__(self):
        return self.last_name
    



