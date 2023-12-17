from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from orders.models import OrderModel, OrderItemModel
from django.views.generic import DetailView

from accounts.models import CarModel
from accounts.forms import CommentForm
# Create your views here.


class CarDetailsView(DetailView):
    model = CarModel
    template_name = "car_details.html"
    pk_url_kwarg = "id"

    def post(self, request, *args, **kwargs):
        comment_form = CommentForm(data=request.POST)
        car = self.get_object()

        if comment_form.is_valid():
            self.process_comment(request, comment_form, car)

        return self.get(request, *args, **kwargs)

    def process_comment(self, request, comment_form, car):
        new_comment = comment_form.save(commit=False)
        new_comment.email = request.user.email
        new_comment.car = car
        new_comment.save()
        messages.success(request, "Thanks for your comment")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        car = self.object
        comments = car.comments.order_by('-createdAt')
        comment_form = CommentForm()

        context.update({
            'car': car,
            'comments': comments,
            'comment_form': comment_form,
        })

        return context


@login_required
def buy_now(request, id):
    car = get_object_or_404(CarModel, pk=id)
    dynamic_url = reverse("car_details", args=[car.id])

    if car.quantity <= 0:
        messages.warning(request, "Sorry, the order is out of stock!")
        return redirect(dynamic_url)

    # Check if there are any existing orders and order items
    orders_exist = OrderModel.objects.exists()
    order_items_exist = OrderItemModel.objects.exists()

    if orders_exist and order_items_exist:
        order_item = OrderItemModel.objects.filter(
            car=car, order__user=request.user).first()

        if order_item:
            order_item.quantity += 1
            order_item.save()
            car.quantity = car.quantity - 1
            order_item.save()
            messages.success(
                request, f"Successfully added one more {car.car_name} to your order.")
        else:
            create_new_order(request, car)
        car.save()
    else:
        create_new_order(request, car)
    car.save()
    return redirect(dynamic_url)


def create_new_order(request, car):
    order = OrderModel(user=request.user, total_amount=car.price)
    order.save()

    order_item = OrderItemModel(order=order, car=car, quantity=1)
    order_item.save()

    car.quantity = car.quantity - 1
    messages.success(request, "Order placed successfully")
    car.save()
