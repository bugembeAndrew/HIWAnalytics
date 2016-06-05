# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
from __future__ import unicode_literals

from django.db import models

class Agent(models.Model):
    id = models.IntegerField(primary_key=True)
    agent = models.CharField(unique=True, max_length=50)
    email = models.CharField(unique=True, max_length=100)
    username = models.CharField(unique=True, max_length=70)
    password = models.CharField(max_length=70)
    authkey = models.CharField(db_column='authKey', max_length=100, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'agent'

class Art(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100, blank=True)
    gender = models.CharField(max_length=6, blank=True)
    age = models.DateField(blank=True, null=True)
    district = models.ForeignKey('District', db_column='district', blank=True, null=True)
    area = models.CharField(max_length=30, blank=True)
    designation = models.CharField(max_length=100, blank=True)
    sector = models.ForeignKey('BeneficiaryCategory', db_column='sector', blank=True, null=True)
    telephone_number = models.BigIntegerField(unique=True)
    created_at = models.DateTimeField()
    created_by = models.ForeignKey(Agent, db_column='created_by')
    class Meta:
        managed = False
        db_table = 'art'

class ArtCall(models.Model):
    id = models.IntegerField(primary_key=True)
    art = models.ForeignKey(Art, db_column='art')
    date_called = models.DateTimeField()
    date_last_vist_hf = models.DateTimeField(blank=True, null=True)
    hf_last_visit = models.ForeignKey('HealthFacility', db_column='hf_last_visit', blank=True, null=True)
    date_next_visit_hf = models.DateTimeField(blank=True, null=True)
   # hf_next_visit = models.ForeignKey('HealthFacility', db_column='hf_next_visit', blank=True, null=True)
    hf_next_visit = models.IntegerField(blank=True, null=True)
    hf_challenges = models.CharField(max_length=255, blank=True)
    has_arv = models.CharField(max_length=3, blank=True)
    sms_optin = models.CharField(max_length=3, blank=True)
    spouse_tested = models.CharField(max_length=7, blank=True)
    baby_tested = models.CharField(max_length=7, blank=True)
    challenges_other = models.CharField(max_length=255, blank=True)
    status = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    created_by = models.ForeignKey(Agent, db_column='created_by')
    class Meta:
        managed = False
        db_table = 'art_call'

class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=80)
    class Meta:
        managed = False
        db_table = 'auth_group'

class AuthGroupPermissions(models.Model):
    id = models.IntegerField(primary_key=True)
    group = models.ForeignKey(AuthGroup)
    permission = models.ForeignKey('AuthPermission')
    class Meta:
        managed = False
        db_table = 'auth_group_permissions'

class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    content_type = models.ForeignKey('DjangoContentType')
    codename = models.CharField(max_length=100)
    class Meta:
        managed = False
        db_table = 'auth_permission'

class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField()
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=75)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'auth_user'

