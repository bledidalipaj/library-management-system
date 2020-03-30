from django.db import models


class LibraryBranch(models.Model):
    branch_name = models.CharField(max_length=50)
    address = models.CharField(max_length=150)
    telephone = models.CharField(max_length=30)
    description = models.TextField()
    open_date = models.DateTimeField()

    def __str__(self):
        return f'Library Branch: {self.branch_name}'


class Checkout(models.Model):
    pass


class Patron(models.Model):
    MALE = 'M'
    FEMALE = 'F'

    GENDER_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female')
    ]
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.CharField(max_length=150)
    date_of_birth = models.DateField(auto_now_add=True)
    telephone = models.CharField(max_length=30)
    gender = models.CharField(
        max_length=1, choices=GENDER_CHOICES, default=MALE)
    # libary_card = models.OneToOneField(LibraryCard, on_delete=models.CASCADE)
    home_library_branch = models.ForeignKey(
        LibraryBranch, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class LibraryCard(models.Model):
    fees = models.FloatField(default=0.00)
    created = models.DateTimeField(auto_now_add=True)
    patron = models.OneToOneField(Patron, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'Library card {self.id}'
