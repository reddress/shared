package com.tinacg;

import static com.tinacg.util.Shortcuts.print;

public class MyMainMan {
    // in directory c:\Users\Heitor\Desktop\emacs-24.3\bin\shared\java\cookbook
    // > gradle build

    // If jar is activated in build.gradle
    // > java -ea -jar build/libs/cookbook-0.1.jar

    // otherwise
    // run.bat
    
    // p.36 1.12 Buggy
    /*
    static String name;
    */
    
    public static void main(String[] args) {
        // p. 35 1.11 AssertDemo
        /*
        int i = 4;
        if (args.length == 1) {
            i = Integer.parseInt(args[0]);
        }
        assert i > 0 : "i is non-positive";
        print("Hello after assertion");
        */

        // p. 36 1.12 Buggy
        /* // use jdb
        int n = name.length();
        print(n);

        name += "; the end.";
        print(name);
        */

        print("i is well");
    }
}
