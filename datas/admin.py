from django.contrib import admin
from .models import Deposit, CIF, Financing, Collateral
import pandas as pd
from django.shortcuts import render
from django.urls import path
from django.http import HttpResponseRedirect
from .forms import CSVUploadForm
from django import forms


class CsvImportForm(forms.Form):
    csv_upload = forms.FileField(label="Select a CSV file")


def get_urls(self):
    urls = super.get_urls()
    custom_urls = [
        path('upload-csv/', self.admin_site.admin_view(self.upload_csv), name="upload_csv"),
    ]
    return custom_urls + urls


class DepositAdmin(admin.ModelAdmin):
    list_display = ('field', 'description', 'table_name', 'datatype', 'remarks')
    search_fields = ('field', 'description', 'table_name')

    def upload_csv(self, request):
        if request.method == "POST":
            form = CSVUploadForm(request.POST, request.FILES)
            if form.is_valid():
                csv_file = form.cleaned_data['csv_file']
                data = pd.read_csv(csv_file)

                for index, row in data.iterrows():
                    Deposit.objects.create(
                        field=row['field'],
                        description=row['description'],
                        table_name=row['table_name'],
                        datatype=row['datatype'],
                        remarks=row['remarks']
                    )
                self.message_user(request, "CSV file imported successfully!")
                return HttpResponseRedirect(request.get_full_path())
        form = CSVUploadForm()
        return render(request, "admin/csv_upload_form.html", {"form":form})

# Combined this into Deposit Model
# class DepositProductAdmin(admin.ModelAdmin):
#     list_display = ('field', 'description', 'table_name', 'datatype', 'remarks')
#     search_fields = ('field', 'description', 'table_name')

#     def upload_csv(self, request):
#         if request.method == "POST":
#             form = CSVUploadForm(request.POST, request.FILES)
#             if form.is_valid():
#                 csv_file = form.cleaned_data['csv_file']
#                 data = pd.read_csv(csv_file)

#                 for index, row in data.iterrows():
#                     DepositProduct.objects.create(
#                         field=row['field'],
#                         description=row['description'],
#                         table_name=row['table_name'],
#                         datatype=row['datatype'],
#                         remarks=row['remarks']
#                     )
#                 self.message_user(request, "CSV file imported successfully!")
#                 return HttpResponseRedirect(request.get_full_path())
#         form = CSVUploadForm()
#         return render(request, "admin/csv_upload_form.html", {"form":form})

class CIFAdmin(admin.ModelAdmin):
    list_display = ('field', 'description', 'field_name', 'table_name', 'datatype', 'remarks')
    search_fields = ('field', 'description', 'field_name')

    def upload_csv(self, request):
        if request.method == "POST":
            form = CSVUploadForm(request.POST, request.FILES)
            if form.is_valid():
                csv_file = form.cleaned_data['csv_file']
                data = pd.read_csv(csv_file)

                for index, row in data.iterrows():
                    CIF.objects.create(
                        field=row['field'],
                        description=row['description'],
                        field_name=row['field_name'],
                        table_name=row['table_name'],
                        remarks=row['remarks']
                    )

                self.message_user(request, "CSV file imported successfully!")
                return HttpResponseRedirect(request.get_full_path())
        form = CSVUploadForm()
        return render(request, "admin/csv_upload_form.html", {"form":form})

class FinancingAdmin(admin.ModelAdmin):
    list_display = ('field', 'description', 'field_name', 'table_name', 'datatype', 'remarks')
    search_fields = ('field', 'description', 'field_name')

    def upload_csv(self, request):
        if request.method == "POST":
            form = CSVUploadForm(request.POST, request.FILES)
            if form.is_valid():
                csv_file = form.cleaned_data['csv_file']
                data = pd.read_csv(csv_file)

                for index, row in data.iterrows():
                    Financing.objects.create(
                        field=row['field'],
                        description=row['description'],
                        field_name=row['field_name'],
                        table_name=row['table_name'],
                        remarks=row['remarks']
                    )
                self.message_user(request, "CSV file imported successfully!")
                return HttpResponseRedirect(request.get_full_path())
        form = CSVUploadForm()
        return render(request, "admin/csv_upload_form.html", {"form":form})

class CollateralAdmin(admin.ModelAdmin):
    list_display = ('field', 'description', 'field_name', 'table_name', 'datatype', 'remarks')
    search_fields = ('field', 'description', 'field_name')

    def upload_csv(self, request):
        if request.method == "POST":
            form = CSVUploadForm(request.POST, request.FILES)
            if form.is_valid():
                csv_file = form.cleaned_data['csv_file']
                data = pd.read_csv(csv_file)

                for index, row in data.iterrows():
                    Collateral.objects.create(
                        field=row['field'],
                        description=row['description'],
                        field_name=row['field_name'],
                        table_name=row['table_name'],
                        remarks=row['remarks']
                    )
                self.message_user(request, "CSV file imported successfully!")
                return HttpResponseRedirect(request.get_full_path())
        form = CSVUploadForm()
        return render(request, "admin/csv_upload_form.html", {"form":form})

def get_urls(self):
    urls = super.get_urls()
    custom_urls = [
        path('upload-csv/', self.admin_site.admin_view(self.upload_csv), name="upload_csv"),
    ]
    return custom_urls + urls

# change_list_template = "admin/dep_change_list.html"

# Register your models here.

admin.site.register(Deposit, DepositAdmin)
# admin.site.register(DepositProduct, DepositProductAdmin)
admin.site.register(CIF, CIFAdmin)
admin.site.register(Financing, FinancingAdmin)
admin.site.register(Collateral, CollateralAdmin)
