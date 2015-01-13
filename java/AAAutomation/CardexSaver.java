// Look at FIXME

// WHEN REARRANGING BUTTONS IN MARCH, MOVE ALL "VENDAS 2014" TO
// "VENDAS ANTIGO" AND DISCARD VENDAS 2013 DATA

import java.awt.*;
import java.awt.event.*;
import java.awt.datatransfer.*;

import javax.swing.*;
import javax.swing.event.*;
import javax.swing.filechooser.*;
import javax.swing.table.*;

import java.io.*;
import java.nio.file.*;
import java.nio.charset.*;

import java.util.*;
import java.text.*;

import org.jopendocument.dom.*;
import org.jopendocument.dom.spreadsheet.*;

import static myutil.Convenience.print;

class CardexPanel extends JPanel implements ActionListener {
    final String configurationFile = "ConfiguracaoCardex.txt";
    Properties config;    
    
    Chegando chegando;

    int todayMonth;
    int todayYear;
    
    GridBagConstraints constraints = new GridBagConstraints();
    
    DefaultListModel<String> codigoListModel = new DefaultListModel<String>();
    JList<String> codigoList = new JList<String>(codigoListModel);

    int codigoListSize;
    
    JLabel lastModified;
    JLabel estoqueCaixas;
    
    JFrame dialogFrame;

    Robot bot;
    Keyboard kb;

    JLabel progress;

    JTextField estoque;
    JTextField reservado;
    int pecasTotais;

    JTextField jaPedido;
    JTextField vendasAntigo;
    JTextField vendasAtual;
    JTextField qtdePorCaixa;

    JTextArea infoTextArea = new JTextArea();
    JScrollPane infoScrollPane;
        
