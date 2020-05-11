from django.db import models


class LibraryBranch(models.Model):
    branch_name = models.CharField(max_length=50)
    address = models.CharField(max_length=150)
    telephone = models.CharField(max_length=30)
    description = models.TextField()
    open_date = models.DateTimeField()

    def __str__(self):
        return f'{self.branch_name}'

    class Meta:
        verbose_name_plural = 'Library Branches'


class Checkout(models.Model):
    library_asset = models.ForeignKey(
        'Book', related_name='checkouts', on_delete=models.PROTECT, null=True)
    library_card = models.ForeignKey(
        'LibraryCard', related_name='checkouts', on_delete=models.PROTECT, null=True)
    since = models.DateTimeField(auto_now_add=True, null=True)
    until = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Checkout {self.pk}'


class CheckoutHistory(models.Model):
    library_asset = models.ForeignKey('Book', on_delete=models.PROTECT)
    library_card = models.ForeignKey('LibraryCard', on_delete=models.PROTECT)
    checked_out = models.DateTimeField(auto_now_add=True)
    checked_in = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'Checkout History {self.pk}'

    class Meta:
        ordering = ['-checked_out']
        verbose_name_plural = 'Checkout History'


class Hold(models.Model):
    library_asset = models.ForeignKey('Book', on_delete=models.PROTECT)
    library_card = models.ForeignKey('LibraryCard', on_delete=models.PROTECT)
    hold_placed = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Hold {self.pk}'


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
    date_of_birth = models.DateField()
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


class Status(models.Model):
    STATUS_CHOICES = [
        ('AV', 'Available'),
        ('CO', 'Checked Out'),
        ('LO', 'Lost')
    ]
    name = models.CharField(max_length=2, choices=STATUS_CHOICES)
    description = models.TextField()

    def __str__(self):
        if self.name == 'AV':
            return 'Available'
        elif self.name == 'CO':
            return 'Checked Out'
        elif self.name == 'LO':
            return 'Lost'

    class Meta:
        verbose_name_plural = 'Status'


class LibraryAsset(models.Model):
    title = models.CharField(max_length=100)
    publish_date = models.DateField()
    status = models.ForeignKey(
        Status, related_name='assets', on_delete=models.CASCADE)
    cost = models.DecimalField(max_digits=5, decimal_places=2)
    number_of_copies = models.IntegerField()
    location = models.ForeignKey(
        LibraryBranch, related_name='assets', on_delete=models.CASCADE)

    class Meta:
        abstract = True

    @property
    def is_available_to_borrow(self):
        return self.number_of_copies > Checkout.objects.filter(library_asset=self.pk).count()

    @property
    def number_of_available_copies_to_borrow(self):
        return self.number_of_copies - Checkout.objects.filter(library_asset=self.pk).count()


class Author(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        ordering = ['first_name']


class Book(LibraryAsset):
    isbn = models.CharField(max_length=13)
    authors = models.ManyToManyField(Author)
    dewey_index = models.CharField(max_length=15)
    cover_image = models.ImageField(
        upload_to='covers/books', default='media/covers/nocover.jpg')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
