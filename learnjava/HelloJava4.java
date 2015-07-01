import java.awt.*;
import java.awt.event.*;
import javax.swing.*;

public class HelloJava4 {
    public static void main(String[] args) {
        JFrame frame = new JFrame("Hello Java 4");
        frame.add(new HelloComponent4("Hellocomponent4"));
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(300, 300);
        frame.setVisible(true);
    }
}

class HelloComponent4 extends JComponent
    implements MouseMotionListener, ActionListener, Runnable {
    String theMessage;
    int messageX = 125;
    int messageY = 95;

    JButton theButton;

    int colorIndex;
    static Color[] someColors = {
        Color.red, Color.green, Color.BLUE, Color.MAGENTA
    };

    boolean blinkState;

    public HelloComponent4(String message) {
        theMessage = message;
        theButton = new JButton("Change color");
        setLayout(new FlowLayout());

        theButton.add(new JButton("buttonception"));
        
        add(theButton);
        theButton.addActionListener(this);
        addMouseMotionListener(this);
        Thread t = new Thread(this);
        t.start();
    }

    public void paintComponent(Graphics g) {
        g.setColor(blinkState ? getBackground() : currentColor());
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

    public void run() {
        try {
            while(true) {
                blinkState = !blinkState;
                repaint();
                Thread.sleep(500);
            }
        } catch(InterruptedException ie) {

        }
    }   
}
