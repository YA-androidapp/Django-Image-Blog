from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
<<<<<<< HEAD
from django.utils.html import format_html
from django.conf import settings
import base64
import os


class Category(models.Model):

    # Fields
    id = models.BigAutoField(primary_key=True)

    name = models.CharField(max_length=100)
    slug = models.SlugField()

    created_at = models.DateTimeField(auto_now_add=True)
=======


class Tag(models.Model):

    # Fields
    id = models.BigAutoField(primary_key=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField()
    name = models.CharField(max_length=100)
>>>>>>> 609159725a8427956399f25bc6c3d39cc33898e1

    class Meta:
        pass

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
<<<<<<< HEAD
        return reverse('myapp_Category_detail', args=(self.slug,))

    def get_update_url(self):
        return reverse('myapp_Category_update', args=(self.slug,))


class File(models.Model):

    # Relationships
    post = models.ForeignKey('myapp.Post', on_delete=models.CASCADE, related_name='post_files', blank=True, null=True)

    # Fields
    id = models.BigAutoField(primary_key=True)

    binary = models.BinaryField(blank=True, null=True)
    file = models.FileField(upload_to='upload/files/', blank=True, null=True)
    title = models.CharField(max_length=100, blank=True, null=True)

    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
=======
        return reverse("myapp_Tag_detail", args=(self.slug,))

    def get_update_url(self):
        return reverse("myapp_Tag_update", args=(self.slug,))


class Post(models.Model):

    # Relationships
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='author_posts')
    category = models.ForeignKey("myapp.Category", on_delete=models.CASCADE, related_name='category_posts')
    tags = models.ManyToManyField("myapp.Tag")

    # Fields
    id = models.BigAutoField(primary_key=True)
    published_at = models.DateTimeField()
    description = models.TextField()
    is_public = models.BooleanField()
    title = models.CharField(max_length=100)
    updated_at = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
>>>>>>> 609159725a8427956399f25bc6c3d39cc33898e1

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
<<<<<<< HEAD
        return reverse('myapp_File_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('myapp_File_update', args=(self.pk,))


class Image(models.Model):

    # Relationships
    post = models.ForeignKey('myapp.Post', on_delete=models.CASCADE, related_name='post_images', blank=True, null=True)

    # Fields
    id = models.BigAutoField(primary_key=True)

    binary = models.BinaryField(blank=True, null=True)
    image = models.ImageField(
        upload_to='upload/images/', blank=True, null=True)
    title = models.CharField(max_length=100, blank=True, null=True)

    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
=======
        return reverse("myapp_Post_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("myapp_Post_update", args=(self.pk,))


class File(models.Model):

    # Relationships
    post = models.ForeignKey("myapp.Post", on_delete=models.CASCADE)

    # Fields
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=100)
    file = models.FileField(upload_to="upload/files/")
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    binary = models.BinaryField()
>>>>>>> 609159725a8427956399f25bc6c3d39cc33898e1

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
<<<<<<< HEAD
        return reverse('myapp_Image_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('myapp_Image_update', args=(self.pk,))

    def save(self, *args, **kwargs):
        if self.image:
            print('path', 'upload/images/')
            print('path', self.image.url)
            print('path', os.path.join('upload/images/', self.image.url))
            data = open(os.path.join(settings.MEDIA_ROOT, 'upload/images/', os.path.basename(self.image.url)), 'rb').read()
            self.binary = data
            super(Image, self).save(*args, **kwargs)


class Post(models.Model):

    # Relationships
    author = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, related_name='author_posts', blank=True, null=True)
    category = models.ForeignKey(
        'myapp.Category', on_delete=models.CASCADE, related_name='category_posts', blank=True, null=True)
    tags = models.ManyToManyField('myapp.Tag', related_name='tag_posts', blank=True, null=True)

    # Fields
    id = models.BigAutoField(primary_key=True)

    content = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    is_public = models.BooleanField(default=False)
    published_at = models.DateTimeField(blank=True, null=True)
    title = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
=======
        return reverse("myapp_File_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("myapp_File_update", args=(self.pk,))


class Image(models.Model):

    # Relationships
    post = models.ForeignKey("myapp.Post", on_delete=models.CASCADE)

    # Fields
    id = models.BigAutoField(primary_key=True)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    binary = models.BinaryField()
    created = models.DateTimeField(auto_now_add=True, editable=False)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="upload/images/")
>>>>>>> 609159725a8427956399f25bc6c3d39cc33898e1

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
<<<<<<< HEAD
        return reverse('myapp_Post_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('myapp_Post_update', args=(self.pk,))


class Tag(models.Model):

    # Fields
    id = models.BigAutoField(primary_key=True)

    name = models.CharField(max_length=100)
    slug = models.SlugField()

    created_at = models.DateTimeField(auto_now_add=True)

=======
        return reverse("myapp_Image_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("myapp_Image_update", args=(self.pk,))


class Category(models.Model):

    # Fields
    id = models.BigAutoField(primary_key=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100)
    slug = models.SlugField()

>>>>>>> 609159725a8427956399f25bc6c3d39cc33898e1
    class Meta:
        pass

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
<<<<<<< HEAD
        return reverse('myapp_Tag_detail', args=(self.slug,))

    def get_update_url(self):
        return reverse('myapp_Tag_update', args=(self.slug,))
=======
        return reverse("myapp_Category_detail", args=(self.slug,))

    def get_update_url(self):
        return reverse("myapp_Category_update", args=(self.slug,))
>>>>>>> 609159725a8427956399f25bc6c3d39cc33898e1
