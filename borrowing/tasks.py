from celery import shared_task
from utils import send_telegram_message


@shared_task
def notify_new_borrowing(user, book):
    message = f"New borrowing!\nUser: {user}\nBook: {book}"
    send_telegram_message(message)


@shared_task
def notify_overdue_borrowing(user, book, days_overdue):
    message = (
        f"Overdue Borrowing!\nUser: {user}\nBook: {book}\nDays Overdue: {days_overdue}"
    )
    send_telegram_message(message)


@shared_task
def notify_successful_payment(user, amount):
    message = f"Successful payment!\nUser: {user}\nAmount: {amount} USD"
    send_telegram_message(message)
