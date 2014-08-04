import static myutil.Convenience.print;

import javax.script.ScriptEngineManager;
import javax.script.ScriptEngine;
import javax.script.ScriptException;

public class MyScript {
    static ScriptEngineManager mgr = new ScriptEngineManager();
    static ScriptEngine engine = mgr.getEngineByName("Scheme");
    
    public static void main(String[] args) {
        String theScript = "9";
        try {
            print(engine.eval(theScript));
        }
        catch (ScriptException se) {
            System.err.println(se);
        }
    }
}
