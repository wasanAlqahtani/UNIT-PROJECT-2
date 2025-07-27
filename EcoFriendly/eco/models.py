from django.db import models

# Create your models here.

#action model 
class Action(models.Model):
    #location text choices 
    class LocationChoices(models.TextChoices):

        Location1 = "School", "School"
        Location2 = "Home", "Home"
        Location3 = "Work", "Work"
        Location4 = "Picnic", "Picnic"
        Location5 = "Others", "Others"
      
    title = models.CharField(max_length=1024)
    description = models.TextField()
    image = models.ImageField(upload_to="images/", default="images/default.jpg")
    location = models.CharField(max_length=1024, choices=LocationChoices.choices,
                                default=LocationChoices.Location5)
    created_at = models.DateField(auto_now_add=True)
#comment model for each action 
class Comment(models.Model):
    #rate integer choices (its help when calculate average )
    class RatingChoices(models.IntegerChoices):
        RATE1 = 1, "👍🏻 Try Harder"
        RATE2 = 2, "🎉 Keep Going " 
        RATE3 = 3, "🤩 Nice Job"
        RATE14 = 4, "🥇 Excellent"

    action = models.ForeignKey(Action, on_delete= models.CASCADE)
    content = models.TextField()
    rating = models.SmallIntegerField(choices=RatingChoices.choices)
    created_at = models.DateField(auto_now_add=True)


