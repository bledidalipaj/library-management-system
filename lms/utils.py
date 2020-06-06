from django.core.mail import send_mail


STATUS_DICT = {
    'AV': 'Available',
    'CO': 'Checked Out',
    'LO': 'Lost'
}


def notify_patron_about_hold(hold):
    subject = f'{hold.library_asset.title} - Available for checkout'
    message = f'''
    {hold.library_asset.title} is available for checkout.
    Please visit {hold.library_asset.location}, to complete the checkout process.
    '''
    to_email = hold.library_card.patron.email
    send_mail(
        subject,
        message,
        '',
        [to_email],
    )
