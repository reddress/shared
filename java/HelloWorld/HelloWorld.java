public class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello World");
        System.out.println(getNameTwice());
    }

    public static String getName() {
        return "Harry";
    }

    public static String getNameTwice() {
        return getName() + getName();
    }
}
