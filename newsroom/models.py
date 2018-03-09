from django.db import models
from django.utils import timezone
from django.urls import reverse


# class Post(models.Model):
#     author = models.ForeignKey('auth.User',on_delete=models.CASCADE)
#     title = models.CharField(max_length=200)
#     text = models.TextField()
#     created_date = models.DateTimeField(default=timezone.now)
#     published_date = models.DateTimeField(blank=True, null=True)
#
#     def publish(self):
#         self.published_date = timezone.now()
#         self.save()
#
#     def approve_comments(self):
#         return self.comments.filter(approved_comment=True)
#
#     def get_absolute_url(self):
#         return reverse("post_detail",kwargs={'pk':self.pk})
#
#
#     def __str__(self):
#         return self.title
#
#
#
# class Comment(models.Model):
#     post = models.ForeignKey('blog.Post', related_name='comments',on_delete=models.CASCADE)
#     author = models.CharField(max_length=200)
#     text = models.TextField()
#     created_date = models.DateTimeField(default=timezone.now)
#     approved_comment = models.BooleanField(default=False)
#
#     def approve(self):
#         self.approved_comment = True
#         self.save()
#
#     def get_absolute_url(self):
#         return reverse("post_list")
#
#     def __str__(self):
#         return self.text


class ParentInfograph(models.Model):
    p_id = models.AutoField('pid', primary_key=True, unique=True)
    name = models.CharField(max_length = 100, unique=True)
    description = models.CharField(max_length = 255, blank=False)
    date_created = models.DateTimeField(default=timezone.now)

    # def get_absolute_url(self):
    #     return reverse('home', kwargs={'pk':self.pk})

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "ParentInfograph"
        verbose_name_plural = "ParentInfographs"
        ordering = ['date_created', ]


class AppStatus(models.Model):
    status_id = models.PositiveIntegerField(primary_key=True , unique=True)
    description = models.CharField(max_length = 50)
    status_type = models.CharField(max_length = 50)

    class Meta:
        verbose_name = "AppStatus"
        verbose_name_plural = "AppStatus"

    def __str__(self):
        return self.description


class InfographCategory(models.Model):
    c_id = models.PositiveIntegerField(primary_key=True, unique=True)
    category = models.CharField(max_length = 30)

    class Meta:
        verbose_name = "InfographCategory"
        verbose_name_plural = "InfographCategories"

    def __str__(self):
        return self.category

class AppSource(models.Model):
    source_id = models.PositiveIntegerField(primary_key=True, unique=True, null=False)
    source = models.CharField(max_length = 100)
    source_type = models.CharField(max_length = 50)
    name = models.CharField(max_length = 100)

    class Meta:
        verbose_name = "AppSource"

    def __str__(self):
        return self.source

class Infograph(models.Model):
    i_id = models.PositiveIntegerField(primary_key=True, unique=True)
    p_id = models.PositiveIntegerField(unique=True)
    name = models.CharField(max_length = 100)
    description = models.CharField(max_length = 255)
    date_created = models.DateTimeField(default=timezone.now)
    c_id = models.PositiveIntegerField(unique=True)
    status_id = models.PositiveIntegerField(unique=True)
    source_id = models.PositiveIntegerField(unique=True)
    # p_id = models.ForeignKey(ParentInfograph, on_delete=models.CASCADE, related_name='p_id')
    # infograph_category = models.ForeignKey(InfographCategory, on_delete=models.CASCADE, related_name='infographs')
    # appstatus = models.ForeignKey(AppStatus, on_  delete=models.CASCADE)
    # appsource = models.ForeignKey(AppSource, on_delete=models.CASCADE)


    # def get_absolute_url(self):
    #     return reverse('home', kwargs={'pk':self.pk})

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Infograph"
        verbose_name_plural = "Infographs"
        ordering = ['date_created', ]


class MasterTopics(models.Model):
    mt_id = models.PositiveIntegerField(primary_key=True,unique=True)
    master_topic_code = models.CharField(max_length = 50, unique=True)
    master_topic = models.CharField(max_length = 100, unique=True)

    class Meta:
        verbose_name = "MasterTopic"
        verbose_name_plural = "MasterTopics"

    def __str__(self):
        return self.master_topic

