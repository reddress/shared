import java.awt.*;
import java.awt.event.*;
import javax.swing.*;

public class HelloJava3 {
    public static void main(String[] args) {
        JFrame frame = new JFrame("Hello Java 3");
        frame.add(new HelloComponent3("Hellocomponent3"));
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(300, 300);
        frame.setVisible(true);
    }
}

class HelloComponent3 extends JComponent
    implements MouseMotionListener, ActionListener {
    String theMessage;
    int messageX = 125;
    int messageY = 95;

    JButton theButton;

    int colorIndex;
    static Color[] someColors = {
        Color.red, Color.green, Color.BLUE, Color.MAGENTA
    };

    public HelloComponent3(String message) {
        theMessage = message;
        theButton = new JButton("Change color");
        setLayout(new FlowLayout());

        theButton.add(new JButton("buttonception"));
        
        add(theButton);
        theButton.addActionListener(this);
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

    public void actionPerformed(ActionEvent e) {
        if (e.getSource() == theButton) {
            changeColor();
        }
    }

    synchronized private void changeColor() {
        if (++colorIndex == someColors.length) {
            colorIndex = 0;
        }
        setForeground(currentColor());
        repaint();
    }

    synchronized private Color currentColor() {
        return someColors[colorIndex];
    }
    
    public void mouseMoved(MouseEvent e) {
        theMessage = String.valueOf(e.getX());
        repaint();
    }
}
