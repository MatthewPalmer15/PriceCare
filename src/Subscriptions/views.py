from django.shortcuts import redirect, render
from django.contrib import messages
from Subscriptions.forms import CreateSubscription
from .models import Subscription
from .bgprocess import calculate_monthly_total, calculate_weekly_total, calculate_yearly_total

def dashboard(request):
    if request.user.is_authenticated:
        user_subscriptions = Subscription.objects.filter(user=request.user).order_by('provider__name')
        context = {
            "subscriptions": user_subscriptions,
            "weekly_total": calculate_weekly_total(user_subscriptions),
            "monthly_total": calculate_monthly_total(user_subscriptions),
            "yearly_total": calculate_yearly_total(user_subscriptions),
        }
        return render(request, 'subscriptions/dashboard.html', context)
    else:
        messages.error(request, 'You must be logged in to view this page', extra_tags='danger')
        return redirect('users_login')

def create_subscription(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = CreateSubscription(request.POST)
            if form.is_valid():
                form.save(commit=False)
                form.instance.user = request.user
                form.save()
                messages.success(request, 'Subscription added successfully', extra_tags='success')
                return redirect('subs_dashboard')
            else:
                messages.error(request, 'Subscription could not be added', extra_tags='danger')
                return render(request, 'subscriptions/create.html', {'form': form})
        else:
            form = CreateSubscription()
            return render(request, 'subscriptions/create.html', {'form': form})
    else:
        messages.error(request, 'You must be logged in to view this page', extra_tags='danger')
        return redirect('users_login')

def delete_subscription(request, id):
    if request.user.is_authenticated:
        subscription = Subscription.objects.get(id=id)
        if subscription.user == request.user:
            subscription.delete()
            messages.success(request, 'Subscription deleted successfully', extra_tags='success')
        else:
            messages.error(request, 'Subscription could not be deleted', extra_tags='danger')
        return redirect('subs_dashboard')
    else:
        messages.error(request, 'You must be logged in to view this page', extra_tags='danger')
        return redirect('users_login')

