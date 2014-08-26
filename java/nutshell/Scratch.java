import java.util.*;
import java.io.*;

import static util.Convenience.print;

class Scratch {
    public static void main(String[] args) {
        String[] words = { " Hello" };
        Object[] objects = { 1, "2" };

        objects[1] = new Integer(9);
        print(objects[1]);
    }
}
