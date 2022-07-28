from datetime import datetime
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
from .forms import CreateUser, EditUserDetails, EditUserPassword, SupportTicketResponseForm, SupportTicketForm
from .models import User, SupportTicket, SupportTicketResponse

def view_user(request):
    """ Views the user profile """
    return render(request, "users/view.html", {})

def register_user(request):
    """ Registers a new user """
    if request.user.is_authenticated:
        redirect("/")
    if request.method == "POST":
        form = CreateUser(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Your account has been created", extra_tags='success')
            return redirect("/")
        else:
            for error in form.errors:
                messages.error(request, form.errors[error][0], extra_tags='danger')
            return render(request, "users/register.html", {'form': form})
    else:
        form = CreateUser()
        return render(request, "users/register.html", {'form': form})

def login_user(request):
    """ Logs in an existing user """
    if request.user.is_authenticated:
        redirect("/")
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f"You are now logged in as {request.user.username}", extra_tags='success')
            return redirect("/")
        else:
            messages.error(request, "Invalid Username or Password. Please Try Again", extra_tags='danger')
            return render(request, 'users/login.html', {})
    else:
        return render(request, 'users/login.html', {})

def logout_user(request):
    """ Logs out the user """
    logout(request=request)
    request.session.clear()
    messages.success(request, "You have been logged out", extra_tags='success')
    return redirect("/")

def delete_user(request):
    """ Deletes the current user'sa account """
    if request.user.is_authenticated:
        request.user.delete()
        messages.success(request, "Your account has been deleted", extra_tags='success')
        return redirect("/")
    else:
        messages.error(request, "Your account could not be deleted", extra_tags='success')
        return redirect("/")

def change_user_details(request):
    """ Changes the user's details """
    if request.user.is_authenticated:
        if request.method == "POST":
            form = EditUserDetails(request.POST, request.FILES, instance=request.user)
            if form.is_valid():
                form.save()
                messages.success(request, "Your account has been updated", extra_tags='success')
                return redirect("users_profile")
            else:
                for error in form.errors:
                    messages.error(request, form.errors[error][0], extra_tags='danger')
                return render(request, "users/change_details.html", {'form': form})
        else:
            form = EditUserDetails(instance=request.user)
            return render(request, "users/change_details.html", {'form': form})
    else:
        messages.error(request, "You are not logged in", extra_tags='danger')
        return redirect("/")

def change_user_password(request):
    """ Changes the user's password """
    if request.user.is_authenticated:
        if request.method == "POST":
            form = EditUserPassword(request.user, request.POST)
            if form.is_valid():
                user = form.save()
                update_session_auth_hash(request, user)
                messages.success(request, "Your password has been updated", extra_tags='success')
                return redirect("users_profile")
            else:
                for error in form.errors:
                    messages.error(request, form.errors[error][0], extra_tags='danger')
                return render(request, "users/change_password.html", {'form': form})
        else:
            form = EditUserPassword(user=request.user)
            return render(request, "users/change_password.html", {'form': form})
    else:
        messages.error(request, "You are not logged in", extra_tags='danger')
        return redirect("/")


def view_support(request):
    """ Views the support page """
    if request.user.is_authenticated:
        support_tickets = SupportTicket.objects.filter(user=request.user).order_by('is_closed', '-created_at')

        if request.method == "POST":
            form = SupportTicketResponseForm(request.POST, request.FILES)
            if form.is_valid():
                form.save(commit=False)
                form.instance.ticket = SupportTicket.objects.get(id=request.POST['ticket_id'])
                form.instance.user = request.user
                form.instance.created_at = datetime.now()
                form.save()
                messages.success(request, "Your response has been submitted", extra_tags='success')
                return redirect("users_support")
            else:
                for error in form.errors:
                    messages.error(request, form.errors[error][0], extra_tags='danger')
                return render(request, "users/support.html", {'form': form, 'support_tickets': support_tickets})
        else:
            form = SupportTicketResponseForm()
            context = {
                'support_tickets': support_tickets,
                'form': form,
            }
            return render(request, "support/view.html", context)
    else:
        messages.error(request, "You are not logged in", extra_tags='danger')
        return redirect("/")

def view_support_admin(request):
    """ Views the support page """
    if request.user.is_authenticated and request.user.is_superuser:
        all_support_tickets = SupportTicket.objects.all().exclude(is_closed=True).order_by('-created_at')

        if request.method == "POST":
            form = SupportTicketResponseForm(request.POST, request.FILES)
            if form.is_valid():
                form.save(commit=False)
                form.instance.ticket = SupportTicket.objects.get(id=request.POST['ticket_id'])
                form.instance.user = request.user
                form.instance.created_at = datetime.now()
                form.save()
                messages.success(request, "Your response has been submitted", extra_tags='success')
                return redirect("users_support_admin")
            else:
                for error in form.errors:
                    messages.error(request, form.errors[error][0], extra_tags='danger')
                return render(request, "users/support.html", {'form': form, 'support_tickets': all_support_tickets})
        else:
            form = SupportTicketResponseForm()
            context = {
                'support_tickets': all_support_tickets,
                'form': form,
            }
            return render(request, "support/view.html", context)
    else:
        messages.error(request, "You do not have the permissions for this", extra_tags='danger')
        return redirect("/")


def create_support_ticket(request):
    """ Creates a new support ticket """
    if request.user.is_authenticated:
        if request.method == "POST":
            form = SupportTicketForm(request.POST, request.FILES)
            if form.is_valid():
                form.save(commit=False)
                form.instance.user = request.user
                form.instance.created_at = datetime.now()
                form.save()
                messages.success(request, "Your support ticket has been submitted", extra_tags='success')
                return redirect("users_support")
            else:
                for error in form.errors:
                    messages.error(request, form.errors[error][0], extra_tags='danger')
                return render(request, "support/create.html", {'form': form})
        else:
            form = SupportTicketForm()
            return render(request, "support/create.html", {'form': form})
    else:
        messages.error(request, "You are not logged in", extra_tags='danger')
        return redirect("/")

def close_support_ticket(request, ticket_id):
    """ Closes a support ticket """
    if request.user.is_authenticated:
        ticket = SupportTicket.objects.get(user=request.user, id=ticket_id)
        ticket.is_closed = True
        ticket.save()
        SupportTicketResponse.objects.create(
            ticket=ticket,
            user=User.objects.get(username="Care Bot"),
            message="This ticket has been closed. You can no longer reply to it.",
            created_at=datetime.now()
        )
        messages.success(request, "Your ticket has been closed", extra_tags='success')
        return redirect("users_support")
    else:
        messages.error(request, "You are not logged in", extra_tags='danger')
        return redirect("/")
