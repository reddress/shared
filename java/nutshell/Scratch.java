import java.util.*;
import java.io.*;

import static util.Convenience.print;
// c.bat Scratch

class Scratch {
    public static void main(String[] args) {
        int[] lst = { 1, 2, 3 };
        int[] otherlst = lst;
        alterList(otherlst);
        print(lst[0]);
    }

    public static void alterList(int[] lst) {
        lst[0] = 10;
    }
}
