import java.util.*;
import java.io.*;

import static util.Convenience.print;

// TO RUN:
// c.bat Scratch

class Dog {
    static class Toy {
        static class Wheel {
            static int roundness = 96;
        }
        static int wheels = 4;
    }

    static void showInner() {
        print(Toy.Wheel.roundness);
    }
}

class Scratch {
    public static void main(String[] args) {
        Dog d = new Dog();
        d.showInner();
    }
}