class Topics(models.Model):
    t_id = models.PositiveIntegerField(primary_key=True, unique=True)
    mt_id = models.PositiveIntegerField(primary_key=False, unique=True)
    topic_code = models.CharField(max_length = 50, unique=True)
    topic_description = models.CharField(max_length = 50)
    master_topics = models.ForeignKey(MasterTopics, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Topic"
        verbose_name_plural = "Topics"

    def __str__(self):
        return self.topic_description


class CustomMetaTags(models.Model):
    mtg_id = models.PositiveIntegerField(primary_key=True, unique=True)
    metatag = models.CharField(max_length = 50)
    description = models.CharField(max_length = 100)


class Entity(models.Model):
    e_id = models.PositiveIntegerField(primary_key=True, unique=True)
    entity_code = models.CharField(max_length = 50)
    entity_type = models.CharField(max_length = 50)
    description = models.CharField(max_length = 100)

    class Meta:
        verbose_name_plural = "Entity"



class GeoPolitical(models.Model):
    e_id = models.PositiveIntegerField(primary_key=True, unique=True)
    gp_code = models.CharField(max_length = 50)
    description = models.CharField(max_length = 100)


    class Meta:
        verbose_name_plural = "GeoPolitical"


class InfographAssociation(models.Model):
    i_ad = models.PositiveIntegerField(primary_key=True)
    i_id = models.PositiveIntegerField()
    t_id = models.PositiveIntegerField()
    mtg_id = models.PositiveIntegerField()
    e_id = models.PositiveIntegerField()
    gp_id = models.PositiveIntegerField()
    date_created = models.DateTimeField(default=timezone.now)
    status_id = models.PositiveIntegerField()

class UserType(models.Model):
    usertype_id = models.PositiveIntegerField(primary_key=True)
    usertype = models.CharField(max_length = 50)


class Users(models.Model):
    u_id = models.PositiveIntegerField(primary_key=True)
    login = models.CharField(max_length = 100)
    pwd = models.CharField(max_length = 100)
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    gp_id = models.PositiveIntegerField()
    status_id = models.PositiveIntegerField()
    date_created = models.DateTimeField(default=timezone.now)
    user_type_id = models.ForeignKey(UserType, on_delete=models.CASCADE)
    # gpid = models.OneToOne(User, on_delete=models.CASCADE)
    # status_id = models.ForeignKey(Users, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"



    def __str__(self):
        return " ".join([self.first_name,
                         self.last_name]).strip()

    # def get_absolute_url(self):
    #     return reverse('author.detail', args=[self.pk, ])


class AuditType(models.Model):
    auid = models.PositiveIntegerField(primary_key=True)
    audit_type = models.CharField(max_length = 100)
    date_created = models.DateTimeField(default=timezone.now)


class UserTopic(models.Model):
    ut_id = models.PositiveIntegerField(primary_key=True)
    u_id = models.PositiveIntegerField()
    t_id = models.PositiveIntegerField()
    date_created = models.DateTimeField(default=timezone.now)
    status_id = models.PositiveIntegerField()
    # users = models.ForeignKey(Users, on_delete=models.CASCADE)
    # topics = models.ForeignKey(Topics, on_delete=models.CASCADE)
    # appstatus = models.ForeignKey(AppStatus, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class UserEntity(models.Model):
    ue_id = models.PositiveIntegerField(primary_key=True)
    u_id = models.PositiveIntegerField()
    e_id = models.PositiveIntegerField()
    date_created = models.DateTimeField(default=timezone.now)
    status_id = models.PositiveIntegerField()
    # users = models.ForeignKey(Users, on_delete=models.CASCADE)
    # entity = models.ForeignKey(Entity, on_delete=models.CASCADE)
    # appstatus = models.ForeignKey(AppStatus, on_delete=models.CASCADE)


class UserCustomMetaTags(models.Model):
    umtg_id = models.PositiveIntegerField(primary_key=True)
    u_id = models.PositiveIntegerField()
    mtg_id = models.PositiveIntegerField()
    date_created = models.DateTimeField(default=timezone.now)
    status_id = models.PositiveIntegerField()
    # users = models.ForeignKey(Users, on_delete=models.CASCADE)
    # customMetaTags = models.ForeignKey(CustomMetaTags, on_delete=models.CASCADE)
    # appstatus = models.ForeignKey(AppStatus, on_delete=models.CASCADE)


class UserGeoPolitical(models.Model):
    upg_id = models.PositiveIntegerField(primary_key=True)
    u_id = models.PositiveIntegerField()
    gp_id = models.PositiveIntegerField()
    date_created = models.DateTimeField(default=timezone.now)
    status_id = models.PositiveIntegerField()
    # users = models.ForeignKey(Users, on_delete=models.CASCADE)
    # geoPoliticals = models.ForeignKey(GeoPolitical, on_delete=models.CASCADE)
    # appstatus = models.ForeignKey(AppStatus, on_delete=models.CASCADE)


class AssociationType(models.Model):
    at_id = models.PositiveIntegerField(primary_key=True)
    association = models.CharField(max_length = 100)

class UserAssociations(models.Model):
    ua_id = models.PositiveIntegerField(primary_key=True)
    u_id1 = models.PositiveIntegerField()
    u_id2 = models.PositiveIntegerField()
    at_id = models.PositiveIntegerField()
    date_created = models.DateTimeField(default=timezone.now)
    status_id = models.PositiveIntegerField()
    # users = models.ForeignKey(Users, on_delete=models.CASCADE)
    # users = models.ForeignKey(Users, on_delete=models.CASCADE)
    # associationType = models.ForeignKey(AssociationType, on_delete=models.CASCADE)
    # appstatus = models.ForeignKey(AppStatus, on_delete=models.CASCADE)
    #

class UserAudit(models.Model):
    uau_id = models.PositiveIntegerField(primary_key=True)
    u_id = models.PositiveIntegerField()
    au_id = models.PositiveIntegerField()
    element_id = models.PositiveIntegerField()
    date_created = models.DateTimeField(default=timezone.now)
    # users = models.ForeignKey(Users, on_delete=models.CASCADE)
    # auditType = models.ForeignKey(AuditType, on_delete=models.CASCADE)

class AppSettings(models.Model):
    as_id = models.PositiveIntegerField(primary_key=True)
    appset = models.CharField(max_length = 50)
    appval = models.CharField(max_length = 255)

    class Meta:
        verbose_name = "AppSetting"
        verbose_name_plural = "AppSettings"
