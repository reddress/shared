import java.util.*;

class Person {
    String myName;
    public Person(String name) {
        myName = name;
    }

    public Person() {
        myName = "Anonymous";
    }
    
    public void sayHi() {
        System.out.println("Hi, my name is " + myName);
    }
}

public class Scratch {
    public static <T> void print(T val) {
        System.out.println(val);
    }

    enum Size { Small, Medium, Large }

    // static inner class - better to place it outside without static
    // http://stackoverflow.com/a/70687/1238040
    private static class Mug {
        String color;
        private Mug(String s) {
            color = s;
        }
        public String getColor() {
            return "I am " + color;
        }
        
    }
    
    public static void main(String[] args) {
        System.out.println(9);
        {
            int a = 20;
            System.out.println(a);
        }
        int b = 3;
        if (b == 3) {
            System.out.println("b is 3");
        }
        print("o hai");

        for (String s = "Skill"; s.length() < 9; s += "z") {
            print(s);
        }

        int y = 0;
        for (int x = 0; x < 3; x++) {
            y += 10;
        }
        print(y);

        int[] arrayofInts = new int[] { 1, 2, 3, 4 };
        for (int i : arrayofInts) {
            print("square");
            print(i * i);
            print("cube");
            print(i * i * i);
        }

        List<String> listOfStr = new ArrayList<String>();
        listOfStr.add("foo");
        listOfStr.add("bar");
        for (String s : listOfStr) {
            print(s);
        }

        int c = 3;

        switch (c) {
        case 1:
            print("uno");
            break;
        case 3:
            print("tres");
            break;
        case 5:
            print("cinco");
            break;
        default:
            print("def");
            break;
        }

        Size sz = Size.Medium;

        switch (sz) {
        case Small:
            print("S");
            break;
        case Medium:
            print("M");
            break;
        default:
            print("unknown");
            break;
        }
        print(1+2*3);
        int[] aNull = null;
        // for (int i : aNull) {
        //     print(i);      NullPointerException
        // }
        print("o hai");

        Person bob = new Person("bob");
        bob.sayHi();

        Person[] people = new Person[5];

        // Strings have length() method
        print("ABC".length());

        // arrays have length property
        print(people.length);

        Mug mug = new Mug("yellow");
        print(mug.getColor());

        Mug mug2 = new Mug("red");
        print(mug2.getColor());

        print(mug.getColor());

        Pendulum p;
        p = new Pendulum();

        p.mass = 5.0;
        print(p.getDoubleMass());

        Pendulum bigP = new Pendulum();
        bigP.mass = 20.0;
        bigP.gravAccel = 12.0f;

        print(p.gravAccel);

        String myString = "abc";

        alterColortoGreen(mug);
        print(mug.getColor());
    }
    public static void alterColortoGreen(Mug m) {
        m.color = "Green";
    }
}

class Pendulum {
    double mass;
    double length = 1.0;
    int cycles;
    static float gravAccel = 9.80f;  // static member is associated with the class, not any individual instance
    static final float EARTH_G = 9.80f;  // final marks variable as constant
    
    double getPosition(double time) {
        return 1.0;
    }
    double getDoubleMass() {
        return mass * 2.0;
    }
}

