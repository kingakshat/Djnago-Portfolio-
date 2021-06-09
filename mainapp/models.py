from django.db import models


# Create your models here.
class view(models.Model):

    def __str__(self):
        return self.view_name
    view_name = models.CharField(max_length=200)
    view_intro = models.CharField(max_length=1000)


class look(models.Model):

    def __str__(self):
        return self.look_fdis
    look_fdis = models.CharField(max_length=500)
    look_pdis = models.CharField(max_length=500)
    look_mintro = models.CharField(max_length=500, default='main_intro_ine')
    look_wgol = models.CharField(max_length=500, default='main_intro_ine')


class studing(models.Model):

    def __str__(self):
        return self.studing_a
    studing_a = models.CharField(max_length=500)


class exp(models.Model):

    def __str__(self):
        return self.exp_a
    exp_a = models.CharField(max_length=500)


class course(models.Model):

    def __str__(self):
        return self.course_a
    course_a = models.CharField(max_length=500)


class achivment(models.Model):

    def __str__(self):
        return self.achivment_a
    achivment_a = models.CharField(max_length=500)


class one(models.Model):

    def __str__(self):
        return self.one_name
    one_name = models.CharField(max_length=500)
    one_disone = models.CharField(max_length=500)
    one_distwo = models.CharField(max_length=500)
    one_date = models.CharField(max_length=500)
    one_del = models.CharField(max_length=500)


class onet(models.Model):

    def __str__(self):
        return self.one_team
    one_team = models.CharField(max_length=500)


class two(models.Model):

    def __str__(self):
        return self.two_name
    two_name = models.CharField(max_length=500)
    two_disone = models.CharField(max_length=500)
    two_distwo = models.CharField(max_length=500)
    two_date = models.CharField(max_length=500)
    two_del = models.CharField(max_length=500)


class twot(models.Model):

    def __str__(self):
        return self.two_team
    two_team = models.CharField(max_length=500)


class three(models.Model):

    def __str__(self):
        return  self.three_name
    three_name = models.CharField(max_length=500)
    three_disone = models.CharField(max_length=500)
    three_distwo = models.CharField(max_length=500)
    three_date = models.CharField(max_length=500)
    three_del = models.CharField(max_length=500)


class threet(models.Model):

    def __str__(self):
        return self.three_team
    three_team = models.CharField(max_length=500)


class Feedback(models.Model):
    Name = models.CharField(max_length=200)
    Mail = models.CharField(max_length=200)
    Your_Message = models.CharField(max_length=2000)

    def __str__(self):
        return self.Name + '// ' + self.Mail

