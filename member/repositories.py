from member.models import Member


class MemberRepository:
    def create(self, first_name, last_name, membership_type, validity_date):
        member = Member(first_name=first_name, last_name=last_name,
                        membership_type=membership_type, validity_date=validity_date)
        member.save()
        return member

    def update(id, first_name, last_name, membership_type, validity_date):
        member = Member.objects.get(id=id)
        member.first_name = first_name
        member.last_name = last_name
        member.membership_type = membership_type
        member.validity_date = validity_date
        member.save()
        return member
