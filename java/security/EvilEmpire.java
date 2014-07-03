import java.net.*;

public class EvilEmpire {
    public static void main(String[] args) throws Exception {
        try {
            Socket s = new Socket("207.46.131.13", 80);
            System.out.println("Connected!");
        } catch (SecurityException e) {
            System.out.println("SecurityException: Could not connect");
        }
    }
}
