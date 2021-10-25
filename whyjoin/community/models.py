""" The models representing all the data in the community application. """
from django.db import models
from django.contrib.auth.models import User

branch_choices = [("USMC", "United States Marine Corps"),
                  ("USA", "United States Army"),
                  ("USN", "United States Navy"),
                  ("USAF", "United States Air Force"),
                  ("NG", "National Guard"),
                  ("USCG", "United States Coast Guard"),
                  ("RSV", "Reserves"),
                  ("SF", "Space Force")]


class CommunityBranch(models.Model):
    """ 
    Model represents the branches of service to choose from, to categorize subjects 
    based on the branch. Each branch can then go on to create its own forum and 
    add members interested in each subject.
    """
    name_of_branch = models.CharField(max_length=4, choices=branch_choices)
    # brief description of what the branches mission is
    purpose = models.TextField()
    # number of users that are interested in hearing about the branch
    member_count = models.IntegerField()

    def __str__(self):
        return self.name_of_branch


class CommunityForums(models.Model):
    """
    Model represents discussions created by users. Referencing the branch model
    to categorize each for its respective branch.
    """
    # Reference the built in django user model
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