    public CardexPanel() throws IOException {
        ContainerListener listener = new ContainerAdapter() {
                public void componentAdded(ContainerEvent e) {
                    Component comp = e.getChild();
                    if (comp instanceof JButton) {
                        ((JButton)comp).addActionListener(CardexPanel.this);
                    }
                }
            };
        addContainerListener(listener);

        // load config properties
        InputStream inputStream = null;
        config = new Properties();
        
        try {
            inputStream = new FileInputStream(configurationFile);
            config.load(inputStream);
        }
        catch (IOException e) {
            e.printStackTrace();
        }
        finally {
            if (inputStream != null) {
                try {
                    inputStream.close();
                }
                catch (Exception e) {
                    e.printStackTrace();
                }
            }
        }
        
        Date today = new Date();
        Calendar cal = Calendar.getInstance();
        cal.setTime(today);
        todayMonth = cal.get(Calendar.MONTH);
        todayYear = cal.get(Calendar.YEAR);
            
        dialogFrame = new JFrame();
        dialogFrame.setAlwaysOnTop(true);
        dialogFrame.setUndecorated(true);
        dialogFrame.setVisible(true);
        
        Coordinates dialogFrameCoords = new Coordinates(config.getProperty("DialogLocation"));
        dialogFrame.setLocation(dialogFrameCoords.x, dialogFrameCoords.y);

        setLayout(new GridBagLayout());
        constraints.weightx = 1.0;
        constraints.weighty = 1.0;
        constraints.fill = GridBagConstraints.BOTH;
        int x, y;
        int curRow = 0;

        JScrollPane codigoScrollPane = new JScrollPane();
        codigoScrollPane.setViewportView(codigoList);
        codigoScrollPane.setPreferredSize(new Dimension(100, 70));

        rowSpan(5);
        addGB(codigoScrollPane, x = 0, y = curRow);
        
        rowSpan(1);
        colSpan(2);
        addGB(new JButton("Adicionar letras"), x = 1, y = 0);
        addGB(new JButton("Adicionar código"), x = 1, y = 1);
        addGB(new JButton("Remover código"), x = 1, y = 2);
        addGB(new JButton("Próximo"), x = 1, y = 3);
        addGB(new JButton("Abrir código"), x = 1, y = 4);
        curRow += 5;
            
        rowSpan(1);
        colSpan(1);
        // addGB(new JLabel("Abrir Cardex"), x = 0, y = curRow);
        // addGB(new JLabel("Atualizado"), x = 2, y = curRow);
        // curRow += 1;

        addGB(new JButton("2013"), x = 0, y = curRow);
        addGB(new JButton("2014"), x = 1, y = curRow);
        // addGB(lastModified, x = 2, y = curRow);
        // addGB(new JButton("2008"), x = 2, y = curRow);
        addGB(new JButton("Atual"), x = 2, y = curRow);
        curRow += 1;

        colSpan(2);
        addGB(new JLabel("Já pedido"), x = 0, y = curRow);
        colSpan(1);
        addGB(new JLabel("Atualizado"), x = 2, y = curRow);
        curRow += 1;
        
        colSpan(2);
        jaPedido = new JTextField();
        addGB(jaPedido, x = 0, y = curRow);
        colSpan(1);
        lastModified = new JLabel("");
        addGB(lastModified, x = 2, y = curRow);        
        curRow += 1;

        colSpan(1);
        estoqueCaixas = new JLabel("Est.");
        addGB(estoqueCaixas, x = 0, y = curRow);
        addGB(new JLabel("Reservado"), x = 1, y = curRow);
        progress = new JLabel("");
        addGB(progress, x = 2, y = curRow);
        curRow += 1;

        rowSpan(1);
        colSpan(1);
        estoque = new JTextField();
        reservado = new JTextField();
        estoque.addFocusListener(new FocusListener() {
                @Override public void focusLost(final FocusEvent fe) {
                    // LOST FOCUS ACTION
                    countAndSetCaixas();
                }
                @Override public void focusGained(final FocusEvent fe) {
                    estoque.selectAll();
                }
            });
        reservado.addFocusListener(new FocusListener() {
                @Override public void focusLost(final FocusEvent fe) {
                    countAndSetCaixas();
                }
                @Override public void focusGained(final FocusEvent fe) {
                    reservado.selectAll();
                }
            });

        addGB(estoque, x = 0, y = curRow);
        addGB(reservado, x = 1, y = curRow);
        addGB(new JButton("Calcular"), x = 2, y = curRow);
        rowSpan(1);
        curRow += 1;

        colSpan(1);
        addGB(new JLabel("Vendas 2013"), x = 0, y = curRow);
        addGB(new JLabel("Vendas 2014"), x = 1, y = curRow);
        addGB(new JLabel("Qtde por caixa"), x = 2, y = curRow);
        curRow += 1;

        vendasAntigo = new JTextField();
        vendasAtual = new JTextField();
        qtdePorCaixa = new JTextField();
        vendasAntigo.addFocusListener(new FocusListener() {
                @Override public void focusLost(final FocusEvent fe) { }
                @Override public void focusGained(final FocusEvent fe) {
                    vendasAntigo.selectAll();
                }
            });
        vendasAtual.addFocusListener(new FocusListener() {
                @Override public void focusLost(final FocusEvent fe) { }
                @Override public void focusGained(final FocusEvent fe) {
                    vendasAtual.selectAll();
                }
            });
        qtdePorCaixa.addFocusListener(new FocusListener() {
                @Override public void focusLost(final FocusEvent fe) {
                    countAndSetCaixas();
                }
                @Override public void focusGained(final FocusEvent fe) {
                    qtdePorCaixa.selectAll();
                }
            });
        addGB(vendasAntigo, x = 0, y = curRow);
        addGB(vendasAtual, x = 1, y = curRow);
        addGB(qtdePorCaixa, x = 2, y = curRow);
        curRow += 1;

        colSpan(3);
        infoTextArea = new JTextArea();
        infoTextArea.setRows(4);
        infoScrollPane = new JScrollPane();
        infoScrollPane.setViewportView(infoTextArea);
        infoScrollPane.setPreferredSize(new Dimension(100, 100));
        
        addGB(infoScrollPane, x = 0, y = curRow);
        curRow += 1;

        rowSpan(1);
        colSpan(3);
        addGB(new JButton("Salvar info e copiar para clipboard"), x = 0, y = curRow);
        curRow += 1;
        
        colSpan(1);

        codigoList.addListSelectionListener(new ListSelectionListener() {
                public void valueChanged(ListSelectionEvent e) {
                    loadSavedData();
                }
            });
        codigoList.addMouseListener(new MouseAdapter() {
                public void mouseClicked(MouseEvent me) {
                    if (me.getClickCount() == 2) {
                        botOpenCodigo(codigoList.getSelectedValue());
                        Coordinates guiProximoCoords = new Coordinates(config.getProperty("GUIProximo"));
                        bot.mouseMove(guiProximoCoords.x, guiProximoCoords.y);
                        // Coordinates guiProximoCoords = new Coordinates(config.getProperty("GUIProximo"));
                        // bot.mouseMove(guiProximoCoords.x, guiProximoCoords.y);
                        // Coordinates guiPularCoords = new Coordinates(config.getProperty("GUIPular"));
                        // bot.mouseMove(guiPularCoords.x, guiPularCoords.y);
                    }
                }
            });
        
        try {
            bot = new Robot();
            kb = new Keyboard(bot);
        }
        catch (Exception e) {
            JOptionPane.showMessageDialog(dialogFrame, "Error instantiating Robot");
        }

        try { 
            chegando = new Chegando(config.getProperty("Chegando"));
            JOptionPane.showMessageDialog(dialogFrame, "Planilha Chegando: " + config.getProperty("Chegando") + "\nPegou lista do Sr. Yeh?");
        }
        catch (Exception e) {
            e.printStackTrace();
            JOptionPane.showMessageDialog(dialogFrame, "Erro carregando Chegando. Verifique ConfiguracaoCardex.txt");
            // exit application
            throw new IOException();
        }
    }

