import java.util.*;
import java.io.*;

class Dog {
    public void answer() {
        System.out.println("Yes this is dog");
    }
}

class Point {
    public double x, y;
    public Point(double x, double y) {
        this.x = x; this.y = y;
    }
    public double sum() {
        return this.x + this.y;
    }
    public void setX(double newx) {
        this.x = newx;
    }
    @Override
    public String toString() {
        return "regular point " + this.x + this.y;
    }
}

class ColoredPoint extends Point {
    public String color;
    public ColoredPoint(String color) {
        super(1.0, 2.0);
        this.color = color;
    }
    @Override
    public String toString() {
        return this.color + this.x + this.y;
    }
}

class Scratch {
    public static void main(String[] args) {
        short m = 2;
        short n = 4;
        boolean b = true;

    }

    public static void setHeadToZero(int[] arr) {
        arr[0] = 0;
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
