import static myutil.Convenience.print;

import java.util.*;

public class Scratch {
    public static void main(String[] args) {
        print(inverse(Double.parseDouble(args[0])));
    }

    public static double inverse(double x) {
        try {
            return 1.0 / x;
        }
        catch (Exception e) {
            print("caught object");
            return 0;
        }
    }
}
