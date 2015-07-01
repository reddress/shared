import java.util.ArrayList;
import java.util.List;

public class UseArrayList {
    public static void main(String[] args) {
        List myList = new ArrayList();
        Integer thirty = new Integer(30);
        myList.add(thirty);

        myList.add("seventy");

        for (int i = 0; i < 2; i++) {
            int n = (int) myList.get(i);  // ClassCastException
            System.out.println(n);
        }
    }
}
