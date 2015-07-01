package com.tinacg.gilmera;

public class Account {
    private String longName;
    private String id;

    public Account(String longName, String id) {
        this.longName = longName;
        this.id = id;
    }

    public String getId() {
        return this.id;
    }

    public String toString() {
        return this.longName + "(" + this.id + ")";
    }
}
