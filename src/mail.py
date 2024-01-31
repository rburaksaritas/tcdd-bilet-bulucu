import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import config

def send_email(tren_adi, binis_tarih, vagon_no, seat_no):
    message = MIMEMultipart()
    message['From'] = config.email_address
    message['To'] = config.destination_address
    message['Subject'] = f'Available Seat: {seat_no}, Vagon {vagon_no}, {binis_tarih}'

    body = f"An available seat has been found on {tren_adi} for the journey on {binis_tarih}. " \
           f"Seat {seat_no} in Wagon {vagon_no} is available."
    message.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP('smtp.office365.com', 587)
    server.starttls()
    server.login(config.email_address, config.email_password)
    text = message.as_string()
    server.sendmail(config.email_address, config.destination_address, text)
    server.quit()
    print(f"Email sent for Seat {seat_no} in Wagon {vagon_no} of {tren_adi} on {binis_tarih}.")
