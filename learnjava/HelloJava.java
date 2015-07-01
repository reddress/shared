import javax.swing.*;
import java.awt.FlowLayout;
import java.awt.Dimension;

public class HelloJava {
    public static void main(String[] args) {
        JFrame frame = new JFrame("Hello Java window title");
        JLabel label = new JLabel("Hello, Java!", JLabel.CENTER);
        JLabel label2 = new JLabel("Hello, again!", JLabel.CENTER);
        HelloComponent helloComponent = new HelloComponent();

        helloComponent.setPreferredSize(new Dimension(300, 30));
        
        frame.setLayout(new FlowLayout());
        frame.add(helloComponent);
        frame.add(label);
        frame.add(label2);
        frame.pack();
        frame.setSize(300, 300);
        frame.setVisible(true);
    }
}
