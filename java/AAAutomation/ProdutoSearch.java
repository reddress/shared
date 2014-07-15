import java.awt.event.*;
import java.awt.Robot;

public class ProdutoSearch {
    public static void main(String[] args) throws InterruptedException {
        Robot bot = null;
        try {
            bot = new Robot();
        } catch (Exception e) {
            System.err.println("Failed instantiating Robot: " + e);
        }

        int mask = InputEvent.BUTTON1_DOWN_MASK;
        bot.mouseMove(600, 55);
        bot.mousePress(mask);
        bot.mouseRelease(mask);

        Keyboard k = new Keyboard(bot);
        Thread.sleep(500);
        k.type(args[0] + "\n");
    }
}