    void countAndSetCaixas() {
        if (Integer.parseInt(qtdePorCaixa.getText()) == 0) {
            estoqueCaixas.setText("Est. ? cx");
        }
        else {
            estoqueCaixas.setText("Est. " + String.valueOf(
                                      (Integer.parseInt(estoque.getText()) +
                                       Integer.parseInt(reservado.getText())) /
                                      (Integer.parseInt(qtdePorCaixa.getText()))) + " cx");
        }
    }

    void rowSpan(int rows) {
        constraints.gridheight = rows;
    }

    void colSpan(int cols) {
        constraints.gridwidth = cols;
    }
    
    void addGB(Component component, int x, int y) {
        constraints.gridx = x;
        constraints.gridy = y;
        add(component, constraints);
    }

    public void sortCodigoList() {
        Enumeration<String> codigoEnum = codigoListModel.elements();
        ArrayList<String> codigoList = new ArrayList<String>();

        while (codigoEnum.hasMoreElements()) {
            codigoList.add(codigoEnum.nextElement());
        }
        codigoListModel.removeAllElements();
        Collections.sort(codigoList);

        for (String codigo : codigoList) {
            //codigoListModel.addElement(codigo);
            addCodigo(codigo);
        }
    }

    public void setCodigoList(String sourcePathString) {
        codigoListModel.removeAllElements();

        /*
          Charset charset = Charset.forName("US-ASCII");
          Path configFile = Paths.get(sourcePathString);
          try (BufferedReader reader = Files.newBufferedReader(configFile, charset)) {
          String line = null;
          while ((line = reader.readLine()) != null) {
          codigoListModel.addElement(line);
          }
          }
          catch (IOException x) {
          System.err.println("IOException when setting codigo list");
          }
        */

        Sheet sheet = null;
        File file = null;
        
        try {
            file = new File(sourcePathString);
            sheet = SpreadSheet.createFromFile(file).getSheet(0);
            for (int row = 1; row <= sheet.getRowCount(); row++) {
                String cellContents = sheet.getImmutableCellAt("A" + row).getTextValue();
                if (!cellContents.equals("codigo")) {
                    addCodigo(cellContents);
                    // codigoListModel.addElement(cellContents);
                }
            }
            codigoListSize = codigoList.getModel().getSize();
            progress.setText("(" + codigoListSize + ")");
        }
        catch (Exception e) {
            System.err.println("Error opening spreadsheet to set codigo list");
        }
    }

    public void saveCodigoList(String destination) {
        Object[][] data = new Object[codigoListModel.getSize()][1];

        for (int i = 0; i < codigoListModel.getSize(); i++) {
            data[i] = new Object[] { codigoListModel.getElementAt(i) };
        }

        String[] columns = new String[] { "codigo" };
        TableModel model = new DefaultTableModel(data, columns);

        try {
            File file = new File(destination);
            SpreadSheet.createEmpty(model).saveAs(file);
            // JOptionPane.showMessageDialog(dialogFrame, "Arquivo salvo: " + destination.replace("\\\\", "\\"));
        }
        catch (Exception e) {
            e.printStackTrace();
            JOptionPane.showMessageDialog(dialogFrame, "Erro: Arquivo está aberto, feche-o e tente de novo.");
        }
    }

