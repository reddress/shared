public class ProductIO {
    public static void main (String[] args) {
        ProductData sample = new ProductData("data/120000.txt");
        // sample.save("100", "48", "something\nanother");
        sample.load();
        System.out.println(sample.extraData);
    }
}
