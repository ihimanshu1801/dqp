from django.db import models
from django.utils import timezone
from django.urls import reverse

class ParentInfograph(models.Model):
    p_id = models.AutoField(primary_key=True, unique = True)
    name = models.CharField(max_length = 100, blank=False, unique=True)
    description = models.CharField(max_length = 255)
    date_created = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "ParentInfograph"
        verbose_name_plural = "ParentInfographs"
        ordering = ['date_created', ]
#

class AppStatus(models.Model):
    status_id = models.AutoField(primary_key=True, unique = True)
    description = models.CharField(max_length = 50)
    status_type = models.CharField(max_length = 50)

    class Meta:
        verbose_name = "AppStatus"
        verbose_name_plural = "AppStatus"

    def __str__(self):
        return self.description
#
#
class InfographCategory(models.Model):
    c_id = models.AutoField(primary_key=True, unique = True)
    category = models.CharField(max_length = 30)

    class Meta:
        verbose_name = "InfographCategory"
        verbose_name_plural = "InfographCategories"

    def __str__(self):
        return self.category
#
class AppSource(models.Model):
    source_id = models.AutoField(primary_key=True, unique = True)
    source = models.URLField(max_length = 100)
    source_type = models.CharField(max_length = 50)
    domain_url = models.URLField(max_length = 100,  default='www.test.com')

    class Meta:
        verbose_name = "AppSource"

    def __str__(self):
        return self.source
