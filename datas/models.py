from django.db import models

# Create your models here.

class Deposit(models.Model):
    field = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    table_name = models.CharField(max_length=50)
    datatype = models.CharField(max_length=50)
    remarks = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return f"Field: {self.field}, Description: {self.description}, Table: {self.table_name}, Datatype: {self.datatype}, Remarks: {self.remarks or 'N/A'}"
    

class DepositProduct(models.Model):
    field = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    table_name = models.CharField(max_length=50)
    datatype = models.CharField(max_length=50)
    remarks = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return f"Field: {self.field}, Description: {self.description}, Table: {self.table_name}, Datatype: {self.datatype}, Remarks: {self.remarks or 'N/A'}"

class Financing(models.Model):
    field = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    field_name = models.CharField(max_length=100)
    table_name = models.CharField(max_length=50)
    datatype = models.CharField(max_length=50)
    remarks = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return f"Field: {self.field}, Description: {self.description}, Field Name: {self.field_name} ,Table: {self.table_name}, Datatype: {self.datatype}, Remarks: {self.remarks or 'N/A'}"

class Collateral(models.Model):
    field = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    field_name = models.CharField(max_length=100)
    table_name = models.CharField(max_length=50)
    datatype = models.CharField(max_length=50)
    remarks = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return f"Field: {self.field}, Description: {self.description}, Field Name: {self.field_name} ,Table: {self.table_name}, Datatype: {self.datatype}, Remarks: {self.remarks or 'N/A'}"

class CIF(models.Model):
    field = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    field_name = models.CharField(max_length=100)
    table_name = models.CharField(max_length=50)
    datatype = models.CharField(max_length=50)
    remarks = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return f"Field: {self.field}, Description: {self.description}, Field Name: {self.field_name} ,Table: {self.table_name}, Datatype: {self.datatype}, Remarks: {self.remarks or 'N/A'}"