    public boolean advanceCodigo() {
        if (!checkEnd()) {
            int nextIndex = codigoList.getSelectedIndex() + 1;
            codigoList.setSelectedIndex(nextIndex);
            codigoList.ensureIndexIsVisible(nextIndex);

            // load from chegando and data file
            loadSavedData();
            // jaPedido.setText(chegando.getChegando(codigoList.getSelectedValue()));
            return true;
        }
        else {
            return false;
        }
    }

    public void loadSavedData() {
        if (codigoList.getSelectedIndex() != -1) {        
            String chegandoValue = chegando.getChegando(codigoList.getSelectedValue());
            if (chegandoValue != null) {
                if (chegandoValue.length() > 25) {
                    chegandoValue = chegandoValue.substring(0, 25) + "*";
                }
            }
            jaPedido.setText(chegandoValue);
            // print(codigoList.getSelectedValue().trim());
            
            ProductData productData = new ProductData("data/" + codigoList.getSelectedValue() + ".txt");
            lastModified.setText(productData.lastModified);
            estoque.setText(productData.estoque);
            reservado.setText(productData.reservado);
            vendasAntigo.setText(productData.vendasAntigo);
            vendasAtual.setText(productData.vendasAtual);
            qtdePorCaixa.setText(productData.qtdePorCaixa);
            infoTextArea.setText(productData.extraData);
            infoTextArea.setCaretPosition(0);
            
            pecasTotais = Integer.parseInt(productData.estoque) +
                Integer.parseInt(productData.reservado);
            // print("LOADED PCS TOTAIS " + pecasTotais);
            progress.setText((1 + codigoList.getSelectedIndex()) + " de " + codigoListSize);

            countAndSetCaixas();
        }
    }
    
    public void openCardex() {
        botOpenCodigo(codigoList.getSelectedValue());
        try {
            click(configCoords("Imprimir"));
            Thread.sleep(200);
            click(configCoords("Cardex"));
            Thread.sleep(300);
        }
        catch (Exception e) {
            System.err.println("Exception in openCardex");
        }
    }
    
    public void openCardexAtual() {
        // click on Produto bar, Imprimir icon, and Cardex button
        //print("activate robot for " + codigoList.getSelectedValue());
        openCardex();

        try {
            click(configCoords("InicialDia"));
            kb.type("01");
            Thread.sleep(100);
            click(configCoords("InicialMes"));
            kb.type("01");
            Thread.sleep(200);
            kb.type("\n");

            Coordinates ultimaPaginaCoords = new Coordinates(config.getProperty("UltimaPagina"));
            bot.mouseMove(ultimaPaginaCoords.x, ultimaPaginaCoords.y);
        }
        catch (Exception e) {
            System.err.println("Error in Cardex Atual");
        }
    }

    public void openCardex2008() {
        // click on Produto bar, Imprimir icon, and Cardex button
        //print("activate robot for " + codigoList.getSelectedValue());
        openCardex();

        try {
            click(configCoords("InicialDia"));
            kb.type("01");
            Thread.sleep(100);
            click(configCoords("InicialMes"));
            kb.type("01");
            Thread.sleep(100);
            click(configCoords("InicialAno"));
            kb.type("2008");
            Thread.sleep(300);
            kb.type("\n");

            Coordinates ultimaPaginaCoords = new Coordinates(config.getProperty("UltimaPagina"));
            bot.mouseMove(ultimaPaginaCoords.x, ultimaPaginaCoords.y);
        }
        catch (Exception e) {
            System.err.println("Error in Cardex Atual");
        }
    }

    public void openCardexAntigo() {
        // click on Produto bar, Imprimir icon, and Cardex button
        openCardex();

        try {
            // click to set 01-01-201X (year before)
            click(configCoords("InicialDia"));
            kb.type("01");
            click(configCoords("InicialMes"));
            kb.type("01");
            click(configCoords("InicialAno"));
            kb.type(String.valueOf(todayYear - 1));
            Thread.sleep(350);
            click(configCoords("FinalFlecha"));
            Thread.sleep(300);
            for (int i = 0; i <= todayMonth; i++) {
                click(configCoords("CalendarioVoltar"));
                Thread.sleep(50);
            }
            Thread.sleep(250);
            click(configCoords("CalendarioDezembro31"));
            
            Coordinates ultimaPaginaCoords = new Coordinates(config.getProperty("UltimaPagina"));
            bot.mouseMove(ultimaPaginaCoords.x, ultimaPaginaCoords.y);
        }
        catch (Exception e) {
            System.err.println("Error in Cardex Antigo");
        }
    }

