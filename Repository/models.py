from django.db import models

class Questions(models.Model):
    title = models.CharField(max_length=200)
    
    LANGUAGE_CHOICES = (
        ("python", "python"),
        ("java", "java"),
        ("javascript", "javascript"),
        ("c", "c")
    )
    language = models.CharField(max_length=100, choices=LANGUAGE_CHOICES, default="python")
    
    DIFFICULTY_LEVEL = (
        ("easy", "easy"),
        ("medium", "medium"),
        ("hard", "hard")
    )
    difficulty_level = models.CharField(max_length=100, choices=DIFFICULTY_LEVEL, default="easy")
    
    notes = models.TextField(null=True)
    topic = models.CharField(max_length=200)
    published_date = models.DateField(auto_now_add=True)
    
   
    
    is_active = models.BooleanField(default=True)