class AuthUserGroups(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(AuthUser)
    group = models.ForeignKey(AuthGroup)
    class Meta:
        managed = False
        db_table = 'auth_user_groups'

class AuthUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(AuthUser)
    permission = models.ForeignKey(AuthPermission)
    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'

class BeneficiaryCategory(models.Model):
    id = models.IntegerField(primary_key=True)
    beneficiary_category = models.CharField(unique=True, max_length=50)
    short_name = models.CharField(max_length=30)
    class Meta:
        managed = False
        db_table = 'beneficiary_category'

class Calls(models.Model):
    id = models.IntegerField(primary_key=True)
    patient_names = models.CharField(max_length=200, blank=True)
    age_no = models.IntegerField(blank=True, null=True)
    age_unit = models.CharField(max_length=6, blank=True)
    sex = models.CharField(max_length=6, blank=True)
    reason_for_call = models.CharField(max_length=100, blank=True)
    det_reason_for_call = models.TextField(blank=True)
    emergency = models.CharField(max_length=3, blank=True)
    caller_names = models.CharField(max_length=200, blank=True)
    relationship = models.CharField(max_length=200, blank=True)
    alt_number = models.IntegerField(blank=True, null=True)
    aboutus = models.CharField(max_length=200, blank=True)
    sms = models.CharField(max_length=3, blank=True)
    dob = models.DateField(blank=True, null=True)
    email = models.CharField(max_length=200, blank=True)
    location = models.CharField(max_length=200, blank=True)
    notes = models.TextField(blank=True)
    caller_number = models.IntegerField(blank=True, null=True)
    agent = models.IntegerField(blank=True, null=True)
    queue = models.CharField(max_length=10, blank=True)
    language = models.CharField(max_length=7, blank=True)
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
    id = models.IntegerField(primary_key=True)
    district = models.CharField(unique=True, max_length=50)
    class Meta:
        managed = False
        db_table = 'district'

class DjangoAdminLog(models.Model):
    id = models.IntegerField(primary_key=True)
    action_time = models.DateTimeField()
    user = models.ForeignKey(AuthUser)
    content_type = models.ForeignKey('DjangoContentType', blank=True, null=True)
    object_id = models.TextField(blank=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.IntegerField()
    change_message = models.TextField()
    class Meta:
        managed = False
        db_table = 'django_admin_log'

class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    class Meta:
        managed = False
        db_table = 'django_content_type'

class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'django_session'

class HealthFacility(models.Model):
    id = models.IntegerField(primary_key=True)
    region = models.ForeignKey('HfRegion', db_column='region')
    district = models.ForeignKey(District, db_column='district')
    hsd = models.CharField(max_length=100, blank=True)
    county = models.CharField(max_length=100, blank=True)
    subcounty = models.CharField(max_length=100, blank=True)
    parish = models.CharField(max_length=100, blank=True)
    health_facility = models.CharField(max_length=100, blank=True)
    level = models.ForeignKey('HfLevel', db_column='level', blank=True, null=True)
    ownership = models.ForeignKey('HfOwnership', db_column='ownership', blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'health_facility'

class HfLevel(models.Model):
    id = models.IntegerField(primary_key=True)
    level = models.CharField(max_length=100, blank=True)
    class Meta:
        managed = False
        db_table = 'hf_level'

class HfOwnership(models.Model):
    id = models.IntegerField(primary_key=True)
    ownership = models.CharField(max_length=100, blank=True)
    class Meta:
        managed = False
        db_table = 'hf_ownership'

class HfRegion(models.Model):
    id = models.IntegerField(primary_key=True)
    region = models.CharField(max_length=100, blank=True)
    class Meta:
        managed = False
        db_table = 'hf_region'

class IncomingCall(models.Model):
    id = models.IntegerField(primary_key=True)
    gender = models.CharField(max_length=6, blank=True)
    age = models.IntegerField(blank=True, null=True)
    district = models.ForeignKey(District, db_column='district', blank=True, null=True)
    beneficiary_category = models.ForeignKey(BeneficiaryCategory, db_column='beneficiary_category', blank=True, null=True)
    beneficiary_subcategory = models.CharField(max_length=50, blank=True)
    reason_for_call = models.TextField(blank=True)
    service_category = models.ForeignKey('ServiceCategory', db_column='service_category', blank=True, null=True)
    advise_offered = models.TextField(blank=True)
    referal_details = models.CharField(max_length=100, blank=True)
    agent = models.ForeignKey(Agent, db_column='agent', blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    phone = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'incoming_call'

class OutgoingCall(models.Model):
    id = models.IntegerField(primary_key=True)
    names = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=6, blank=True)
    district = models.ForeignKey(District, db_column='district', blank=True, null=True)
    next_visit = models.DateField(blank=True, null=True)
    health_facility = models.CharField(max_length=100, blank=True)
    comments = models.TextField(blank=True)
    phone = models.IntegerField(blank=True, null=True)
    agent = models.ForeignKey(Agent, db_column='agent')
    date = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'outgoing_call'

class ScIc(models.Model):
    id = models.IntegerField(primary_key=True)
    incoming_call = models.ForeignKey(IncomingCall, db_column='incoming_call', blank=True, null=True)
    service_category = models.ForeignKey('ServiceCategory', db_column='service_category', blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'sc_ic'

class ServiceCategory(models.Model):
    id = models.IntegerField(primary_key=True)
    service_category = models.CharField(unique=True, max_length=50)
    class Meta:
        managed = False
        db_table = 'service_category'

class Shift(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100, blank=True)
    shift_start = models.TimeField(blank=True, null=True)
    shift_end = models.TimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'shift'

class Shiftreport(models.Model):
    id = models.IntegerField(primary_key=True)
    date = models.DateTimeField()
    shift = models.ForeignKey(Shift, db_column='shift')
    agent = models.ForeignKey(Agent, db_column='agent')
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
    summary = models.TextField(blank=True)
    callduration_outgoing = models.IntegerField()
    voicecalls_outgoing = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'shiftreport'

