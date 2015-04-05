import datetime
from hashlib import sha1

from django.db import models

# Create your models here.

AGE_RANGE_CHOICES = (
    ('under13', 'Under 13'),
    ('13to20', '13 through 20'),
    ('over21', '21 and over'),
)

class Event(models.Model):
    title = models.CharField(max_length=256)
    short_title = models.CharField(max_length=50)
    thumbnail = models.FileField(null=True, blank=True)
    full_pic = models.FileField(null=True, blank=True)
    from_time = models.DateTimeField()
    to_time = models.DateTimeField()
    description = models.TextField()
    price = models.IntegerField()
    location = models.CharField(max_length=100, blank=True, null=True)
    is_closed = models.BooleanField(default=False)
    is_published = models.BooleanField(default=True)

    class Meta:
        ordering = ['-from_time']
    
    def __unicode__(self):
        return self.short_title
    
    def short_time(self):
        from_hour = self.from_time.hour
        if from_hour > 12:
            from_ampm = 'p'
            from_hour -= 12
        else:
            from_ampm = 'a'
        from_minute = self.from_time.minute
        if from_minute > 0:
            from_minute = ":%s" % (from_minute,)
        else:
            from_minute = ''
        
        to_hour = self.to_time.hour
        if to_hour > 12:
            to_ampm = 'p'
            to_hour -= 12
        else:
            to_ampm = 'a'
        to_minute = self.to_time.minute
        if to_minute > 0:
            to_minute = ":%s" % (to_minute,)
        else:
            to_minute = ''
        
        if from_ampm == to_ampm:
            from_ampm = ''
        
        return "%s%s%s-%s%s%s" % (from_hour, from_minute, from_ampm,
                                  to_hour, to_minute, to_ampm)

class Registrant(models.Model):
    event = models.ForeignKey('Event')
    confirmation_code = models.CharField(max_length=40, blank=True)
    first_name = models.CharField(max_length=35)
    last_name = models.CharField(max_length=35)
    email_address = models.EmailField(max_length=254)
    phone_number = models.CharField(max_length=20)
    age_range = models.CharField(max_length=7, choices=AGE_RANGE_CHOICES, default=AGE_RANGE_CHOICES[0][0])
    notify_future = models.BooleanField(default=False)
    comments = models.TextField(null=True, blank=True)
    referral = models.CharField(max_length=256, null=True, blank=True)
    register_date = models.DateTimeField(auto_now_add=True)
    
    def __unicode__(self):
        day = self.register_date.day
        month = self.register_date.month
        return "%s, %s (%s/%s) - %s" % (self.last_name, self.first_name, month, day, self.event.short_title)
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.confirmation_code = sha1(self.last_name + datetime.datetime.utcnow().isoformat()).hexdigest()
        super(Registrant, self).save(*args, **kwargs)
