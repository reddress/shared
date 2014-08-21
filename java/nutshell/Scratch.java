import java.util.*;
import java.io.*;

class Scratch {
    public static void main(String[] args) throws InterruptedException {
        countdown(9);
    }

    public static void countdown(int from) throws InterruptedException {
        for (; from > 0; from--) {
            Thread.sleep(200);
            print(from);
        }
    }
    public static int getNumber(Object o) {
        String s = "one";
        return (int) o;
    }

    public static int divideBy(int x) {
        try {
            print("trying " + x);
            return 3 / x;
        }
        catch (NullPointerException e) {
            e.printStackTrace();
        }
        finally {
            print("in finally block");
            return 10;
        }
    }
    public static void printRem(int x) {
        if (x % 2 == 0) {
            print("no rem");
            return;
        }
        print("remainder 1");
    }

    public static <T> void print(T arg) {
        System.out.println(arg);
    }
}
