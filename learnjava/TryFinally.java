public class TryFinally {
    public static void main(String[] args) {
        try {
            System.out.println("hello");
            return;

        } finally {
            assert false;
            System.out.println("world");
        }
    }
}
