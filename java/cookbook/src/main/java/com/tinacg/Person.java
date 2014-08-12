package com.tinacg;

public class Person {
    String fname, lname;
    
    public Person(String fname, String lname) {
        this.fname = fname;
        this.lname = lname;
    }

    public String getFullName() {
        return (this.fname + this.lname).toLowerCase();
    }
}
