import traceback
from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin
from django.conf import settings
from django.core.mail import send_mail

class ExceptonMw(MiddlewareMixin):
    def process_exception(self, request, exception):

        print('from middleware:',exception)
        print(traceback.format_exc())

        res = send_mail(
            "mySite 报错了!",
            traceback.format_exc(),
            settings.EMAIL_HOST_USER,
            ['klvong@icloud.com']
        )
        print(res)
        return HttpResponse("网页有点忙")
