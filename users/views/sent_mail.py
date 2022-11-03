from django.core.mail import send_mail
from django.conf import settings
import datetime
from cryptography.fernet import Fernet
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from rest_framework import mixins, viewsets, status
from rest_framework.response import Response
from users.models import User


class UserSentMail(mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    Function for sending mail for forget password
    """
    def sent_mail(self, request):
        """
        Function for sending the mail for forget password
        """
        try:
            receiver = request.data['email']
            query = User.objects.all().filter(email__iexact=receiver)
            key = Fernet.generate_key()
            fernet = Fernet(key)
            now_time = datetime.datetime.now()
            strnowtime = now_time.strftime('%m/%d/%y %H:%M')
            enc_message = fernet.encrypt(strnowtime.encode())
            if query:
                User.objects.all().filter(email__iexact=receiver).update(key=key)
                key = User.objects.filter(email__iexact=receiver).values('key')
                for q in query:
                    id = q.id
                    first_name = q.first_name
                subject = "Forget Password Link"
                message = f"http://devsita.netrum-tech.com/forget_password/{id}@{enc_message}"
                email_from = settings.EMAIL_HOST_USER
                email_receiver = [receiver]
                html_message = render_to_string("email_template.html", {'link': message, "name": first_name})
                text_content = strip_tags(html_message)

                send_mail(subject,
                          text_content,
                          email_from,
                          email_receiver,
                          html_message=html_message)
                data = {
                    "Status": "SUCCESS",
                    "Messages": message,
                    "Message": "Mail Successfully sent"
                }
                return Response(
                    {
                        "Data": data
                    }
                )
        except Exception as e:
            data = {
                "Status": status.HTTP_400_BAD_REQUEST,
                "Message": f"{e}"
            }
            return Response(
                {
                    "Data": data
                }
            )

    def decrypt_hashcode(self, request):
        """
        Function for decrypting hashcode of send mail
        """
        try:
            request_token = request.data['token']
            id = request_token.split("@")[0]
            token = request_token.split("@")[1]
            new = token.split("'")[1]
            byte_token = new.encode('utf-8')
            user = User.objects.all().filter(id=id)
            
            for q in user:
                user_key = q.key
                user.key = ""
                user.update()

            if user_key:
                key = user_key
                fernet = Fernet(key)
                dec_message = fernet.decrypt(token=byte_token).decode()
                newdatetime = datetime.datetime.strptime(dec_message, format('%m/%d/%y %H:%M'))
                current_time = datetime.datetime.now()
                backcurrenttime = current_time - datetime.timedelta(minutes=30)
                if newdatetime > backcurrenttime:
                    data = {
                        "Status": "SUCCESS",
                        "Message": "Success",
                    }
                else:
                    data = {
                        "Status": "FAILED",
                        "Message": "Session Timeout!!"
                    }
                return Response(
                    {
                        "Data": data
                    }
                )
        except Exception as e:
            data = {
                    "Status": "FAILED",
                    "Message": f"{e}"
                }
            return Response(
                {
                    "Data": data
                }
            )
