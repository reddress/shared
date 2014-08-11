import java.io.*;
import java.nio.file.*;
import java.nio.charset.*;

import java.util.*;
import java.text.*;

public class ProductData {
    Path filePath;

    String filename;
    String lastModified;
    String estoque;
    String reservado;
    String vendasAntigo;
    String vendasAtual;
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
            this.lastModified = "";
            this.estoque = "0";
            this.reservado = "0";
            this.vendasAntigo = "0";
            this.vendasAtual = "0";
            this.qtdePorCaixa = "0";
            this.extraData = "\nÚltimo container - \n";
        }
    }

    public void load() {
        this.extraData = "";
        try (BufferedReader reader = Files.newBufferedReader(this.filePath, StandardCharsets.UTF_8)) {
                String firstLine = reader.readLine();
                String[] firstValues = firstLine.split(";");
                this.lastModified = firstValues[0];
                this.estoque = firstValues[1];
                this.reservado = firstValues[2];
                this.vendasAntigo = firstValues[3];
                this.vendasAtual = firstValues[4];
                this.qtdePorCaixa = firstValues[5];

                String line = "";
                while ((line = reader.readLine()) != null) {
                    this.extraData += line + "\n";
                }
            }
        catch (IOException e) {
            e.printStackTrace();
        }
    }
            

    public void save(String estoque, String reservado, String vendasAntigo, String vendasAtual, String qtdePorCaixa, String extraData) {
        Date today = new Date();
        SimpleDateFormat sdf = new SimpleDateFormat("dd/MM/yyyy");

        this.lastModified = sdf.format(today);
        this.estoque = estoque.equals("") ? "0" : estoque;
        this.reservado = reservado.equals("") ? "0" : reservado;
        this.vendasAntigo = vendasAntigo.equals("") ? "0" : vendasAntigo;
        this.vendasAtual = vendasAtual.equals("") ? "0" : vendasAtual;
        this.qtdePorCaixa = qtdePorCaixa.equals("") ? "0" : qtdePorCaixa;
        this.extraData = extraData;

        try (BufferedWriter writer = Files.newBufferedWriter(this.filePath, StandardCharsets.UTF_8)) {
                writer.write(this.lastModified + ";" +
                             this.estoque + ";" +
                             this.reservado + ";" +
                             this.vendasAntigo + ";" +
                             this.vendasAtual + ";" +
                             this.qtdePorCaixa + "\n");
                writer.write(this.extraData);
            }
        catch (IOException e) {
            e.printStackTrace();
        }
    }
}
