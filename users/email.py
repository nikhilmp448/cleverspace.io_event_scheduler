
from django.core.mail import send_mail
import random
from django.conf import settings



def sent_email_return_otp(email):
    otp = str(random.randint(1000,9999))
    subject = " your one time password for 'Cleverspace.io' machinetest email verification "
    message = f"OTP {otp}"
    from_email = settings.EMAIL_HOST_USER
    try:
        send_mail(subject=subject,message=message,from_email=from_email,recipient_list=[email])
    except Exception as e:
        # Handle the exception here, for example, you can log the error
        print(f"Error sending email: {str(e)}")
    return(otp)

