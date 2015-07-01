class CreateMultiplier {
    public static void main(String[] args) {
        Multiplier three = new Multiplier(3);
        Multiplier five = new Multiplier(5);

        System.out.println(three.multiply(9));
        System.out.println(five.multiply(9));
    }
}
