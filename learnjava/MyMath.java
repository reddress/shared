import static assist.Shortcuts.print;

public class MyMath {
    private static int someConst;
    private static String someStr;
    
    private static int Fibo(int n) {
        if (n < 1) {
            return 1;
        } else {
            return Fibo(n - 1) + Fibo(n - 2);
        }
    }

    public static void main(String[] args) {
        for (int i = 0; i < 9; i++) {
            print(Fibo(i));
        }
        print(someConst);
        print(someStr);
    }
}