    public void openCardexAntigoTwoYears() {
        // click on Produto bar, Imprimir icon, and Cardex button
        openCardex();

        try {
            // click to set 01-01-201X (year before)
            click(configCoords("InicialDia"));
            kb.type("01");
            click(configCoords("InicialMes"));
            kb.type("01");
            click(configCoords("InicialAno"));
            kb.type(String.valueOf(todayYear - 2));
            Thread.sleep(350);
            click(configCoords("FinalFlecha"));
            Thread.sleep(300);
            for (int i = 0; i <= (12 + todayMonth); i++) {
                click(configCoords("CalendarioVoltar"));
                Thread.sleep(50);
            }
            Thread.sleep(250);
            click(configCoords("CalendarioDezembro31DoisAnos"));
            
            Coordinates ultimaPaginaCoords = new Coordinates(config.getProperty("UltimaPagina"));
            bot.mouseMove(ultimaPaginaCoords.x, ultimaPaginaCoords.y);
        }
        catch (Exception e) {
            System.err.println("Error in Cardex Antigo Two Years");
        }
    }

    public void proximo() {
        if (advanceCodigo()) {
            try {
                botOpenCodigo(codigoList.getSelectedValue());
                Coordinates guiProximoCoords = new Coordinates(config.getProperty("GUIProximo"));
                bot.mouseMove(guiProximoCoords.x, guiProximoCoords.y);
            }
            catch (Exception e) {
                e.printStackTrace();
            }
        }
    }

    public boolean checkEnd() {
        boolean reachedEnd = codigoList.getSelectedIndex() == codigoListModel.getSize() - 1;
        if (reachedEnd) {
            JOptionPane.showMessageDialog(dialogFrame, "Fim da lista");
        }
        return reachedEnd;
    }

    public void deleteCodigo() {
        int currentIndex = codigoList.getSelectedIndex();
        int newIndex = currentIndex;
        if (currentIndex != -1) {
            codigoListModel.removeElementAt(currentIndex);
            if (currentIndex == codigoListModel.getSize()) {
                newIndex -= 1;
            }
            codigoList.setSelectedIndex(newIndex);
            codigoListSize = codigoList.getModel().getSize();
        }
    }

    public void addCodigo(String codigoToAdd) {
        if (codigoToAdd != null && codigoToAdd.length() > 5 && !codigoListModel.contains(codigoToAdd)) {
            codigoListModel.addElement(codigoToAdd.toUpperCase().trim());
            codigoListSize = codigoList.getModel().getSize();
        }
    }

    public void addLetras(int index, String base, String lettersToAdd) {
        if (lettersToAdd != null && !lettersToAdd.equals("")) {
            codigoListModel.removeElementAt(index);

            if (lettersToAdd != null && lettersToAdd.length() > 0) {
                for (int i = 0; i < lettersToAdd.length(); i++) {
                    char c = lettersToAdd.charAt(i);
                    String codigoToAdd = base + c;
                    addCodigo(codigoToAdd.toUpperCase());
                }
                sortCodigoList();
                
                int newIndex = index + lettersToAdd.length();
                codigoList.setSelectedIndex(newIndex);
                codigoList.ensureIndexIsVisible(newIndex);
            }
        }
        else {
            advanceCodigo();
        }
    }
        
    public void saveProductData() {
        if (codigoList.getSelectedIndex() != -1) {
            String filename = "data/" + codigoList.getSelectedValue() + ".txt"; 
            ProductData productData = new ProductData(filename);
            productData.save(estoque.getText(), reservado.getText(), vendasAntigo.getText(), vendasAtual.getText(), qtdePorCaixa.getText(), infoTextArea.getText());
        }
    }

