import java.io.*;
import java.nio.file.*;
import java.nio.charset.*;

import java.util.*;
import java.text.*;

public class ProductData {
    Path filePath;

    String filename;
    String lastModified;
    String vendasAntigo;
    String qtdePorCaixa;
    String extraData;
    
    public ProductData(String filename) {
        this.filename = filename;
        this.filePath = Paths.get(this.filename);
        File f = new File(this.filename);
        if (f.exists() && !f.isDirectory()) {
            load();
        }
        else {
            this.extraData = "\nÚltimo container - ";
        }
    }

    public void load() {
        this.extraData = "";
        try (BufferedReader reader = Files.newBufferedReader(this.filePath, StandardCharsets.UTF_8)) {
                String firstLine = reader.readLine();
                String[] firstValues = firstLine.split(";");
                this.lastModified = firstValues[0];
                this.vendasAntigo = firstValues[1];
                this.qtdePorCaixa = firstValues[2];

                String line = "";
                while ((line = reader.readLine()) != null) {
                    this.extraData += line + "\n";
                }
            }
        catch (IOException e) {
            e.printStackTrace();
        }
    }
            

    public void save(String vendasAntigo, String qtdePorCaixa, String extraData) {
        Date today = new Date();
        SimpleDateFormat sdf = new SimpleDateFormat("dd/MM/yyyy");

        this.lastModified = sdf.format(today);
        this.vendasAntigo = vendasAntigo.equals("") ? "0" : vendasAntigo;
        this.qtdePorCaixa = qtdePorCaixa.equals("") ? "0" : qtdePorCaixa;
        this.extraData = extraData;

        try (BufferedWriter writer = Files.newBufferedWriter(this.filePath, StandardCharsets.UTF_8)) {
                writer.write(this.lastModified + ";" + this.vendasAntigo + ";" + this.qtdePorCaixa + "\n");
                writer.write(this.extraData);
            }
        catch (IOException e) {
            e.printStackTrace();
        }
    }
}
