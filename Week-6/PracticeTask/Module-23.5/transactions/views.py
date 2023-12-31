from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils import timezone
from django.shortcuts import get_object_or_404, redirect
from django.views import View
from django.http import HttpResponse
from django.views.generic import CreateView, ListView, FormView
from transactions.constants import DEPOSIT, WITHDRAWAL, LOAN, LOAN_PAID, MONEY_TRANSFER
from datetime import datetime
from django.db.models import Sum
from transactions.forms import (
    DepositForm,
    WithdrawForm,
    LoanRequestForm,
    MoneyTransferForm
)
from accounts.models import UserBankAccount
from transactions.models import Transaction
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


def send_transaction_email(user, amount, subject, template):
    message = render_to_string(template, {
        'user': user,
        'amount': amount,
    })
    send_email = EmailMultiAlternatives(subject, '', to=[user.email])
    send_email.attach_alternative(message, "text/html")
    send_email.send()


class TransactionCreateMixin(LoginRequiredMixin, CreateView):
    template_name = 'transactions/transaction_form.html'
    model = Transaction
    title = ''
    success_url = reverse_lazy('transaction_report')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({
            'account': self.request.user.account
        })
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)  # template e context data pass kora
        context.update({
            'title': self.title
        })

        return context


class DepositMoneyView(TransactionCreateMixin):
    form_class = DepositForm
    title = 'Deposit'

    def get_initial(self):
        return {'transaction_type': DEPOSIT}

    def form_valid(self, form):
        amount = form.cleaned_data.get('amount')
        account = self.request.user.account
        if account.is_bankrupt:
            messages.error(
                self.request, "Sorry, deposits are not allowed for bankrupt accounts.")
            return self.form_invalid(form)

        account.balance += amount
        account.save(update_fields=['balance'])

        messages.success(
            self.request,
            f'{"{:,.2f}".format(float(amount))}$ was deposited to your account successfully'
        )
        send_transaction_email(
            self.request.user, amount, "Deposit Message", 'transactions/deposit_email.html')
        return super().form_valid(form)


class WithdrawMoneyView(TransactionCreateMixin):
    form_class = WithdrawForm
    title = 'Withdraw Money'

    def get_initial(self):
        initial = {'transaction_type': WITHDRAWAL}
        return initial

    def form_valid(self, form):
        amount = form.cleaned_data.get('amount')
        account = self.request.user.account

        if account.is_bankrupt:
            messages.error(
                self.request, "Sorry, withdrawals are not allowed for bankrupt accounts.")
            return self.form_invalid(form)

        if account.balance >= amount:
            account.balance -= amount
            account.save(update_fields=['balance'])

            messages.success(
                self.request,
                f'Successfully withdrawn {"{:,.2f}".format(float(amount))}$ from your account'
            )
        else:
            messages.error(
                self.request, "Insufficient balance for withdrawal.")
        send_transaction_email(
            self.request.user, amount, "Withdraw Message", 'transactions/withdraw_email.html')
        return super().form_valid(form)


class LoanRequestView(TransactionCreateMixin):
    form_class = LoanRequestForm
    title = 'Request For Loan'

    def get_initial(self):
        return {'transaction_type': LOAN}

    def form_valid(self, form):
        amount = form.cleaned_data.get('amount')
        account = self.request.user.account

        if account.is_bankrupt:
            messages.error(
                self.request, "Sorry, loan request are not allowed for bankrupt accounts.")
            return self.form_invalid(form)
        else:
            current_loan_count = Transaction.objects.filter(
                account=self.request.user.account, transaction_type=3, loan_approve=True).count()
            if current_loan_count >= 3:
                return HttpResponse("You have cross the loan limits")
            messages.success(
                self.request,
                f'Loan request for {"{:,.2f}".format(float(amount))}$ submitted successfully'
            )

        send_transaction_email(
            self.request.user, amount, "Loan Request Message", 'transactions/loan_email.html')
        return super().form_valid(form)


