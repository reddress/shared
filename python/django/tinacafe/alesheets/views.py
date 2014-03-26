from itertools import chain

from django.shortcuts import render, get_object_or_404

from .models import Owner, AccountType, Account, Transaction

def index(request):
    return render(request, 'alesheets/index.html')

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
        

def show_account(request, short_name):
    account = get_object_or_404(Account, short_name=short_name)
    debit_transactions = Transaction.objects.filter(debit=account)
    credit_transactions = Transaction.objects.filter(credit=account)
    raw_transactions = sorted(chain(debit_transactions,
                                    credit_transactions),
                              key=lambda tr: tr.date)
    all_transactions = []
    balance = 0
    for transaction in raw_transactions:
        row_data = get_transaction_html(transaction, account, balance)
        all_transactions.append(row_data[0])
        balance = row_data[1]
        
    #all_transactions = map(lambda tr: get_transaction_html(tr, account),
    #                       all_transactions)

    # compute balance
    # something like
    # for transaction in all_transactions[::-1]:
    # 
    return render(request, 'alesheets/showaccount.html', { 'accountname': account.name, 'transactions': all_transactions })

