public class ReferenceCopy {
    public static void main(String[] args) {
        Foo myFoo = new Foo();
        myFoo.setValue(10);

        Foo anotherFoo = myFoo;
        anotherFoo.setValue(20);

        System.out.println(myFoo.getValue());
    }
}

class Foo {
    int myValue;

    public void setValue(int v) {
        myValue = v;
    }

    public int getValue() {
        return myValue;
    }
}
