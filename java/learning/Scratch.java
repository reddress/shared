import static myutil.Convenience.print;

class Animal {
    float weight;
    String type;
    Animal(float weight) {
        this.weight = weight;
        this.type = "Animal";
    }

    float getWeight() {
        return this.weight;
    }
    
    void eat() {
        print("OM NOM NOM");
    }

    void sleep() {
        print("catch some zzz");
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
    String type;
    Cat(float weight) {
        super(weight);
        this.type = "Cat";
    }
    
    boolean longHair;
    void purr() {
        print("Purrrrrrrrrr");
    }
    @Override void sleep() {
        print("taking a catnap");
    }
}

public class Scratch {
    public static void main(String[] args) {
        Cat simon = new Cat(92.1f);
        // Animal creature = new Animal(9.2);
        Animal creature = simon;

        simon.purr();
        print(creature.getWeight());

        creature.sleep();
        print(creature.type);
        String commaSeparated = "eggs, ham, toast";
        String[] foods = commaSeparated.split(",");
        for (String food : foods) {
            print("(" + food + ")");
        }

        String s = "giraffe";
        for (int i = 0; i < 10; i++) {
            print(s.length() + " " + String.valueOf(i) + " " + s.substring(0, i));
        }
    }
}
