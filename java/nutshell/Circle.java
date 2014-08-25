public class Circle {
    public static final double PI = 3.141592;

    public static double radiansToDegrees(double radians) {
        return radians * 180 / PI;
    }

    public double area() {
        return PI * r * r;
    }

    public double circumference() {
        return 2 * PI * r;
    }

    public Circle(double r) {
        this.r = r;
    }

    public Circle() {
        this(1.0);
    }
    public double r = 9.0;

}
