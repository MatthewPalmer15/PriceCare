from datetime import datetime
from django.http import FileResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from docxtpl import DocxTemplate
from Subscriptions.forms import SubscriptionForm
from .models import Subscription
from .bgprocess import *

def dashboard(request):
    """ View all subscriptions that the user has defined """
    if request.user.is_authenticated:
        # Get all subscriptions that are linked to the user and renders to the dashboard template
        user_subscriptions = Subscription.objects.filter(user=request.user)
        user_subscriptions.order_by('provider__name')
        context = {
            "subscriptions": user_subscriptions,
            "weekly_total": calculate_weekly_total(user_subscriptions),
            "monthly_total": calculate_monthly_total(user_subscriptions),
            "yearly_total": calculate_yearly_total(user_subscriptions),
        }
        return render(request, 'subscriptions/dashboard.html', context)
    else:
        messages.error(request, message='You must be logged in to view this page',extra_tags='danger')
        return redirect('users_login')

def create_subscription(request):
    """ Create a new subscription """
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = SubscriptionForm(request.POST)
            if form.is_valid():
                form.save(commit=False)
                form.instance.user = request.user
                form.save()
                messages.success(request, message='Subscription added successfully', extra_tags='success')
                return redirect('subs_dashboard')
            else:
                messages.error(request, message='Subscription could not be added', extra_tags='danger')
                return render(request, 'subscriptions/create.html', {'form': form})
        else:
            form = SubscriptionForm()
            return render(request, 'subscriptions/create.html', {'form': form})
    else:
        messages.error(request, message='You must be logged in to view this page', extra_tags='danger')
        return redirect('users_login')

def delete_subscription(request, subscription_id):
    """ Delete a current subscription """
    if request.user.is_authenticated:
        subscription = Subscription.objects.get(id=subscription_id)
        if subscription.user == request.user:
            subscription.delete()
            messages.success(request, message='Subscription deleted successfully', extra_tags='success')
        else:
            messages.error(request, message='Subscription could not be deleted', extra_tags='danger')
        return redirect('subs_dashboard')
    else:
        messages.error(request, message='You must be logged in to view this page',extra_tags='danger')
        return redirect('users_login')

def edit_subscription(request, subscription_id):
    """ Edit a current subscription """
    if request.user.is_authenticated:
        subscription = Subscription.objects.get(id=subscription_id)
        if subscription.user == request.user:
            if request.method == 'POST':
                form = SubscriptionForm(request.POST, instance=subscription)
                if form.is_valid():
                    form.save()
                    messages.success(
                        request,
                        'Subscription updated successfully',
                        extra_tags='success'
                    )
                    return redirect('subs_dashboard')
                else:
                    messages.error(request, message='Subscription could not be updated', extra_tags='danger')
                    return render(request, 'subscriptions/edit.html', {'form': form})
            else:
                form = SubscriptionForm(instance=subscription)
                return render(request, 'subscriptions/edit.html', {'form': form})
        else:
            messages.error(request, message='Subscription could not be updated', extra_tags='danger')
            return redirect('subs_dashboard')
    else:
        messages.error(request, message='You must be logged in to view this page', extra_tags='danger')
        return redirect('users_login')

def download_statement(request):
    """ Download a DOCX statement of the user's subscriptions """
    subscriptions = Subscription.objects.filter(user=request.user).order_by('provider__name')
    current_date = datetime.now()
    doc = DocxTemplate("Static/invoices/template.docx")
    context = {
        'user': request.user,
        'subscriptions': subscriptions,
        'current_date': format_date(current_date),
        'weekly_total': calculate_weekly_total(subscriptions),
        'monthly_total': calculate_monthly_total(subscriptions),
        'yearly_total': calculate_yearly_total(subscriptions),
    }
    doc.render(context)
    doc.save(f"Static/invoices/{request.user.username}_invoice_{format_date(current_date)}.docx")
    filename = f"Static/invoices/{request.user.username}_invoice_{format_date(current_date)}.docx"
    response = FileResponse(open(filename, 'rb'))
    return response
