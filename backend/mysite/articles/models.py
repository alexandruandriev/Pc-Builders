from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()

    def __str__(self):
        return self.title

class Ram(models.Model):
    memory_types = (
        ('2','DDR2'),
        ('3','DDR3'),
        ('4','DDR4'),
        )
    memory_sizes = (
        ('2','2GB'),
        ('4','4GB'),
        ('8','8GB'),
        ('16','16GB'),
        ('32','32GB'),
        ('64','64GB'),
        ('124','124GB'),

    )
    title = models.CharField(max_length=100)
    product_code = models.CharField(max_length=50)
    memory_type = models.CharField(max_length=1,choices=memory_types)
    size = models.CharField(max_length=3,choices=memory_sizes)
    frequency = models.CharField(max_length=10)
    voltage = models.CharField(max_length = 6)
    
    def __str__(self):
        return self.title
    
    

