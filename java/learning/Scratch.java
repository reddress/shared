import java.util.*;
import static myutil.Convenience.print;
import java.text.*;

public class Scratch {
    public static void main(String[] args) {
        Cat kat = new Cat("Kat");
        kat.meow();
        print(55);
        System.out.printf("pos num +%d %n", 1435029199);
        print(MessageFormat.format("{0} + {0} = {1}", 3, 4, 7));
    }
}
