import factory
from factory import fuzzy
from django.contrib.auth.models import User
import datetime
from django.utils import timezone 
from django.test import TestCase

""" Factory para modelo User """
class UserFactory(factory.DjangoModelFactory):
       FACTORY_FOR = User
       username = factory.Sequence(lambda n: "user_%d" % n)
       is_active=True

class MailingListFactory(factory.DjangoModelFactory):
    FACTORY_FOR='super_archives.MailingList'
    FACTORY_DJANGO_GET_OR_CREATE=('name','email','description','logo',)
    name=fuzzy.FuzzyText()
    email=  factory.Sequence(lambda n: "mailist_%d@foo.com" % n)
    description=fuzzy.FuzzyText()
    logo=factory.django.FileField(filename='foo.png')


class MembershipFactory(factory.DjangoModelFactory):
    FACTORY_FOR='super_archives.MailingListMembership'
    FACTORY_DJANGO_GET_OR_CREATE=('user','mailinglist',)

    mailinglist=factory.SubFactory(MailingListFactory)
    user=factory.SubFactory(UserFactory)

class EmailAddressFactory( factory.DjangoModelFactory):
    FACTORY_FOR='super_archives.EmailAddress'
    FACTORY_DJANGO_GET_OR_CREATE=('user','address','realname')
    user=factory.SubFactory(User)
    address=fuzzy.FuzzyText()
    realname=fuzzy.FuzzyText()

class ThreadFactory(factory.DjangoModelFactory):
    FACTORY_FOR='super_archives.Thread'
    FACTORY_DJANGO_GET_OR_CREATE=('subject_token','mailinglist',)
    subject_token=fuzzy.FuzzyText()
    mailinglist=factory.SubFactory(MailingListFactory)

     
class MessageFactory(factory.DjangoModelFactory):
    FACTORY_FOR='super_archives.Message'
    FACTORY_DJANGO_GET_OR_CREATE=('from_address','thread','subject','subject_clean','body','received_time','message_id')
    from_address=factory.SubFactory(EmailAddressFactory)
    thread=factory.SubFactory(ThreadFactory)
    subject=fuzzy.FuzzyText()
    subject_clean=fuzzy.FuzzyText()
    body=fuzzy.FuzzyText()
    received_time=fuzzy.FuzzyNaiveDateTime(timezone.datetime(timezone.now().year-1,1,1 ))
    message_id=fuzzy.FuzzyText()

    
