package com.tinacg.gilmera;

import java.util.List;
import java.util.ArrayList;
import java.util.Map;
import java.util.HashMap;
import java.math.BigDecimal;

public class User {

    // default timezone?
    
    private String username;
    private Map<String, Currency> currencies;
    private Map<String, Account> accounts;
    private List<Transaction> transactions;
    private Map<String, Map<String, Amount>> accountBalances;

    public User(String username) {
        this.username = username;
        this.currencies = new HashMap<String, Currency>();
        this.accounts = new HashMap<String, Account>();
        this.transactions = new ArrayList<Transaction>();
        this.accountBalances = new HashMap<String, Map<String, Amount>>();
    }

    public void addCurrency(Currency currency) {
        currencies.put(currency.getId(), currency);
    }

    public Currency getCurrency(String id) {
        return currencies.get(id);
    }

    public void addAccount(Account account) {
        accounts.put(account.getId(), account);
    }

    public Account getAccount(String id) {
        return accounts.get(id);
    }

    public void addTransaction(Transaction transaction) {
        this.transactions.add(transaction);
    }

    public HashMap<String, Amount> createZeroBalances() {
        HashMap<String, Amount> zeroBalances = new HashMap<String, Amount>();
        for (Currency currency : this.currencies.values()) {
            zeroBalances.put(currency.getId(), new Amount("0.00", currency));
        }
        
        return zeroBalances;
    }
        
    public void initializeBalances() {
        // set accountBalances values to 0
        for (Account account : this.accounts.values()) {
            //
            System.out.println(account.getId());
            accountBalances.put(account.getId(), createZeroBalances());
        }
    }
    
    public void computeBalances(List<Transaction> transactions) {
        initializeBalances();
    }

    // FIXME make it private
    public void addToAccountBalance(String accountId, String currencyId, Amount newAmount) {
        Amount currentAmount = getAccountBalance(accountId, currencyId);
        accountBalances.get(accountId).put(currencyId, currentAmount.add(newAmount));
    }

    public Amount getAccountBalance(String accountId, String currencyId) {
        return accountBalances.get(accountId).get(currencyId);
    }

    public HashMap<String, Amount> accountSummary(List<Transaction> transactions, String accountId) {
        HashMap<String, Amount> totals = new HashMap<String, Amount>();
        for (Currency currency : this.currencies.values()) {
            totals.put(currency.getId(), new Amount("0.00", currency));
        }
        
        for (Transaction transaction : this.transactions) {
            String transactionCurrency = transaction.getAmount().getCurrency();

            // FIXME currently only adds debit
            if (transaction.getDebitId().equals(accountId)) {
                totals.put(transactionCurrency,
                           totals.get(transactionCurrency).add(transaction.getAmount()));
            }
        }
        return totals;
    } 

    public List<Transaction> getAllTransactions() {
        return this.transactions;
    }
    
    // simply add all transaction values
    public BigDecimal simplySumTransactions() {
        BigDecimal total = new BigDecimal("0.00");
        for (Transaction transaction : this.transactions) {
            total = total.add(transaction.getAmount().getFigure());
        }
        return total;
    }

    // filter List of transactions
    // public ArrayList<Transaction> filterList(
    
}
