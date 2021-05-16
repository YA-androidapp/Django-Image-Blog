from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model


class Tag(models.Model):

    # Fields
    id = models.BigAutoField(primary_key=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField()
    name = models.CharField(max_length=100)

    class Meta:
        pass

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
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

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
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

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
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

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("myapp_Image_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("myapp_Image_update", args=(self.pk,))


class Category(models.Model):

    # Fields
    id = models.BigAutoField(primary_key=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100)
    slug = models.SlugField()

    class Meta:
        pass

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse("myapp_Category_detail", args=(self.slug,))

    def get_update_url(self):
        return reverse("myapp_Category_update", args=(self.slug,))