class TransactionReportView(LoginRequiredMixin, ListView):
    template_name = 'transactions/transaction_report.html'
    model = Transaction
    balance = 0  # filter korar pore ba age amar total balance ke show korbe

    def get_queryset(self):
        queryset = super().get_queryset().filter(
            account=self.request.user.account
        )
        start_date_str = self.request.GET.get('start_date')
        end_date_str = self.request.GET.get('end_date')

        if start_date_str and end_date_str:
            start_date = datetime.strptime(start_date_str, '%Y-%m-%d').date()
            end_date = datetime.strptime(end_date_str, '%Y-%m-%d').date()

            queryset = queryset.filter(
                timestamp__date__gte=start_date, timestamp__date__lte=end_date)
            self.balance = Transaction.objects.filter(
                timestamp__date__gte=start_date, timestamp__date__lte=end_date
            ).aggregate(Sum('amount'))['amount__sum']
        else:
            self.balance = self.request.user.account.balance

        return queryset.distinct()  # unique queryset hote hobe

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'account': self.request.user.account
        })

        return context


class PayLoanView(LoginRequiredMixin, View):
    def get(self, request, loan_id):
        loan = get_object_or_404(Transaction, id=loan_id)
        print(loan)
        if loan.loan_approve:
            user_account = loan.account
            # Reduce the loan amount from the user's balance
            # 5000, 500 + 5000 = 5500
            # balance = 3000, loan = 5000
            if loan.amount < user_account.balance:
                user_account.balance -= loan.amount
                loan.balance_after_transaction = user_account.balance
                user_account.save()
                loan.loan_approved = True
                loan.transaction_type = LOAN_PAID
                loan.save()
                return redirect('transactions:loan_list')
            else:
                messages.error(
                    self.request,
                    f'Loan amount is greater than available balance'
                )

        return redirect('loan_list')


class LoanListView(LoginRequiredMixin, ListView):
    model = Transaction
    template_name = 'transactions/loan_request.html'
    context_object_name = 'loans'  # loan list ta ei loans context er moddhe thakbe

    def get_queryset(self):
        user_account = self.request.user.account
        queryset = Transaction.objects.filter(
            account=user_account, transaction_type=3)
        print(queryset)
        return queryset


class MoneyTransferView(FormView):
    template_name = 'transactions/transfer_form.html'
    form_class = MoneyTransferForm
    title = 'Money transfer'
    success_url = reverse_lazy('money_transfer')

    def get_initial(self):
        return {'transaction_type': MONEY_TRANSFER}

    def form_valid(self, form):
        sender_account = UserBankAccount.objects.get(user=self.request.user)
        recipient_account_no = form.cleaned_data['recipient_account_no']
        transfer_amount = form.cleaned_data['transfer_amount']
        recipient_account = UserBankAccount.objects.filter(
            account_no=recipient_account_no
        ).first()
        print(recipient_account.user.email,sender_account.user.email)

        account = self.request.user.account

        if account.is_bankrupt:
            self.handle_bankrupt_error()
            return self.form_invalid(form)

        # if not recipient_account:
        #     messages.error(self.request, 'Recipient account does not exist.')
        #     return self.form_invalid(form)

        if not recipient_account:
            self.handle_recipient_error()
            return self.form_invalid(form)

        if sender_account.balance < transfer_amount:
            self.handle_insufficient_balance_error()
            return self.form_invalid(form)

        sender_account.money_transfer(recipient_account, transfer_amount)
        self.handle_success_message(transfer_amount)

        send_transaction_email(sender_account.user, transfer_amount,
                               "Money Transfer Sent", 'transactions/money_transfer_mail.html')
        send_transaction_email(recipient_account.user, transfer_amount,
                               "Money Transfer Received", 'transactions/money_received_mail.html')

        return super().form_valid(form)

    def handle_bankrupt_error(self):
        messages.error(
            self.request, "Sorry, Money Transfer Failed. Because this bank is bankrupt.")

    def handle_recipient_error(self):
        messages.error(self.request, 'Recipient account does not exist.')

    def handle_insufficient_balance_error(self):
        messages.error(
            self.request, 'Sorry, Transfer amount exceeds your available balance.')

    def handle_success_message(self, transfer_amount):
        formatted_amount = "{:,.2f}".format(float(transfer_amount))
        messages.success(
            self.request, f'Successfully sent {formatted_amount}$ from your account')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'title': self.title})
        return context
