from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name  

class SubCategory(models.Model):     
    name = models.CharField(max_length=200) 
    category = models.ForeignKey(Category, on_delete=models.CASCADE)  

    def __str__(self):
        return self.name

class States(models.Model):     
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name        

class CompanyDetails(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=550, null=True, blank=True)
    no_of_emp = models.CharField(max_length=200, null=True, blank=True)
    state = models.ForeignKey(States, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Jobs(models.Model):
    companydetails = models.ForeignKey(CompanyDetails, on_delete=models.CASCADE)
    jobPosition = models.CharField(max_length=200)
    Location = models.CharField(max_length=200)

    def __str__(self):
        return self.Location
