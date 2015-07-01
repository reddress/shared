import java.awt.*;
import java.awt.event.*;
import javax.swing.*;

public class HelloJava2 {
    public static void main(String[] args) {
        JFrame frame = new JFrame("Hello Java 2");
        JLabel label = new JLabel("A label", JLabel.CENTER);
        HelloComponent2 helloComponent2 = new HelloComponent2("Hello java 2 中國");
        helloComponent2.setPreferredSize(new Dimension(300, 30));

        frame.setLayout(new FlowLayout());
        frame.add(helloComponent2);
        frame.add(label);
        frame.pack();
        
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(300, 300);
        frame.setVisible(true);
    }
}

class HelloComponent2 extends JComponent implements MouseMotionListener {
    String theMessage;
    int messageX = 125;
    int messageY = 15;

    public HelloComponent2(String message) {
        theMessage = message;
        addMouseMotionListener(this);
    }

    public void paintComponent(Graphics g) {
        g.drawString(theMessage, messageX, messageY);
    }

    private void updateLocation(MouseEvent e) {
        messageX = e.getX();
        messageY = e.getY();
        repaint();
    }
    
    public void mouseDragged(MouseEvent e) {
        updateLocation(e);
    }
    
    public void mouseMoved(MouseEvent e) {
        theMessage = String.valueOf(e.getX());
        repaint();
    }
}
