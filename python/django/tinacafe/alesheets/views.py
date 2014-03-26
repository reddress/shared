from itertools import chain
from datetime import datetime, timedelta

from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import Owner, AccountType, Account, Transaction

@login_required
def index(request):
    asset_accounts = Account.objects.filter(type__name="Asset")
    expense_accounts = Account.objects.filter(type__name="Expense")
    liability_accounts = Account.objects.filter(type__name="Liability")
    equity_accounts = Account.objects.filter(type__name="Equity")
    income_accounts = Account.objects.filter(type__name="Income")

    return render(request, 'alesheets/index.html',
                  { 'asset_accounts': asset_accounts,
                    'expense_accounts': expense_accounts,
                    'liability_accounts': liability_accounts,
                    'equity_accounts': equity_accounts,
                    'income_accounts': income_accounts })

def get_transaction_html(transaction, account, balance):
    sign = account.type.sign_modifier
    if str(transaction.credit) == str(account.short_name):
        sign *= -1
        
    new_balance = balance + (sign * transaction.value)
    table_row = """<tr>
    <td><a href="/admin/alesheets/transaction/%s/" target="alesheets_admin">
          %s</a</td>
    <td>%s/%s/%s %02d:%02d</td> <!-- Date -->
    <td>%s</td> <!-- Description -->""" % (transaction.id,
                                           transaction.id,
                                           transaction.date.year,
                                           transaction.date.month,
                                           transaction.date.day,
                                           transaction.date.hour,
                                           transaction.date.minute,
                                           transaction.description)

    if str(transaction.debit) == str(account.short_name):
        table_row += '''
        <td>%.2f</td>
        <td><a href="../%s">%s</a></td>''' % (transaction.value,
                                              transaction.credit,
                                              transaction.credit)
    else:
        table_row += '''
        <td><a href="../%s">%s</a></td>
        <td>%.2f</td>
        ''' % (transaction.debit, transaction.debit, transaction.value)

    table_row += '<td>%.2f</td></tr>' % new_balance
    
    return (table_row, new_balance)
        
@login_required
def show_account(request, short_name):
    asset_accounts = Account.objects.filter(type__name="Asset")
    expense_accounts = Account.objects.filter(type__name="Expense")
    liability_accounts = Account.objects.filter(type__name="Liability")
    equity_accounts = Account.objects.filter(type__name="Equity")
    income_accounts = Account.objects.filter(type__name="Income")
    
    account = get_object_or_404(Account, short_name=short_name)
    debit_transactions = Transaction.objects.filter(debit=account,
                                date__gt=(datetime.today()-timedelta(days=31)))
    credit_transactions = Transaction.objects.filter(credit=account,
                                date__gt=(datetime.today()-timedelta(days=31)))
    raw_transactions = sorted(chain(debit_transactions,
                                    credit_transactions),
                              key=lambda tr: tr.date)
    all_transactions = []
    balance = 0
    for transaction in raw_transactions:
        row_data = get_transaction_html(transaction, account, balance)
        all_transactions.append(row_data[0])
        balance = row_data[1]
        
    return render(request, 'alesheets/showaccount.html',
                  { 'account_name': account.name,
                    'account_short_name': account.short_name,
                    'transactions': all_transactions,
                    'asset_accounts': asset_accounts,
                    'expense_accounts': expense_accounts,
                    'liability_accounts': liability_accounts,
                    'equity_accounts': equity_accounts,
                    'income_accounts': income_accounts })
                    


def user_login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return HttpResponseRedirect('/alesheets/')
    else:
        return HttpResponse('User not found or password incorrect. <a href="/alesheets/login/">try again</a>')

def user_logout(request):
    logout(request)
    return render(request, 'registration/logout.html')
