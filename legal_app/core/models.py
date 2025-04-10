from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    # Add any extra fields you need for your user model
    pass

class LegalExpert(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    expertise_areas = models.CharField(max_length=255)  # You might want to use a ManyToManyField with a separate Expertise model for a more robust solution
    contact_email = models.EmailField()
    contact_phone = models.CharField(max_length=20)
    bio = models.TextField(blank=True)
    availability = models.TextField(blank=True)  # You might want a more structured way to represent availability (e.g., using a library or a separate model)

    def __str__(self):
        return self.user.username

class Appointment(models.Model):
    legal_expert = models.ForeignKey(LegalExpert, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    appointment_time = models.DateTimeField()
    notes = models.TextField(blank=True)
    status = models.CharField(max_length=20, default='scheduled')  # e.g., scheduled, completed, cancelled

    def __str__(self):
        return f"Appointment with {self.legal_expert} at {self.appointment_time}"