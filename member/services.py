from member.repositories import MemberRepository


class MemberService:
    def __init__(self) -> None:
        self.member_repository = MemberRepository()

    def create(self, first_name, last_name, membership_type, validity_date):
        if not first_name:
            raise ValueError('First name is required.')
        if len(first_name) > 50:
            raise ValueError(
                "First name Should be at most 50 characters long.")
        if not last_name:
            raise ValueError('Last name is required.')
        if last_name and len(last_name) > 50:
            raise ValueError("Last name Should be at most 20 characters long.")

        member = self.member_repository.create(
            first_name, last_name, membership_type, validity_date)
        return member

    def update(self, id, first_name, last_name, membership_type, validity_date):
        if len(first_name) > 50:
            raise ValueError(
                "First name Should be at most 50 characters long.")
        if last_name and len(last_name) > 50:
            raise ValueError("Last name Should be at most 20 characters long.")
        member=self.member_repository.update(first_name, last_name, membership_type, validity_date)
        return member
