package com.tinacg;

import java.util.regex.*;
import java.util.*;
import java.text.*;
import java.time.*;
import java.time.format.*;

import static com.tinacg.util.Convenience.print;

public class Scratch {
    // in folder shared\java\cookbook
    // c.bat

    public static void main(String[] args) {
        // p. 184

        // p. 529
        print(Locale.getDefault());
        Locale.setDefault(Locale.US);
        
        DateTimeFormatter df = DateTimeFormatter.ofPattern("yyyy MMMM cccc");
        print(df.format(LocalDate.now()));

        // p. 180
        /*
        Date endOfTime = new Date(Long.MAX_VALUE);
        print(endOfTime);
        */
        
        // p. 530
        /*
        Object[] values = {"ough", "different", 10, "pronunciations"};
        String result = MessageFormat.format("thr{0}, c{0}, d{0} have {1} {2} {3}", values);

        print(result);
        */

        
        // p. 120
        /*
        String patt = "\\bfavor\\b";
        String input = "Do me a favor? Fetch my favorite";
        Matcher m = Pattern.compile(patt).matcher(input);

        StringBuffer sb = new StringBuffer();
        while (m.find()) {
            m.appendReplacement(sb, "favour");
        }
        print(sb);
        */
        
        // p. 118
        /*
        String patt = "Q[^u]\\d+\\.";
        Pattern r = Pattern.compile(patt);
        String line = "Order QT100. now";
        Matcher m = r.matcher(line);
        if (m.find()) {
            print(patt + " matches \"" + m.group(0) +
                  "\" in \"" + line + "\"");
        }
        else {
            print("no match");
        }
        */
        
        // p. 114
        /*
        String pattern = "^Q[^u]\\d+.";
        String[] input = {
            "QA777 is the next flight",
            "Qo1uack QACK Quack",
            "QZ29. zfoijw",
            "QA777. QZ999."
        };

        Pattern p = Pattern.compile(pattern);
        for (String in : input) {
            // matches() is used to match the entire region
            // lookingAt() does not require that the entire region matches
            // find(int start) begins at the specified index
            boolean found = p.matcher(in).lookingAt();
            
            print(in);
            if (found) {
                print(pattern + " matches " + in);
            }
        }
        */
    }
}
