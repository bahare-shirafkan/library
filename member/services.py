from member.repositories import MemberRepository
from member.models import OTP
import random
from django.contrib.auth import authenticate, login
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
        
    def getOtp(self,mobile):
        user =self.member_repository.getByMobile(mobile)
        if user is not None:
            otp = random.randint(1000, 9999)
            OTP.objects.update_or_create(user=user, defaults={'otp': otp})
            # Send OTP to the user's console instead of SMS
            print("Your OTP:", otp)
            

    def otp_validation(otp):
            try:
                otp_obj = OTP.objects.get(otp=otp)
                user=authenticate(token=otp)
                otp_obj.delete()
                return user
            except OTP.DoesNotExist:
                raise ValueError("Invalid OTP. Please try again.")
        
