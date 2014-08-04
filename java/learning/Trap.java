public class Trap<T> {
    T trapped;

    public void snare(T trapped) {
        this.trapped = trapped;
    }

    public T release() {
        return trapped;
    }

}

