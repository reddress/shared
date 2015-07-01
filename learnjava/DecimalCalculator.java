class DecimalCalculator extends IntegerCalculator {
    double sum = 2.3;

    public static void printPi() {
        System.out.println("3.14");
    }
    
    @Override
    public void boot() {
        System.out.println("This is DecimalCalculator");
    }
}
