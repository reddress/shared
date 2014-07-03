import java.awt.*;
import javax.swing.*;

class HelloComponent extends JComponent {
    public void paintComponent(Graphics g) {
        g.drawString("Hello Java", 125, 95);
    }
}
