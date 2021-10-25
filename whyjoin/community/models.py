""" The models representing all the data in the community application. """
from django.db import models

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
