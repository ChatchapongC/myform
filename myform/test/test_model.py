from django.test import TestCase
from django.contrib.auth.models import User
import datetime
from myform.models import Event, Question

class EventTest(TestCase):

    def test_event(self):
        event =  Event(event_name="Exam", date_of_event=datetime.date(1999,3,25))
        
        self.assertEqual('Exam', event.event_name)
        self.assertEqual(3, event.date_of_event.month)
        self.assertEqual(1999, event.date_of_event.years)

   

    

