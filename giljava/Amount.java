package com.tinacg.gilmera;

import java.math.BigDecimal;

public class Amount {
    private Currency currency;
    private BigDecimal figure;  // just the number

    public Amount(String figureStr, Currency currency) {
        figureStr = figureStr.replace(',', '.');
        try {
            this.figure = new BigDecimal(figureStr);
        } catch (NumberFormatException nfe) {
            System.err.println("Warning: could not parse figure " + figureStr);
            this.figure = new BigDecimal("0.00");
        }
        this.currency = currency;
    }

    public Amount(BigDecimal figure, Currency currency) {
        this.figure = figure;
        this.currency = currency;
    }

    public String toString() {
        return this.currency.getSymbol() + this.figure;
    }

    public String toVerboseString() {
        return this.figure + " " + this.currency.getLongName();
    }

    public String getCurrency() {
        return this.currency.getId();
    }
    
    public BigDecimal getFigure() {
        return this.figure;
    }

    public Amount add(Amount addend) {
        // FIXME Check that currencies match
        // if (this.currency 
        return new Amount(this.getFigure().add(addend.getFigure()), this.currency);
    }
}
