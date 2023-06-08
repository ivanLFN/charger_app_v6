from django.db import models


class Image(models.Model):

    type_img = models.CharField(max_length=50)
    src = models.CharField(max_length=100)
    desc = models.TextField()

    def __str__(self) -> str:
        return self.type_img + '_' + self.src
    

class Product(models.Model):

    images = models.ManyToManyField(Image)
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    installation = models.CharField(max_length=100)
    sockets_count = models.IntegerField()
    socket_type = models.CharField(max_length=100)
    power = models.CharField(max_length=100)
    remote_control = models.CharField(max_length=100)
    dev = models.BooleanField(default=False, blank=True)

    def __str__(self) -> str:
        return self.title
    

class SegmetOfWork(models.Model):

    title = models.CharField(max_length=100)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    about = models.TextField()

    def __str__(self) -> str:
        return self.title



class Partnership(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=256)
    image = models.ForeignKey(Image, on_delete=models.CASCADE, related_name='partnership_images')
    header_img = models.ForeignKey(Image, on_delete=models.CASCADE, related_name='partnership_header_images')
    header_text_main = models.CharField(max_length=256)
    header_text = models.CharField(max_length=256)
    header_body = models.CharField(max_length=256, blank=True)
    segmets_of_work = models.ManyToManyField(SegmetOfWork, blank=True)

    def __str__(self) -> str:
        return self.title

    