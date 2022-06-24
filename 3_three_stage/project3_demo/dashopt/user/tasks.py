from dashopt.celery import app
from django.core.mail import send_mail

@app.task
def asyn_send_active_email(email_address, verify_url):

    subject = '达达t商城激活邮件'
    html_message = '''
    尊敬的用户您好，请点击激活链接进行激活,
    <a href="%s" target="_blank">点击此处</a>
    '''%(verify_url)

    send_mail(subject,'','572708691@qq.com',[email_address],html_message=html_message)

