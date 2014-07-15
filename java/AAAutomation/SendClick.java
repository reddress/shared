import java.awt.event.*;
import java.awt.Robot;

public class SendClick {
    public static void main(String[] args) {
        Robot bot = null;
        try {
            bot = new Robot();
        } catch (Exception e) {
            System.err.println("Failed instantiating Robot: " + e);
        }

        int mask = InputEvent.BUTTON1_DOWN_MASK;
        bot.mouseMove(205, 55);
        bot.mousePress(mask);
        bot.mouseRelease(mask);
    }
}
