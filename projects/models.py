from django.db import models
from django.utils.translation import gettext as _
from django.utils.text import slugify
# Create your models here.

class ProjectCategory(models.Model):
    category = models.CharField(verbose_name=_("Project Category"), max_length=160)
    slug = models.SlugField(_("slug"),editable=False)

    def __str__(self):
        return self.category
    
    def save(self):
        self.slug = slugify(self.category)
        super(ProjectCategory,self).save()


class Project(models.Model):
    project = models.CharField(verbose_name=_("Project Name"), max_length=160)
    cover  = models.ImageField(verbose_name=_("Project Image"), upload_to="project/",blank=False,null=False,default="cover.png")
    slug = models.SlugField(_("slug"),editable=False,unique=True)
    description = models.TextField()
    views=models.IntegerField(default=0)
    published_date = models.DateField(_("Published Date"), auto_now=False, auto_now_add=True)
    category = models.ManyToManyField(ProjectCategory)

    """Model definition for Project."""

    # TODO: Define fields here

    class Meta:
        """Meta definition for Project."""

        verbose_name = 'Project'
        verbose_name_plural = 'Projects'

    def __str__(self):
        """Unicode representation of Project."""
        pass

    def save(self):
        self.slug = slugify(self.project)
        super(Project,self).save()

    def get_absolute_url(self):
        """Return absolute url for Project."""
        return ('')

    # TODO: Define custom methods here