    public void copyToClipboard() {
        String output = "";
        output += codigoList.getSelectedValue();
        output += ";";
        output += estoque.getText();
        output += ";";
        output += reservado.getText();
        output += ";";
        output += jaPedido.getText().trim().equals("") ? "0" : jaPedido.getText().trim();
        output += ";";
        output += vendasAntigo.getText();
        output += ";";
        output += vendasAtual.getText();
        output += ";";
        output += qtdePorCaixa.getText();
        output += "\n";
        output += infoTextArea.getText();
        
        StringSelection ss = new StringSelection(output);
        Clipboard cb = Toolkit.getDefaultToolkit().getSystemClipboard();
        cb.setContents(ss, null);
    }

    public void click(Coordinates c) {
        int mask = InputEvent.BUTTON1_DOWN_MASK;
        bot.mouseMove(c.x, c.y);
        bot.mousePress(mask);
        bot.mouseRelease(mask);
    }
    
    public void botOpenCodigo(String codigo) {
        try {
            click(configCoords("ProdutoBarra"));
            Thread.sleep(200);
            click(configCoords("BuscaRapida"));
            Thread.sleep(350);
            kb.type(codigo.trim());
            Thread.sleep(200);
            kb.type("\n");
        }
        catch (Exception e) {
            System.err.println("Exception when opening codigo");
        }
    }

    public Coordinates configCoords(String name) {
        return new Coordinates(config.getProperty(name));
    }

    public void clearFields() {
        jaPedido.setText("");
        lastModified.setText("");
        estoque.setText("");
        reservado.setText("");
        vendasAntigo.setText("");
        vendasAtual.setText("");
        qtdePorCaixa.setText("");
        infoTextArea.setText("");
    }
    
    public void actionPerformed(ActionEvent e) {
        switch (e.getActionCommand()) {
        case "Adicionar letras":
            if (codigoList.getSelectedIndex() != -1) {
                try {
                    String base = codigoList.getSelectedValue();
                    int index = codigoList.getSelectedIndex();
                    botOpenCodigo(base);
                    Thread.sleep(550);
                    addLetras(index, base, JOptionPane.showInputDialog(dialogFrame, "Tecle 'Espaço' para manter o código numérico.\nPara inserir letras duplas (como GG) repita esta ação.\n" + base));
                }
                catch (Exception ex) {
                    ex.printStackTrace();
                }
            }
            else {
                JOptionPane.showMessageDialog(dialogFrame, "Primeiro selecione um código");
            }
            break;
            
        case "Adicionar código":
            int messageType = JOptionPane.INFORMATION_MESSAGE;
            addCodigo(JOptionPane.showInputDialog(dialogFrame, "Digite o código"));
            sortCodigoList();
            
            break;
            
        case "Remover código":
            deleteCodigo();
            break;
            
        case "Pular":
            advanceCodigo();
            break;

        case "Próximo":
            // proximo();
            advanceCodigo();
            break;

        case "Abrir código":
            //FIXME
            botOpenCodigo(codigoList.getSelectedValue());
            Coordinates guiProximoCoords = new Coordinates(config.getProperty("GUIProximo"));
            bot.mouseMove(guiProximoCoords.x, guiProximoCoords.y);
            break;

            // case "Antigo":
        case "2014":
            if (codigoList.getSelectedIndex() != -1) {
                openCardexAntigo();
            }
            break;
            
        case "Atual":
            if (codigoList.getSelectedIndex() != -1) {
                openCardexAtual();
            }
            break;

            // case "2008":
        case "2013":
            if (codigoList.getSelectedIndex() != -1) {
                // openCardex2008();
                openCardexAntigoTwoYears();
            }
            break;

        case "Calcular":
            if (codigoList.getSelectedIndex() != -1) {
                // print("CALCULAR");
                int newPecas = Integer.parseInt(estoque.getText()) +
                    Integer.parseInt(reservado.getText());

                if (newPecas < pecasTotais) {
                    // print("NEW PECAS " + newPecas);
                    int difference = pecasTotais - newPecas;
                    int currentVendasAtual = Integer.parseInt(vendasAtual.getText());
                    vendasAtual.setText(String.valueOf(currentVendasAtual + difference));
                    pecasTotais = newPecas;
                }
            }
            break;

        case "Salvar info e copiar para clipboard":
            if (codigoList.getSelectedIndex() != -1) {
                saveProductData();
                copyToClipboard();
            }
            break;
            
        default:
            // print("Unknown command -- JButtons");
            System.err.println("Unknown command -- JButtons");
            break;
        }
    }
}

