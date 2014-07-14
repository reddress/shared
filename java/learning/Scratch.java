import static myutil.Convenience.print;

class Animal {
    float weight;
    Animal(float weight) {
        this.weight = weight;
    }

    float getWeight() {
        return this.weight;
    }
    
    void eat() {
        print("OM NOM NOM");
    }
}

class Mammal extends Animal {
    int heartRate;

    Mammal(float weight) {
        super(weight);
    }

    void breathe() {
        print("breathing...");
    }
}

class Cat extends Mammal {
    Cat(float weight) {
        super(weight);
    }
    
    boolean longHair;
    void purr() {
        print("Purrrrrrrrrr");
    }
}

public class Scratch {
    public static void main(String[] args) {
        Cat simon = new Cat(92.1f);
        // Animal creature = new Animal(9.2);
        Animal creature = simon;

        simon.purr();
        print(creature.getWeight());
    }
}
