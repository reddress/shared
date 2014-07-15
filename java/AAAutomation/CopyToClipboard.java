// http://stackoverflow.com/questions/6710350/copying-text-to-the-clipboard-using-java

import java.awt.datatransfer.*;
import java.awt.Toolkit;

public class CopyToClipboard {
    public static void main(String[] args) {
        StringSelection ss = new StringSelection(args[0]);
        Clipboard cb = Toolkit.getDefaultToolkit().getSystemClipboard();
        cb.setContents(ss, null);
    }
}
