import static myutil.Convenience.print;

class Safe {
    private int code;
    private String contents;
    
    public Safe(int code, String contents) {
        this.code = code;
        this.contents = contents;
    }

    public static Safe makeStandardSafe(int code) {
        // return new Safe(code, "Nothing secret");
        return new FancySafe();
    }

    public String getSecret(int code) {
        if (this.code == code) {
            return this.contents;
        }
        else {
            return "not the right code";
        }
    }
}

class FancySafe extends Safe {
    public FancySafe() {
        super(100, "I am fancy");
    }
}

public class StaticFactoryMethod {
    
    public static void main(String[] args) {
        Safe s = Safe.makeStandardSafe(1023);

        print(s.getSecret(100));
    }
}
