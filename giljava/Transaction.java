package com.tinacg.gilmera;

public class Transaction {
    // private Date date;
    private Amount amount;
    private Account debit;
    private Account credit;

    public Transaction(String dateStr, String timezone,
                       String description, Amount amount,
                       Account debit, Account credit) {
        this.amount = amount;
        this.debit = debit;
        this.credit = credit;
    }

    public Amount getAmount() {
        return this.amount;
    }

    public String getDebitId() {
        return this.debit.getId();
    }

    public String getCreditId() {
        return this.credit.getId();
    }
}
