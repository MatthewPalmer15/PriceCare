import pythoncom
import os
from docx2pdf import convert

def convert_to_pdf(file):
    pythoncom.CoInitialize()
    convert(file, file.replace('.docx', '.pdf'))
    os.remove(file)
    return file.replace('.docx', '.pdf')

def format_date(date):
    """ Format a date to a string """
    return '{:%d %B %Y}'.format(date)


def calculate_weekly_total(subscriptions):
    """ Calculate the total amount of money paid per week """
    total = 0
    for subscription in subscriptions:
        if subscription.frequency.name == "1 week":
            total += subscription.amount
        elif subscription.frequency.name == "2 weeks":
            total += subscription.amount / 2
        elif subscription.frequency.name == "1 month":
            total += subscription.amount / 4
        elif subscription.frequency.name == "3 months":
            total += subscription.amount / 13
        elif subscription.frequency.name == "6 months":
            total += subscription.amount / 26
        elif subscription.frequency.name == "1 year":
            total += subscription.amount / 52
    return round(total, 2)


def calculate_monthly_total(subscriptions):
    """ Calculate the total amount of money paid per month """
    total = 0
    for subscription in subscriptions:
        if subscription.frequency.name == "1 week":
            total += subscription.amount * 4
        elif subscription.frequency.name == "2 weeks":
            total += subscription.amount * 2
        elif subscription.frequency.name == "1 month":
            total += subscription.amount
        elif subscription.frequency.name == "3 months":
            total += subscription.amount / 3
        elif subscription.frequency.name == "6 months":
            total += subscription.amount / 6
        elif subscription.frequency.name == "1 year":
            total += subscription.amount / 12
    return round(total, 2)


def calculate_yearly_total(subscriptions):
    """ Calculate the total amount of money paid per year """
    total = 0
    for subscription in subscriptions:
        if subscription.frequency.name == "1 week":
            total += subscription.amount * 52
        elif subscription.frequency.name == "2 weeks":
            total += subscription.amount * 26
        elif subscription.frequency.name == "1 month":
            total += subscription.amount * 12
        elif subscription.frequency.name == "3 months":
            total += subscription.amount * 4
        elif subscription.frequency.name == "6 months":
            total += subscription.amount * 2
        elif subscription.frequency.name == "1 year":
            total += subscription.amount
    return round(total, 2)
