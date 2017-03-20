#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3
import cgi
import os
import re
import smtplib


class Shop:
    template_path = "templates/"
    email_template = "email.html"
    shop_temaplte = "shop.html"

    error_template = """<span style='color: darkred; padding: 5px; border: solid 1px darkred;\
 background: rgba(139,0,0,0.41);'>ERROR - {error}</span>"""
    content_type_template = "Content-Type: text/html\n\n"
    template_construct = """{content_type}{error_messages}{main_content}"""

    def __init__(self, product, email):
        self.template = ""
        self.product = product
        self.email = email
        self.error_messages = []

        if self.product is None and self.email is not None:
            self.error_messages.append("You have to choose at least one product!")
            self.__get_template(self.shop_temaplte)
        elif self.product is not None and self.email is None:
            self.error_messages.append("You have to set an email address to order a product!")
            self.__get_template(self.shop_temaplte)
        elif self.email is not None and not MailSender.validate_email(self.email):
            self.error_messages.append("Your email address is not valid!")
            self.__get_template(self.shop_temaplte)
        elif self.product is None and self.email is None:
            self.__get_template(self.shop_temaplte)
        else:
            mail = MailSender(email)
            mail.send()
            self.__get_template(self.email_template)

    def __get_template(self, template):
        f = open(os.path.join(self.template_path, template))
        self.template = f.read()
        f.close()

    def __build_error_messages(self):
        error = ""
        for error_message in self.error_messages:
            error += self.error_template.format(error=error_message) + "<br>\n"
        return error

    def __str__(self):
        html = self.template_construct.format(content_type=self.content_type_template,
                                              error_messages=self.__build_error_messages(), main_content=self.template)
        return html


class MailSender:
    template = """From: {email}
    To: {receiver}
    Subject: Order Confirmation
    MIME-Version: 1.0
    Content-Type: text/html
    Content-Transfer-Encoding: quoted-printable
    
    {message}
    """

    template_message = """Hello there
    
    Thank you very much for your order at our online-shop. The product will be sent as fast as possible.
    
    We wish you a nice day!
    Bye
    """

    smtp_server = "smtp.gmail.com"
    smtp_ssl = True
    smtp_port = "465"
    smtp_email = "xxx@gmail.com"
    smtp_passwd = "xxx"

    EMAIL_REGEX = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")

    def __init__(self, receiver):
        self.message = ""
        self.receiver = receiver
        self.connection = None

    def __build_email(self):
        self.message = self.template.format(email=self.smtp_email, receiver=self.receiver,
                                            message=self.template_message)
        return self.message

    def __connect(self):
        if self.smtp_ssl:
            server = smtplib.SMTP_SSL(self.smtp_server, self.smtp_port)
        else:
            server = smtplib.SMTP(self.smtp_server, self.smtp_port)

        server.login(self.smtp_email, self.smtp_passwd)
        server.set_debuglevel(1)
        self.connection = server

    def send(self):
        self.__connect()
        self.__build_email()
        self.connection.sendmail(self.smtp_email, self.receiver, self.message)

    @staticmethod
    def validate_email(email):
        return MailSender.EMAIL_REGEX.match(email)


form = cgi.FieldStorage()
print(Shop(form.getvalue("product"), form.getvalue("email")))
