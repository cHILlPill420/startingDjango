import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings')

import django
django.setup()

import random
from first_app.models import Topic, Webpage, AccessRecord
from faker import Faker

fakegen = Faker()
topicss = ['Games', 'Sports', 'News', 'Entertainment', 'Social']

def add_topic():
    t = Topic.objects.get_or_create(top_name = random.choice(topicss))[0]
    t.save()
    return t

def populate(N=5):
    for entry in range(N):
        #get topic
        top = add_topic()

        #create fake data for entry
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        #fake webpage entry
        webpg = Webpage.objects.get_or_create(topics = top, url = fake_url, name = fake_name)[0]

        #fake access record
        acc_rec = AccessRecord.objects.get_or_create(name = webpg, date = fake_date)[0]

if __name__ == '__main__':
    print("populating database")
    populate(20)
    print("populating complete")