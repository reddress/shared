package com.tinacg;

import org.junit.*;
import static org.junit.Assert.*;

public class PersonTest {
    @Test
    public void testNameConcat() {
        Person p = new Person("Jack", "Murphy");
        String f = p.getFullName();
        assertEquals("Name concat", "jackmurphy", f);
    }
}
