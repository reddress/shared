import java.util.*;

public class Scratch {
    public static <T> void print(T val) {
        System.out.println(val);
    }

    enum Size { Small, Medium, Large }

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
        
    }
}
