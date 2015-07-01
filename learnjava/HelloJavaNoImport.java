public class HelloJavaNoImport {
    public static void main(String[] args) {
        javax.swing.JFrame frame = new javax.swing.JFrame("Hello Java window title");
        javax.swing.JLabel label = new javax.swing.JLabel("Hello, Java!", javax.swing.JLabel.CENTER);
        frame.add(label);
        frame.setSize(300, 300);
        frame.setVisible(true);
    }
}
