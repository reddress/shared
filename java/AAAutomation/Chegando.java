import java.io.*;
import java.util.HashMap;
import org.jopendocument.dom.*;
import org.jopendocument.dom.spreadsheet.*;

public class Chegando {
    Sheet sheet = null;
    HashMap<String, String> chegaPorCodigo = new HashMap<String, String>();
    
    public Chegando (String path) throws IOException {
//        try {
            File file = new File(path);
            this.sheet = SpreadSheet.createFromFile(file).getSheet(0);

            for (int row = 2; row <= lastRow(); row++) {
                String codigo = readCell("A" + String.valueOf(row));
                if (!chegaPorCodigo.containsKey(codigo)) {
                    chegaPorCodigo.put(codigo, formatChegando(row));
                } else {
                    chegaPorCodigo.put(codigo, chegaPorCodigo.get(codigo) +
                                       formatChegando(row));
                }
            }   
//        } catch (IOException e) {
//            System.err.println("Error reading spreadsheet file.");
//        }
        // chegaPorCodigo.put("123456", "10000");
    }

    protected String readCell(String cellReference) {
        return this.sheet.getImmutableCellAt(cellReference).getTextValue();
    }

    private int lastRow() {
        return sheet.getRowCount();
    }

    private String formatChegando(int row) {
        return String.format("%,d", Integer.parseInt(readCell("D" + String.valueOf(row)))).replace(",", ".") + " (" + readCell("C" + String.valueOf(row)) + ") ";
    }

    public String getChegando(String codigo) {
        String chegandoData = "";
        try {
            chegandoData = chegaPorCodigo.get(codigo.toUpperCase());
        }
        catch (Exception e) {
            chegandoData = "";
        }
        return chegandoData;
    }
}
