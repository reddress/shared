/**
 * javac -cp .;../jars/jOpenDocument-1.3.jar ReadChegando.java
 * java -cp .;../jars/jOpenDocument-1.3.jar ReadChegando
 */

class ReadChegando {
    public static void main (String[] args) {
        Chegando chegando = new Chegando("D:/Pontual/tmp/CHEGANDO_COPY.ods");
        System.out.println(Integer.parseInt(chegando.readCell("D5")) * 3000);
        System.out.println(chegando.getChegando("141825p"));
    }
}
