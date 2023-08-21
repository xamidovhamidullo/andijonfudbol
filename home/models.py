from django.db import models
from ckeditor.fields import RichTextField
# New


class NewCategory(models.Model):
    name = models.CharField(max_length=255)


class New(models.Model):
    img = models.ImageField()
    title = models.CharField(max_length=255)
    date = models.DateField(auto_now_add=True)


class NewTable(models.Model):
    img = models.ImageField()
    name = models.CharField(max_length=200)


class NewPlayer(models.Model):
    age = models.IntegerField()
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    img = models.ImageField(upload_to='pleyrs/')
    type = models.CharField(max_length=200)
    games = models.IntegerField()
    minut_eplayed = models.IntegerField()
    sub_off = models.IntegerField()
    started = models.IntegerField()


class NewTeam(models.Model):
    img = models.ImageField(upload_to="team/")
    url = models.URLField()


class Information(models.Model):
    img = models.ImageField(upload_to="logo/")
    title = models.CharField(max_length=255)
    instagram = models.URLField()
    telegram = models.URLField()
    facebook = models.URLField()
    youtube = models.URLField()
    twitter = models.URLField()
    phone = models.IntegerField()
    email = models.EmailField()


# Team
class TeamPlayer(models.Model):
    img = models.ImageField(upload_to="teamplayer/")
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    statuses = (
        (1, "Darvozabon"),
        (2, "Himoyachi"),
        (3, "Markaz"),
        (4, "Hujumchi"),
    )
    status = models.IntegerField(choices=statuses)


# competitions

class CompetitionCategory(models.Model):
    img = models.ImageField(upload_to='competitions/')
    name = models.CharField(max_length=200)
    game = models.IntegerField()
    victory = models.IntegerField()
    draw = models.IntegerField()
    goal_scord = models.IntegerField()
    swallow = models.IntegerField()
    scord_goal = models.IntegerField()
    total = models.IntegerField()

#

class Stroe(models.Model):
    name = models.CharField(max_length=200)
    img = models.ImageField(upload_to="stroe/")
    price = models.IntegerField()
    date = models.DateField(auto_now_add=True)


class Img(models.Model):
    img = models.ImageField(upload_to="img/")


class StroeArena(models.Model):
    name = models.CharField(max_length=200)
    text = models.TextField()
    kvm = models.IntegerField()
    place = models.IntegerField()
    sector = models.IntegerField()
    location = models.URLField()
    phone = models.IntegerField()
    img = models.ManyToManyField(Img)


# leadership

class Leadership(models.Model):
    name = models.CharField(max_length=200)
    text = models.TextField()
    img = models.ImageField(upload_to='leadership/')


# coaches


class Trainer(models.Model):
    name = models.CharField(max_length=200)
    text = models.TextField()
    img = models.ImageField(upload_to='leadership/')

# CKEditor


class Pride(models.Model):
    title = models.CharField(max_length=200)
    description = RichTextField()
    img = models.ImageField(upload_to="pride/")


class Ceremony(models.Model):
    description = RichTextField()
    img = models.ImageField(upload_to="ceremony/")


class Reference(models.Model):
    bg_img = models.ImageField(upload_to="reference/")
    description = RichTextField()
    date = models.DateTimeField(auto_now_add=True)


class Training(models.Model):
    description = RichTextField()


# shop

class Banner(models.Model):
    title = models.CharField(max_length=200)
    bg_img = models.ImageField(upload_to="shop_banner")


class BoburArena(models.Model):
    bg_img = models.ImageField(upload_to="arena/")
    name = models.CharField(max_length=200)


class ArenaImg(models.Model):
    img = models.ImageField(upload_to="img/")


class Bobur(models.Model):
    name = models.CharField(max_length=230)
    text = models.TextField()
    img = models.ForeignKey(ArenaImg, on_delete=models.CASCADE)
