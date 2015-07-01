import java.io.File;
import java.io.FileReader;

class UseCalculator {
    public static void main(String[] args) {
        DecimalCalculator dc = new DecimalCalculator();
        IntegerCalculator ic = dc;

        ic.boot();
        int s = ic.sum;
        System.out.println(s);

        /*
        File f = new File("UseCalculator.java");
        FileReader reader = new FileReader(f);
        reader.read(new char[(int) f.length()]);
        reader.close();
        */
        System.out.println(7/2);
    }
}
