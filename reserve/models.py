from django.db import models
from datetime import timedelta
from django.utils import timezone
from book.models import Book
from member.models import Member


class Reserve(models.Model):
    book_id = models.ForeignKey(
        Book, related_name='book', on_delete=models.CASCADE)
    member_id = models.ForeignKey(
        Member, related_name='member', on_delete=models.CASCADE)
    from_date = models.DateField(timezone.now)
    to_date = models.DateField()
    created = models.DateTimeField(default=timezone.now)

    def set_to_date(self):
        member = Member.objects.get(id=self.member_id)
        if member.membership_type == "special":
            self.to_date = self.from_date+timedelta(weeks=2)
        else:
            self.to_date = self.from_date+timedelta(weeks=1)
