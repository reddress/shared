import java.util.*;

public class Scratch {
    public static <T> void print(T val) {
        System.out.println(val);
    }

    public static void main(String[] args) {
        print("Hello");
        int foo;
        int bar = 3;
        boolean baz = false;
        if(baz = true) {  // compiler does not flag unintentional assignment
            foo = 42;
            print(foo);
        }
        Float f = new Float("3.0");
        print(f.longValue());

        Integer i = 1234567890;
        Integer j = 1234567890;
        print(i == j);  // false

        print(i.equals(j));  // true
        
        Integer n = 2;
        Integer m = 2;
        print(n == m);  // true because value is small (< 127)
    }
}
