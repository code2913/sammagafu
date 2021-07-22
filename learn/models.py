from django.db import models
from django.utils.translation import gettext as _
from django.utils import timezone
from django.utils.text import slugify

# Create your models here.
class CourseCategory(models.Model):
    category = models.CharField(verbose_name=_("Course Name"), max_length=160)
    slug = models.SlugField(_("slug"),editable=False)

    class Meta:
        """Meta definition for Course."""

        verbose_name = 'Course Category'
        verbose_name_plural = 'Courses Categories'


    def __str__(self):
        return self.category
    
    def save(self):
        if not self.pk:
            self.slug = slugify(self.category)
        super(CourseCategory,self).save()

    

class Course(models.Model):
    course = models.CharField(verbose_name=_("Course Name"), max_length=160)
    cover  = models.ImageField(verbose_name=_("Cover Image"), upload_to="cover/",blank=False,null=False,default="cover.png")
    slug = models.SlugField(_("slug"),editable=False,unique=True)
    description = models.TextField()
    views=models.IntegerField(default=0)
    published_date = models.DateField(_("Published Date"), auto_now=False, auto_now_add=True)
    category = models.ManyToManyField(CourseCategory)



    class Meta:
        """Meta definition for Course."""

        verbose_name = 'Course'
        verbose_name_plural = 'Courses'

    def __str__(self):
        return self.course

    def save(self):
        if not self.pk:
            self.slug = slugify(self.course)
        super(Course,self).save()

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('learn:course-detail', args=[str(self.slug)])


class  Topic(models.Model):
    course = models.ForeignKey(Course, verbose_name=_("course"), on_delete=models.CASCADE,null=True,related_name="topic")
    slug = models.SlugField(_("slug"),editable=False,null=True)
    topic  = models.CharField(_("Topic Name"), max_length=160)
    published_date = models.DateField(_("Published Date"),default=timezone.now())
    video  = models.CharField(_("Url for video"), max_length=400, blank=True)
    description = models.TextField()

    class Meta:

        verbose_name = 'Topic'
        verbose_name_plural = 'Topics'

    def __str__(self):
        return self.topic
    
    def save(self):
        self.slug = slugify(self.topic)
        super(Topic,self).save()

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('learn:topic-detail', args=[str(self.slug)])


