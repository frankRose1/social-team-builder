from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    """A user can create a profile with their details, skills, and avatar"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255)
    skills = last_name = models.CharField(max_length=255) # change this to represent multiple skills
    avatar = models.ImageField(
        blank=True,
        null=True,
        upload_to='avatars'
    )

    def __str__(self):
        return self.full_name


class Project(models.Model):
    """A user can create a project that they need help on, and other users can
    apply to open positions on a project."""
    title = models.CharField(max_length=255)
    project_owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_add_now=True)
    published = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class ProjectPosition(models.Model):
    """A project position wil belong to a project and will have a name,
      description and a related skill."""
    name = models.CharField(max_length=255)
    description = models.TextField()
    skill = models.CharField(max_length=255)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    filled = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class ProjectPositionApplicant(models.Model):
    """Will model the relationship between a User and their relationship to a 
    ProjectPosition"""
    position = models.ForeignKey(ProjectPosition, on_delete=models.CASCADE)
    applicant = models.ForeignKey(User, on_delete=models.CASCADE)