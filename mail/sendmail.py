#!/usr/bin/env python
# -*- coding: utf-8 -*-
import smtplib
import os
import sys
#from optparse import OptionParser
#import optparse
import argparse
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.MIMEBase import MIMEBase
#from email.mime.image import MIMEImage # 发送图片用这个

#mailto_list =['keqiang.ye@vipshop.com','timon.ma@vipshop.com']
#mailto_list = ""
smtpserver = ''
mail_username = ''
mail_pass = ''
mail_postfix = 'test.com'

#def send_mail(receivers,sub,content,attachs): #receivers：收件人；subject：主题；content：邮件内容 attachs: 附件列表
def send_mail(receivers,sub,content): #receivers：收件人；subject：主题；content：邮件内容
    me="<"+mail_username+"@"+mail_postfix+">"
    msg = MIMEMultipart('related')
    part = MIMEText(content,_subtype='plain',_charset='utf-8')
    msg['Subject'] = sub    #设置主题
    msg['From'] = me 
    msg['To'] = ";".join(mailto_list)
    msg.attach(part)
    #构建附件并且发送
    #attach_name = os.path.basename(attach)
    #print "attachment filename %s" % attach_name
    #att = MIMEText(open(attachment, 'rb').read(), 'base64', 'utf-8')
    #att["Content-Type"] = 'application/octet-stream'
    #att["Content-Disposition"] = 'attachment; filename="%s" ' 
    #msg.attach(att)

    # 发送附件
    #for attach in attachs:
    #    att = MIMEBase('application', "octet-stream")
    #    #att.set_payload( open(attach,"rb").read() )
    #    #Encoders.encode_base64(att)
    #    att = MIMEText(open(attach, 'rb').read(), 'base64', 'utf-8')
    #    att.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(attach))
    #    msg.attach(att)

    try:  
        s = smtplib.SMTP()  
        s.connect(smtpserver)  #连接smtp服务器
        s.login(mail_username,mail_pass)  #登陆服务器
        s.sendmail(me, mailto_list, msg.as_string())  #发送邮件
        s.close()  
        return True  
    except Exception, e:  
        print str(e)  
        return False  


if __name__ == '__main__':  
    #usage = "usage: %prog [ -s <subject>] [-c <content>] [-r <mailto_list>]"
    parser = argparse.ArgumentParser()
    #parser.add_argument("-?",action="help", help=argparse.SUPPRESS_HELP)
    parser.add_argument("-s", "--subject",dest="subject", default='TEST',help="Please input the mail's subject")
    #parser.add_option("-c", "--content",dest="html", default='Hello World',help="Please input the mail's body")

    parser.add_argument("-r", "--receivers",dest="mailto_list",action="store",nargs='+',help="input this mailto_list", metavar="keqiang.ye@vipshop.com")
    parser.add_argument('--version', action='version', version='%(prog)s 1.0')

    #group = optparse.OptionGroup(parser, "\nReport arguments bugs to keqiang.ye@vipshop.com!")
    #parser.add_option_group(group)
    #(options, args) = parser.parse_args()
    options = parser.parse_args()
    #attachments = ['/apps/sh/java_env.sh','/apps/sh/phprun.sh'] 
    subject = options.subject
    html = sys.stdin.read()
    #string_content = StringIO.StringIO(content) 
    #html = string_content.readline()
    mailto_list = options.mailto_list
    #for mail in mailto_list:
    #    print mail
    #print "mailto_list is: %s" % mailto_list
    #if send_mail(mailto_list,subject,html,attachments):  
    if send_mail(mailto_list,subject,html):  
        print "邮件发送成功"
    else:
        print "邮件发送失败"