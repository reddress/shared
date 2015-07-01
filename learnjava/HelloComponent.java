import javax.swing.*;
import java.awt.*;

class HelloComponent extends JComponent {
    public void paintComponent(Graphics g) {
        g.drawString("HelloComponent, Java!", 10, 25);
    }
}
