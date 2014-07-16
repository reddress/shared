import java.awt.*;
import java.awt.event.*;
import javax.swing.*;
import javax.swing.event.*;

public class CardexSaver extends JFrame {
    public CardexSaver() {
        super("Cardex Saver");
        createGUI();
    }

    protected void createGUI() {
        setLayout(new FlowLayout());
        
        add(new JLabel("Hello"));

        setLocation(100, 100);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        pack();
        setVisible(true);
    }

    public static void main(String[] args) {
        new CardexSaver();
    }
}