#
class Infograph(models.Model):
    i_id = models.AutoField(primary_key=True, unique = True)
    p_id = models.PositiveIntegerField()
    name = models.CharField(max_length = 100)
    description = models.CharField(max_length = 255)
    date_created = models.DateTimeField(default=timezone.now)
    c_id = models.PositiveIntegerField()
    status_id = models.PositiveIntegerField()
    source_id = models.PositiveIntegerField()
    internal_url = models.ImageField(upload_to='infograph.jpg')
    external_url = models.URLField(max_length = 100,default='www.test1.com')
    parentinfograph = models.ForeignKey(ParentInfograph, on_delete=models.CASCADE,null = True)
    infographcategory = models.ForeignKey(InfographCategory, on_delete=models.CASCADE, null = True)
    appstatus = models.ForeignKey(AppStatus, on_delete=models.CASCADE,null = True)
    appsource = models.ForeignKey(AppSource, on_delete=models.CASCADE, null = True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Infograph"
        verbose_name_plural = "Infographs"
        ordering = ['date_created', ]
#
#
class MasterTopics(models.Model):
    mt_id = models.AutoField(primary_key=True, unique = True)
    master_topic_code = models.CharField(max_length = 50)
    master_topic = models.CharField(max_length = 100)

    class Meta:
        verbose_name = "MasterTopic"
        verbose_name_plural = "MasterTopics"

    def __str__(self):
        return self.master_topic

class Topics(models.Model):
    t_id = models.AutoField(primary_key=True, unique = True)
    mt_id = models.PositiveIntegerField()
    topic_code = models.CharField(max_length = 50)
    topic_description = models.CharField(max_length = 50)
    mastertopics = models.ForeignKey(MasterTopics, on_delete=models.CASCADE,  null = True)

    class Meta:
        verbose_name = "Topic"
        verbose_name_plural = "Topics"

    def __str__(self):
        return self.topic_description
# #
class CustomMetaTags(models.Model):
    mtg_id =  models.AutoField(primary_key=True, unique = True)
    metatag = models.CharField(max_length = 50)
    description = models.CharField(max_length = 100)

    class Meta:
        verbose_name = "CustomMetaTags"
        verbose_name_plural = "CustomMetaTags"

    def __str__(self):
        return self.description


class Entity(models.Model):
    e_id =  models.AutoField(primary_key=True, unique = True)
    entity_code = models.CharField(max_length = 50)
    entity_type = models.CharField(max_length = 50)
    description = models.CharField(max_length = 100)

    class Meta:
        verbose_name = "Entity"
        verbose_name_plural = "Entities"

    def __str__(self):
        return self.description



class GeoPolitical(models.Model):
    e_id =  models.AutoField(primary_key=True, unique = True)
    gp_code = models.CharField(max_length = 50)
    description = models.CharField(max_length = 100)

    class Meta:
        verbose_name = "GeoPolitical"
        verbose_name_plural = "GeoPolitical"

    def __str__(self):
        return self.description

class InfographAssociation(models.Model):
    i_ad = models.AutoField(primary_key=True, unique = True)
    i_id = models.PositiveIntegerField()
    t_id = models.PositiveIntegerField()
    mtg_id = models.PositiveIntegerField()
    e_id = models.PositiveIntegerField()
    gp_id = models.PositiveIntegerField()
    date_created = models.DateTimeField(default=timezone.now)
    status_id = models.PositiveIntegerField()
    infograph = models.ForeignKey(Infograph, on_delete=models.CASCADE,null = True)
    topics = models.ForeignKey(Topics, on_delete=models.CASCADE, null = True)
    custommetatags = models.ForeignKey(CustomMetaTags, on_delete=models.CASCADE,null = True)
    entity = models.ForeignKey(Entity, on_delete=models.CASCADE, null = True)
    geopolitical = models.ForeignKey(GeoPolitical, on_delete=models.CASCADE, null = True)
    appstatus = models.ForeignKey(AppStatus, on_delete=models.CASCADE, null = True)

    class Meta:
        verbose_name = "InfographAssociation"
        verbose_name_plural = "InfographAssociations"
        ordering = ['date_created', ]

    def __str__(self):
        return self.description

# #
class UserType(models.Model):
    usertype_id = models.AutoField(primary_key=True, unique = True)
    usertype = models.CharField(max_length = 50)

    class Meta:
        verbose_name = "UserType"
        verbose_name_plural = "UserType"

    def __str__(self):
        return self.usertype

class Users(models.Model):
    u_id = models.AutoField(primary_key=True, unique = True)
    login = models.CharField(max_length = 100)
    pwd = models.CharField(max_length = 100)
    usertype_id =models.PositiveIntegerField()
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    gp_id = models.PositiveIntegerField()
    status_id = models.PositiveIntegerField()
    date_created = models.DateTimeField(default=timezone.now)
    # usertype = models.ForeignKey(UserType, on_delete=models.CASCADE,null = True)
    geopolitical = models.ForeignKey(GeoPolitical, on_delete=models.CASCADE,null = True)
    appstatus = models.ForeignKey(AppStatus, on_delete=models.CASCADE, null = True)

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return " ".join([self.first_name,
                         self.last_name]).strip()

#
class AuditType(models.Model):
    au_id = models.AutoField(primary_key=True, unique = True)
    audit_type = models.CharField(max_length = 100)
    date_created = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = "AuditType"
        verbose_name_plural = "AuditType"
        ordering = ['date_created', ]

class UserTopic(models.Model):
    ut_id = models.AutoField(primary_key=True, unique = True)
    u_id = models.PositiveIntegerField()
    t_id = models.PositiveIntegerField()
    date_created = models.DateTimeField(default=timezone.now)
    status_id = models.PositiveIntegerField()
    users = models.ForeignKey(Users, on_delete=models.CASCADE, null = True)
    topics = models.ForeignKey(Topics, on_delete=models.CASCADE, null = True)
    appstatus = models.ForeignKey(AppStatus, on_delete=models.CASCADE, null = True)

    class Meta:
        verbose_name = "UserTopic"
        verbose_name_plural = "UserTopics"
        ordering = ['topics', ]

    def __str__(self):
        return self.topics

class UserEntity(models.Model):
    ue_id = models.AutoField(primary_key=True, unique = True)
    u_id = models.PositiveIntegerField()
    e_id = models.PositiveIntegerField()
    date_created = models.DateTimeField(default=timezone.now)
    status_id = models.PositiveIntegerField()
    users = models.ForeignKey(Users, on_delete=models.CASCADE, null = True)
    entity = models.ForeignKey(Entity, on_delete=models.CASCADE,null = True)
    appstatus = models.ForeignKey(AppStatus, on_delete=models.CASCADE, null = True)

    class Meta:
        verbose_name = "UserEntity"
        verbose_name_plural = "UserEntities"
        ordering = ['date_created', ]


class UserCustomMetaTags(models.Model):
    umtg_id = models.AutoField(primary_key=True, unique = True)
    u_id = models.PositiveIntegerField()
    mtg_id = models.PositiveIntegerField()
    date_created = models.DateTimeField(default=timezone.now)
    status_id = models.PositiveIntegerField()
    users = models.ForeignKey(Users, on_delete=models.CASCADE, null = True)
    custommetatags = models.ForeignKey(CustomMetaTags, on_delete=models.CASCADE, null = True)
    appstatus = models.ForeignKey(AppStatus, on_delete=models.CASCADE, null = True)

    class Meta:
        verbose_name = "UserCustomMetaTags"
        verbose_name_plural = "UserCustomMetaTags"
        ordering = ['date_created', ]

    def __str__(self):
        return self.users


class UserGeoPolitical(models.Model):
    upg_id = models.AutoField(primary_key=True, unique = True)
    u_id = models.PositiveIntegerField()
    gp_id = models.PositiveIntegerField()
    date_created = models.DateTimeField(default=timezone.now)
    status_id = models.PositiveIntegerField()
    users = models.ForeignKey(Users, on_delete=models.CASCADE,null = True)
    geopolitical = models.ForeignKey(GeoPolitical, on_delete=models.CASCADE, null = True)
    appstatus = models.ForeignKey(AppStatus, on_delete=models.CASCADE, null = True)

    class Meta:
        verbose_name = "UserGeoPolitical"
        verbose_name_plural = "UserGeoPolitical"
        ordering = ['date_created', ]

    def __str__(self):
        return self.users


class AssociationType(models.Model):
    at_id = models.AutoField(primary_key=True, unique = True)
    association = models.CharField(max_length = 100)

    class Meta:
        verbose_name = "AssociationType"
        verbose_name_plural = "AssociationTypes"


class UserAssociations(models.Model):
    ua_id = models.AutoField(primary_key=True, unique = True)
    u_id1 = models.PositiveIntegerField()
    u_id2 = models.PositiveIntegerField()
    at_id = models.PositiveIntegerField()
    date_created = models.DateTimeField(default=timezone.now)
    status_id = models.PositiveIntegerField()
    users = models.ForeignKey(Users, on_delete=models.CASCADE, null = True)
    associationType = models.ForeignKey(AssociationType, on_delete=models.CASCADE, null = True)
    appstatus = models.ForeignKey(AppStatus, on_delete=models.CASCADE, null = True)

    class Meta:
        verbose_name = "UserAssociations"
        verbose_name_plural = "UserAssociations"
        ordering = ['date_created', ]

class UserAudit(models.Model):
    uau_id = models.AutoField(primary_key=True, unique = True)
    u_id = models.PositiveIntegerField()
    au_id = models.PositiveIntegerField()
    element_id = models.PositiveIntegerField()
    date_created = models.DateTimeField(default=timezone.now)
    users = models.ForeignKey(Users, on_delete=models.CASCADE, null = True)
    audittype = models.ForeignKey(AuditType, on_delete=models.CASCADE, null = True)

    class Meta:
        verbose_name = "UserAudit"
        verbose_name_plural = "UserAudit"
        ordering = ['date_created', ]


class AppSettings(models.Model):
    as_id = models.AutoField(primary_key=True, unique = True)
    app_set = models.CharField(max_length = 50)
    app_val = models.CharField(max_length = 255)

    class Meta:
        verbose_name = "AppSetting"
        verbose_name_plural = "AppSettings"
