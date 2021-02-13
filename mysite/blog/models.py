from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User


# Creating customized model managers
class PublishedManager(models.Manager):
    def get_queryset(self):
        # The get_queryset() method of a manager returns the QuerySet that will be executed.
        return super().get_queryset().filter(status='published')


class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )  # tuple元组，STATUS_CHOICES[0][0] = 'draft'

    # This field is CharField, which translates into a VARCHAR column in the SQL database
    title = models.CharField(max_length=250)

    # This is a field intended to be used in URLs. A slug is a short label
    # that contains only letters, numbers, underscores, or hyphens. You will use
    # the slug field to build beautiful, SEO-friendly URLs for your blog posts.
    #
    # You have added the *unique_for_date parameter* to this field so that you
    # can build URLs for posts using their publish date and slug. Django will
    # prevent multiple posts from having the same slug for a given date.

    slug = models.SlugField(max_length=250, unique_for_date='publish')

    # This field defines a many-to-one relationship, meaning that each
    # post is written by a user, and a user can write any number of posts.
    # For this field, Django will create a foreign key in the database using
    # the primary key of the related model.
    # Using CASCADE, you specify that when the referenced user is deleted,
    # the database will also delete all related blog posts.
    # You specify the name of the reverse relationship, from User to Post,
    # with the *related_name* attribute. This will allow you to access related objects easily.

    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')

    # This is the body of the post. This field is a text field that translates
    # into a TEXT column in the SQL database.

    body = models.TextField()

    # You use Django's timezone now method as the default value.
    # This returns the current datetime in a timezone-aware format.

    publish = models.DateTimeField(default=timezone.now)

    # Since you are using auto_now_add here, the date will be saved automatically when creating an object.

    created = models.DateTimeField(auto_now_add=True)

    # Since you are using auto_now here, the date will be updated automatically when saving an object.

    updated = models.DateTimeField(auto_now=True)

    # You use a choices parameter, so the value of this field can only be set to one of the given choices.

    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICES,
                              default='draft')

    # The Meta class inside the model contains metadata. You tell Django to sort results
    # by the publish field in descending order by default when you query the database.
    # You specify the descending order using the negative prefix. By doing this, posts
    # published recently will appear first.
    objects = models.Manager()  # The default manager.
    published = PublishedManager()  # Our custom manager.

    class Meta:
        ordering = ('-publish',)

    # The __str__() method is the default human-readable representation of the object.
    # Django will use it in many places, such as the administration site.

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail',
                       args=[self.publish.year,
                             self.publish.month,
                             self.publish.day,
                             self.slug])
