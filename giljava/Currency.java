package com.tinacg.gilmera;

public class Currency {
    private String longName;
    private String id;
    private String symbol;

    public Currency(String longName, String id, String symbol) {
        this.longName = longName;
        this.id = id;
        this.symbol = symbol;
    }

    public String getLongName() {
        return this.longName;
    }
    
    public String getId() {
        return this.id;
    }

    public String getSymbol() {
        return this.symbol;
    }
}
