// http://www.javaworld.com/article/2077424/learn-java/does-java-pass-by-reference-or-pass-by-value.html

class Point {
    int x;
    int y;
    public Point(int x, int y) {
        this.x = x;
        this.y = y;
    }
}

public class PassBy {
    public static void main(String[] args) {
        Point pnt1 = new Point(0, 0);
        Point pnt2 = new Point(0, 0);
        System.out.println("Pnt 1: " + pnt1.x + " " + pnt1.y);
        System.out.println("Pnt 2: " + pnt2.x + " " + pnt2.y);
        tricky(pnt1, pnt2);
        System.out.println("After tricky: ");
        System.out.println("Pnt 1: " + pnt1.x + " " + pnt1.y);
        System.out.println("Pnt 2: " + pnt2.x + " " + pnt2.y);        
    }
    public static void tricky(Point arg1, Point arg2) {
        Point temp = arg1;
        arg1 = arg2;
        arg2 = temp;

        arg1.x = 100;
        arg1.y = 100;
        // Java copies and passes the references by value
        // method manipulation alters the objects, but reference swap
        // does not work because the original references are not the
        // same as the copied ones inside the function
    }

}

