from django.db import models

# Create your models here.
class Tutorial(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    slug = models.CharField(max_length=200, editable=False)
    published = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        """ Creates a URL safe slug automatically when a new a Tutorial is created. """
        if not self.pk:
            self.slug = slugify(self.title, allow_unicode=True)

        # Call save on the superclass.
        return super(Tutorial, self).save(*args, **kwargs)

class Module(models.Model):
    title = models.CharField(max_length=200)
    slug = models.CharField(max_length=200, editable=False)
    placement = models.IntegerField()
    tutorial = models.ForeignKey(Tutorial, on_delete=models.CASCADE) # link to tutorial pk
    # list of submodules
    
    def save(self, *args, **kwargs):
        """ Creates a URL safe slug automatically when a new a Module is created. """
        if not self.pk:
            self.slug = slugify(self.title, allow_unicode=True)

        # Call save on the superclass.
        return super(Module, self).save(*args, **kwargs)

class SubModule(models.Model):
    title = models.CharField(max_length=200)
    slug = models.CharField(max_length=200, editable=False)
    # mark_complete = models.BooleanField() # based on student account
    placement = models.IntegerField()
    module = models.ForeignKey(Module, on_delete=models.CASCADE) # link to module pk
    # list of sections

    def save(self, *args, **kwargs):
        """ Creates a URL safe slug automatically when a new a SubModule is created. """
        if not self.pk:
            self.slug = slugify(self.title, allow_unicode=True)

        # Call save on the superclass.
        return super(SubModule, self).save(*args, **kwargs)

# probably not necessary, just need to find a way to save multiple form fields in a submodule (must add 'content' field)
class Section(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    submodule = models.ForeignKey(SubModule, on_delete=models.CASCADE) # link to submodule pk
    # list of images 

class CodeSnippet(models.Model):
    title = models.CharField(max_length=200)
    language = models.CharField(max_length=200)
    content = models.TextField()

class EmphasizeContent(models.Model):
    pass