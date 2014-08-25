import java.util.*;
import java.io.*;

import static util.Convenience.print;

class Boy {
    String name;
    public Boy(String name) {
        this.name = name;
    }
}

class Scratch {
    public static void main(String[] args) {

    }

    public static int useFactorial() {
        try {
            print(factorial(-9));
            File f = new File("notes.txt");
            BufferedReader reader = new BufferedReader(new FileReader(f));
            
        }
        catch (IOException e) {
            print("caught an exception");
        }
        finally {
            print("in finally");

        }
        return 0;
    }



    
    public static double factorial(int x) {
        if (x < 0) {
            throw new IllegalArgumentException("x must be >= 0");
        }
        double fact;
        for (fact = 1.0; x > 1; fact *= x, x--)
            ;
        return fact;
    }
}
