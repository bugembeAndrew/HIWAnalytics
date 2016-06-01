# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Agent(models.Model):
    agent = models.CharField(unique=True, max_length=50)
    email = models.CharField(unique=True, max_length=100)
    username = models.CharField(unique=True, max_length=70)
    password = models.CharField(max_length=70)
    authkey = models.CharField(db_column='authKey', max_length=100, blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return ' %s ' % (self.agent)

    class Meta:
        managed = False
        db_table = 'agent'


class Art(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    gender = models.CharField(max_length=6, blank=True, null=True)
    age = models.DateField(blank=True, null=True)
    district = models.ForeignKey('District', models.DO_NOTHING, db_column='district', blank=True, null=True)
    area = models.CharField(max_length=30, blank=True, null=True)
    designation = models.CharField(max_length=100, blank=True, null=True)
    sector = models.ForeignKey('BeneficiaryCategory', models.DO_NOTHING, db_column='sector', blank=True, null=True)
    telephone_number = models.BigIntegerField(unique=True)
    created_at = models.DateTimeField()
    created_by = models.ForeignKey(Agent, models.DO_NOTHING, db_column='created_by')

    def __str__(self):
        return ' %s ' % (self.name)

    def get_absolute_url(self):
        return reverse('art-detail', kwargs={'pk': self.pk})

    class Meta:
        managed = True
        db_table = 'art'


class ArtCall(models.Model):
    art = models.ForeignKey(Art, models.DO_NOTHING, db_column='art')
    date_called = models.DateTimeField()
    date_last_vist_hf = models.DateTimeField(blank=True, null=True)
    hf_last_visit = models.ForeignKey('HealthFacility', models.DO_NOTHING, db_column='hf_last_visit', blank=True, null=True)
    date_next_visit_hf = models.DateTimeField(blank=True, null=True)
    # hf_next_visit = models.ForeignKey('HealthFacility', models.DO_NOTHING, db_column='hf_next_visit', blank=True, null=True)
    hf_next_visit = models.IntegerField(blank=True, null=True)
    hf_challenges = models.CharField(max_length=255, blank=True, null=True)
    has_arv = models.CharField(max_length=3, blank=True, null=True)
    sms_optin = models.CharField(max_length=3, blank=True, null=True)
    spouse_tested = models.CharField(max_length=7, blank=True, null=True)
    baby_tested = models.CharField(max_length=7, blank=True, null=True)
    challenges_other = models.CharField(max_length=255, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    created_by = models.ForeignKey(Agent, models.DO_NOTHING, db_column='created_by')

    def __str__(self):
        return ' %s %s %s %s %s ' % (self.art.name, self.art.gender, self.art.age, self.art.district, self.art.telephone_number)

    class Meta:
        managed = False
        db_table = 'art_call'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class BeneficiaryCategory(models.Model):
    beneficiary_category = models.CharField(unique=True, max_length=50)
    short_name = models.CharField(max_length=30)

    def __str__(self):
        return ' %s ' % (self.beneficiary_category)

    class Meta:
        managed = False
        db_table = 'beneficiary_category'


class Calls(models.Model):
    patient_names = models.CharField(max_length=200, blank=True, null=True)
    age_no = models.IntegerField(blank=True, null=True)
    age_unit = models.CharField(max_length=6, blank=True, null=True)
    sex = models.CharField(max_length=6, blank=True, null=True)
    reason_for_call = models.CharField(max_length=100, blank=True, null=True)
    det_reason_for_call = models.TextField(blank=True, null=True)
    emergency = models.CharField(max_length=3, blank=True, null=True)
    caller_names = models.CharField(max_length=200, blank=True, null=True)
    relationship = models.CharField(max_length=200, blank=True, null=True)
    alt_number = models.IntegerField(blank=True, null=True)
    aboutus = models.CharField(max_length=200, blank=True, null=True)
    sms = models.CharField(max_length=3, blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    email = models.CharField(max_length=200, blank=True, null=True)
    location = models.CharField(max_length=200, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    caller_number = models.IntegerField(blank=True, null=True)
    agent = models.IntegerField(blank=True, null=True)
    queue = models.CharField(max_length=10, blank=True, null=True)
    language = models.CharField(max_length=7, blank=True, null=True)
    calldate = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'calls'


class Cdr(models.Model):
    acctid = models.BigIntegerField(primary_key=True)
    calldate = models.DateTimeField()
    clid = models.CharField(max_length=80)
    src = models.CharField(max_length=80)
    dst = models.CharField(max_length=80)
    dcontext = models.CharField(max_length=80)
    channel = models.CharField(max_length=80)
    dstchannel = models.CharField(max_length=80)
    lastapp = models.CharField(max_length=80)
    lastdata = models.CharField(max_length=80)
    duration = models.IntegerField()
    billsec = models.IntegerField()
    disposition = models.CharField(max_length=45)
    amaflags = models.IntegerField()
    accountcode = models.CharField(max_length=20)
    userfield = models.CharField(max_length=255)
    uniqueid = models.CharField(max_length=32)
    linkedid = models.CharField(max_length=32)
    sequence = models.CharField(max_length=32)
    peeraccount = models.CharField(max_length=32)
    import_cdr = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cdr'


class District(models.Model):
    district = models.CharField(unique=True, max_length=50)

    def __str__(self):
        return ' %s ' % (self.district)

    class Meta:
        managed = True
        db_table = 'district'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class HealthFacility(models.Model):
    region = models.ForeignKey('HfRegion', models.DO_NOTHING, db_column='region')
    district = models.ForeignKey(District, models.DO_NOTHING, db_column='district')
    hsd = models.CharField(max_length=100, blank=True, null=True)
    county = models.CharField(max_length=100, blank=True, null=True)
    subcounty = models.CharField(max_length=100, blank=True, null=True)
    parish = models.CharField(max_length=100, blank=True, null=True)
    health_facility = models.CharField(max_length=100, blank=True, null=True)
    level = models.ForeignKey('HfLevel', models.DO_NOTHING, db_column='level', blank=True, null=True)
    ownership = models.ForeignKey('HfOwnership', models.DO_NOTHING, db_column='ownership', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'health_facility'


class HfLevel(models.Model):
    level = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hf_level'


class HfOwnership(models.Model):
    ownership = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hf_ownership'


class HfRegion(models.Model):
    region = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hf_region'


class IncomingCall(models.Model):
    gender = models.CharField(max_length=6, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    district = models.ForeignKey(District, models.DO_NOTHING, db_column='district', blank=True, null=True)
    beneficiary_category = models.ForeignKey(BeneficiaryCategory, models.DO_NOTHING, db_column='beneficiary_category', blank=True, null=True)
    beneficiary_subcategory = models.CharField(max_length=50, blank=True, null=True)
    reason_for_call = models.TextField(blank=True, null=True)
    service_category = models.ForeignKey('ServiceCategory', models.DO_NOTHING, db_column='service_category', blank=True, null=True)
    advise_offered = models.TextField(blank=True, null=True)
    referal_details = models.CharField(max_length=100, blank=True, null=True)
    agent = models.ForeignKey(Agent, models.DO_NOTHING, db_column='agent', blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    phone = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return ' %s ' % (self.reason_for_call)

    class Meta:
        managed = False
        db_table = 'incoming_call'


class OutgoingCall(models.Model):
    names = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=6, blank=True, null=True)
    district = models.ForeignKey(District, models.DO_NOTHING, db_column='district', blank=True, null=True)
    next_visit = models.DateField(blank=True, null=True)
    health_facility = models.CharField(max_length=100, blank=True, null=True)
    comments = models.TextField(blank=True, null=True)
    phone = models.IntegerField(blank=True, null=True)
    agent = models.ForeignKey(Agent, models.DO_NOTHING, db_column='agent')
    date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'outgoing_call'


class ScIc(models.Model):
    incoming_call = models.ForeignKey(IncomingCall, models.DO_NOTHING, db_column='incoming_call', blank=True, null=True)
    service_category = models.ForeignKey('ServiceCategory', models.DO_NOTHING, db_column='service_category', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sc_ic'
        unique_together = (('incoming_call', 'service_category'),)


class ServiceCategory(models.Model):
    service_category = models.CharField(unique=True, max_length=50)

    def __str__(self):
        return ' %s ' % (self.service_category)

    class Meta:
        managed = False
        db_table = 'service_category'


class Shift(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    shift_start = models.TimeField(blank=True, null=True)
    shift_end = models.TimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shift'


class Shiftreport(models.Model):
    date = models.DateTimeField()
    shift = models.ForeignKey(Shift, models.DO_NOTHING, db_column='shift')
    agent = models.ForeignKey(Agent, models.DO_NOTHING, db_column='agent')
    voicecalls = models.IntegerField(blank=True, null=True)
    callduration = models.IntegerField(blank=True, null=True)
    wa_new = models.IntegerField(blank=True, null=True)
    wa_old = models.IntegerField(blank=True, null=True)
    tweets = models.IntegerField(blank=True, null=True)
    fb_posts = models.IntegerField(blank=True, null=True)
    fb_messenger = models.IntegerField(blank=True, null=True)
    fb_reach = models.IntegerField(blank=True, null=True)
    email = models.IntegerField(blank=True, null=True)
    video = models.IntegerField(blank=True, null=True)
    ureport = models.IntegerField(blank=True, null=True)
    physical_exam = models.IntegerField(blank=True, null=True)
    summary = models.TextField(blank=True, null=True)
    callduration_outgoing = models.IntegerField()
    voicecalls_outgoing = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'shiftreport'
