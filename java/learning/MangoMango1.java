import java.awt.*;
import javax.swing.*;

public class MangoMango1 {
    public static void main(String[] args) {
        JFrame frame = new JFrame("the frame");

        frame.setLayout(new FlowLayout());
        frame.add(new JLabel("Mango"));
        frame.add(new JButton("Mango"));

        frame.setLocation(100, 100);
        frame.pack();
        frame.setVisible(true);
    }
}
