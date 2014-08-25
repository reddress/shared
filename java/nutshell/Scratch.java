import java.util.*;
import java.io.*;

import static util.Convenience.print;

class Scratch {
    public static void main(String[] args) {
        Double d = new Double(10);
        print(d.i);
    }
}

class Single {
    int i = 0;
    Single(int i) {
        this.i = i;
    }
}

class Double extends Single {
    Double(int mario) {
        super(mario*3);
    }
    Double() {
        super(2);
        this.i = 18;
    }
}

