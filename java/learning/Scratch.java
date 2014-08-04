import static myutil.Convenience.print;

import java.util.*;

public class Scratch {
    public static void main(String[] args) {
        Trap<Mouse> mouseTrap = new Trap<Mouse>();
        mouseTrap.snare(new Mouse());
        print(mouseTrap.release().getName());

        Bear barney = new Bear();
        Bear brown = new Bear();

        barney.changeName("Barney");
        print(brown.greeting());

        Trap<Bear> bearTrap = new Trap<>();
        bearTrap.snare(barney);
        print(bearTrap.release().greeting());

        Trap<Mouse> mouseTrap2 = makeTrap();
        mouseTrap2.snare(new Mouse());
        print(mouseTrap2.release());
    }
    public static <T> Trap<T> makeTrap() {
        return new Trap<T>();
    }
}
