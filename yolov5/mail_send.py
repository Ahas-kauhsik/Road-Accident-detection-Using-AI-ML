import smtplib
from email.message import EmailMessage
import imghdr

def send_notification(data,image_path):
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("ahaskaushik@gmail.com", "mvzk xcgb arno jrsl")
    messages = data
    #s.sendmail("ahaskaushik@gmail.com", "kushalbandi8@gmail.com", messages)

    # create an email message object
    message = EmailMessage()
      
    # open image as a binary file and read the contents
    with open(image_path, 'rb') as file:
       image_data = file.read()
      
    message.set_content("The accident detected on road(road name) (co-ordinates)")
    # attach image to email
    message.add_attachment(image_data, maintype='image', subtype=imghdr.what('Unknown', image_data))
    s.sendmail("ahaskaushik@gmail.com", "kushalbandi8@gmail.com", message.as_string())
    s.quit()
    print('Mail has sent..!')
    return
