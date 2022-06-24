from django.core.mail import send_mail
from dashopt.celery import app


@app.task
def asyn_send_active_email(email_address, verify_url):
    subject = "激活邮件"
    html_message = f"""
                尊敬的用户您好，请点击激活链接，
        <a href={verify_url} target='_blank'>点击此处</a>
        """
    send_mail(subject, '', "909600795@qq.com", [email_address], html_message=html_message)