class Coordinates {
    int x;
    int y;
    Coordinates(int x, int y) {
        this.x = x;
        this.y = y;
    }

    Coordinates(String pair) {
        String[] parts = pair.split(",");
        this.x = Integer.parseInt(parts[0]);
        this.y = Integer.parseInt(parts[1]);
    }
}

public class CardexSaver extends JFrame implements ActionListener { 
    final String configurationFile = "ConfiguracaoCardex.txt";

    JFileChooser fc;
    Charset charset;
    CardexPanel cardexPanel;
    Properties config;
    
    public CardexSaver() throws IOException {
        super("Cardex Saver");
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        // load config properties
        InputStream inputStream = null;
        config = new Properties();
        
        try {
            inputStream = new FileInputStream(configurationFile);
            config.load(inputStream);
        }
        catch (IOException e) {
            e.printStackTrace();
        }
        finally {
            if (inputStream != null) {
                try {
                    inputStream.close();
                }
                catch (Exception e) {
                    e.printStackTrace();
                }
            }
        }

        Coordinates mainCoords = new Coordinates(config.getProperty("MainLocation"));
        setLocation(mainCoords.x, mainCoords.y);

        JMenuBar menuBar = new JMenuBar();
        
        JMenu fileMenu = new JMenu("Arquivo");
        fileMenu.setMnemonic(KeyEvent.VK_A);

        JMenuItem menuItemNovo = new JMenuItem("Nova lista", KeyEvent.VK_N);
        menuItemNovo.addActionListener(this);
        fileMenu.add(menuItemNovo);
        
        JMenuItem menuItemAbrir = new JMenuItem("Abrir lista", KeyEvent.VK_B);
        menuItemAbrir.addActionListener(this);
        fileMenu.add(menuItemAbrir);

        JMenuItem menuItemSalvar = new JMenuItem("Salvar lista", KeyEvent.VK_S);
        menuItemSalvar.addActionListener(this);
        fileMenu.add(menuItemSalvar);

        JMenuItem menuItemSair = new JMenuItem("Sair", KeyEvent.VK_R);
        menuItemSair.addActionListener(this);
        fileMenu.add(menuItemSair);
        
        menuBar.add(fileMenu);
        setJMenuBar(menuBar);

        try {
            cardexPanel = new CardexPanel();
        
            add(cardexPanel, BorderLayout.CENTER);
            pack();
            setResizable(false);
            setAlwaysOnTop(true);
            
            fc = new JFileChooser();
        }
        catch (IOException ioe) {
            throw new IOException();
        }
    }

    public void actionPerformed(ActionEvent e) {
        switch (e.getActionCommand()) {
        case "Nova lista":
            //print("selected nova lista");
            cardexPanel.codigoListModel.removeAllElements();
            cardexPanel.clearFields();
            break;
        case "Abrir lista":
            //print("selected abrir lista");
            int returnVal = fc.showOpenDialog(CardexSaver.this);
            
            if (returnVal == JFileChooser.APPROVE_OPTION) {
                File file = fc.getSelectedFile();

                //print(file.getAbsolutePath());
                cardexPanel.setCodigoList(file.getAbsolutePath().replace("\\", "\\\\"));
                cardexPanel.sortCodigoList();
                cardexPanel.clearFields();
            }
            break;
        case "Salvar lista":
            //print("selected salvar lista");
            int saveReturnVal = fc.showSaveDialog(CardexSaver.this);
            
            if (saveReturnVal == JFileChooser.APPROVE_OPTION) {
                File file = fc.getSelectedFile();

                //print(file.getAbsolutePath());
                cardexPanel.saveCodigoList(file.getAbsolutePath().replace("\\", "\\\\"));
            }
            break;
        case "Sair":
            //print("Selected sair");
            System.exit(0);
            break;
        default:
            // print("Unknown command -- Menu bar");
            System.err.println("Unknown command -- Menu bar");
            break;
        }
    }
    
    public static void main(String[] args) {
        CardexSaver cardexSaver = null;
        try {
            cardexSaver = new CardexSaver();
            cardexSaver.setVisible(true);
        }
        catch (IOException e) {
            e.printStackTrace();
            System.exit(-1);
        }
    }
}
