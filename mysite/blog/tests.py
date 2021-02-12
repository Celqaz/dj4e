from django.test import TestCase

# Create your tests here.
STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

print(STATUS_CHOICES[0][0])