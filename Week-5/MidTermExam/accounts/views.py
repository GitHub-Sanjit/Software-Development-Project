from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm, SetPasswordForm
from django.views.generic import CreateView
from orders.models import OrderModel, OrderItemModel
from django.urls import reverse_lazy
from django.contrib.auth.models import User

from .forms import SignUpForm, UpdateUserForm
# Create your views here.

class UserSignUpView(CreateView):
    model = User
    form_class = SignUpForm
    template_name = 'sign_up.html'
    success_url = reverse_lazy("sign_in")

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect("home")
        return super().get(request, *args, **kwargs)

    def form_valid(self, form):
        messages.success(self.request, "Signed up Successfully")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.warning(self.request, "Invalid user Information")
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_type"] = "SignUp"
        return context


def sign_in(request):
    if request.user.is_authenticated:
        return redirect("home")
    if (request.method == "POST"):
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Logged in Successfully")
                return redirect("profile")
            else:
                messages.warning(request, "User not found")
                return redirect("register")
    else:
        form = AuthenticationForm()
    return render(request, "sign_in.html", {
        "form": form,
        "page_type": "SignIn",
    })


@login_required
def change_password(request):
    if (request.method == "POST"):
        form = SetPasswordForm(request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, "Password changed Successfully")
            return redirect("profile")
    else:
        form = SetPasswordForm(user=request.user)
    return render(request, "change_password.html", {"form": form, "page_type": "Change Password"})


def user_logout(request):
    logout(request)
    messages.success(request, "Logged out Successfully")
    return redirect("home")


@login_required
def profile(request):
    orders = OrderModel.objects.filter(
        user=request.user).order_by('-order_date')
    order_list = OrderItemModel.objects.filter(order__in=orders)
    total_price = sum(order.quantity * order.car.price for order in order_list)

    if request.method == "POST":
        form = UpdateUserForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile Updated Successfully")
            return redirect("profile")
    else:
        form = UpdateUserForm(instance=request.user)
    is_order_exists = len(order_list)

    return render(request, "profile.html", {
        "form": form,
        "page_type": "User Profile",
        "orders": order_list,
        "is_order_exists": is_order_exists,
        "total_price": total_price,
    })



