import java.util.*;

class Cat {
    String name;
    public Cat(String name) {
        this.name = name;
    }

    public static void meow() {
        System.out.println("Miau!");
    }
}

public class Scratch {
    public static <T> void print(T val) {
        System.out.println(val);
    }

    public static void main(String[] args) {
        Cat kat = new Cat("Kat");
        kat.meow();
    }
}
