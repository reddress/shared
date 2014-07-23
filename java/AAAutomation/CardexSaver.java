// Look at FIXME and XXXX

import java.awt.*;
import java.awt.event.*;
import javax.swing.*;
import javax.swing.event.*;
import javax.swing.filechooser.*;
import javax.swing.table.*;

import java.io.*;
import java.nio.file.*;
import java.nio.charset.*;

import java.util.*;

import org.jopendocument.dom.*;
import org.jopendocument.dom.spreadsheet.*;

import static myutil.Convenience.print;

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

class CardexPanel extends JPanel implements ActionListener {
    static int outerWidth = 268;
    static int outerHeight = 292;

    GridBagConstraints constraints = new GridBagConstraints();
    
    DefaultListModel<String> codigoListModel = new DefaultListModel<String>();
    JList<String> codigoList = new JList<String>(codigoListModel);

    JLabel lastModified;
    
    JFrame dialogFrame;

    Robot bot;
    Keyboard kb;

    JTextField jaPedido;
    JTextField vendasAntigo;
    JTextField vendasAtual;
    JTextField qtdePorCaixa;

    JTextArea infoTextArea = new JTextArea();
    JScrollPane infoScrollPane;
    
    // FIXME
    final String chegandoPath = "D:/Pontual/tmp/CHEGANDO_COPY2.ods";
    Chegando chegando;
    
    public CardexPanel() {
        ContainerListener listener = new ContainerAdapter() {
                public void componentAdded(ContainerEvent e) {
                    Component comp = e.getChild();
                    if (comp instanceof JButton) {
                        ((JButton)comp).addActionListener(CardexPanel.this);
                    }
                }
            };
        addContainerListener(listener);

        dialogFrame = new JFrame();
        dialogFrame.setAlwaysOnTop(true);
        dialogFrame.setLocation(500, 400);
        dialogFrame.setUndecorated(true);
        dialogFrame.setVisible(true);
        
        setLayout(new GridBagLayout());
        constraints.weightx = 1.0;
        constraints.weighty = 1.0;
        constraints.fill = GridBagConstraints.BOTH;
        int x, y;
        int curRow = 0;

        JScrollPane codigoScrollPane = new JScrollPane();
        codigoScrollPane.setViewportView(codigoList);
        codigoScrollPane.setPreferredSize(new Dimension(100, 100));

        rowSpan(5);
        addGB(codigoScrollPane, x = 0, y = curRow);
        
        rowSpan(1);
        colSpan(2);
        addGB(new JButton("Adicionar letras"), x = 1, y = 0);
        addGB(new JButton("Adicionar código"), x = 1, y = 1);
        addGB(new JButton("Remover código"), x = 1, y = 2);
        addGB(new JButton("Pular"), x = 1, y = 3);
        addGB(new JButton("Próximo"), x = 1, y = 4);
        curRow += 5;
            
        rowSpan(1);
        colSpan(1);
        addGB(new JLabel("Abrir Cardex"), x = 0, y = curRow);
        addGB(new JLabel("Atualizado"), x = 2, y = curRow);
        curRow += 1;

        lastModified = new JLabel();
        addGB(new JButton("Antigo"), x = 0, y = curRow);
        addGB(new JButton("Atual"), x = 1, y = curRow);
        addGB(lastModified, x = 2, y = curRow);
        curRow += 1;

        addGB(new JLabel("Já pedido"), x = 0, y = curRow);
        curRow += 1;
        
        colSpan(3);
        jaPedido = new JTextField();
        addGB(jaPedido, x = 0, y = curRow);
        curRow += 1;

        colSpan(1);
        addGB(new JLabel("Vendas antigo"), x = 0, y = curRow);
        addGB(new JLabel("Vendas atual"), x = 1, y = curRow);
        addGB(new JLabel("Qtde por caixa"), x = 2, y = curRow);
        curRow += 1;

        vendasAntigo = new JTextField();
        vendasAtual = new JTextField();
        qtdePorCaixa = new JTextField();
        addGB(vendasAntigo, x = 0, y = curRow);
        addGB(vendasAtual, x = 1, y = curRow);
        addGB(qtdePorCaixa, x = 2, y = curRow);
        curRow += 1;

        colSpan(3);
        infoTextArea = new JTextArea();
        infoTextArea.setRows(5);
        infoScrollPane = new JScrollPane();
        infoScrollPane.setViewportView(infoTextArea);
        
        addGB(infoScrollPane, x = 0, y = curRow);
        curRow += 1;

        rowSpan(1);
        colSpan(3);
        addGB(new JButton("Salvar info e copiar para clipboard"), x = 0, y = curRow);
        curRow += 1;
        
        colSpan(1);

        try {
            bot = new Robot();
            kb = new Keyboard(bot);
        }
        catch (Exception e) {
            JOptionPane.showMessageDialog(dialogFrame, "Error instantiating Robot");
        }

        try { 
            chegando = new Chegando(chegandoPath);
            JOptionPane.showMessageDialog(dialogFrame, "Planilha Chegando: " + chegandoPath);
        }
        catch (Exception e) {
            JOptionPane.showMessageDialog(dialogFrame, "Erro carregando Chegando. Verifique ConfiguracaoCardex.txt");
            // exit application
            
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
            codigoListModel.addElement(codigo);
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
                    codigoListModel.addElement(cellContents);
                }
            }
        }
        catch (Exception e) {
            System.err.println("Error opening spreadsheet to set codigo list");
        }
    }

    public void saveCodigoList(String destination) {

        /* 
        Path codigoListFile = Paths.get(destination);
        // OpenOption[] options = { StandardOpenOption.CREATE_NEW, StandardOpenOption.WRITE, StandardOpenOption.TRUNCATE_EXISTING };
        try (BufferedWriter writer = Files.newBufferedWriter(codigoListFile, StandardCharsets.UTF_8)) {
                Enumeration<String> codigoEnum = codigoListModel.elements();
                ArrayList<String> codigoList = new ArrayList<String>();

                while (codigoEnum.hasMoreElements()) {
                    codigoList.add(codigoEnum.nextElement());
                }
                
                for (String codigo : codigoList) {
                    writer.write(codigo + "\n");
                }
            }
        catch (Exception e) {
            e.printStackTrace();
        }
        */

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
            jaPedido.setText(chegando.getChegando(codigoList.getSelectedValue()));
            return true;
        }
        else {
            return false;
        }
    }

    public void openCardex() {
        // click on Produto bar, Imprimir icon, and Cardex button
        print("activate robot for " + codigoList.getSelectedValue());
        botOpenCodigo(codigoList.getSelectedValue());
    }

    public void proximo() {
        if (advanceCodigo()) {
            openCardex();
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
        }
    }

    public void addCodigo(String codigoToAdd) {
        if (codigoToAdd != null && codigoToAdd.length() > 5) {
            codigoListModel.addElement(codigoToAdd.toUpperCase());
        }
    }

    public void addLetras(int index, String base, String lettersToAdd) {
        if (lettersToAdd != null && lettersToAdd.length() > 1) {
            for (int i = 0; i < lettersToAdd.length(); i++) {
                char c = lettersToAdd.charAt(i);
                String codigoToAdd = base + c;
                addCodigo(codigoToAdd.toUpperCase());
            }
            sortCodigoList();
            codigoListModel.removeElementAt(index);
            
            int newIndex = index + lettersToAdd.length();
            codigoList.setSelectedIndex(newIndex);
            codigoList.ensureIndexIsVisible(newIndex);
        }
    }

    public void click(int x, int y) {
        int mask = InputEvent.BUTTON1_DOWN_MASK;
        bot.mouseMove(x, y);
        bot.mousePress(mask);
        bot.mouseRelease(mask);
    }
    
    public void botOpenCodigo(String codigo) {
        try {

            // FIXME constant
            Coordinates c = new Coordinates(600, 55);
            
            click(c.x, c.y);
            Thread.sleep(200);
            kb.type(codigo + "\n");
        }
        catch (Exception e) {
            System.err.println("Exception when opening codigo");
        }
    }
    
    public void actionPerformed(ActionEvent e) {
        switch (e.getActionCommand()) {
        case "Adicionar letras":
            print("clicked add letras");
            if (codigoList.getSelectedIndex() != -1) {
                String base = codigoList.getSelectedValue();
                int index = codigoList.getSelectedIndex();
                addLetras(index, base, JOptionPane.showInputDialog(dialogFrame, "Tecle 'Espaço' para manter o código numérico.\nPara inserir letras duplas (como GG) use Adicionar código\n" + base));
            }
            else {
                JOptionPane.showMessageDialog(dialogFrame, "Primeiro selecione um código");
            }
            break;
            
        case "Adicionar código":
            print("clicked add codigo");
            int messageType = JOptionPane.INFORMATION_MESSAGE;
            addCodigo(JOptionPane.showInputDialog(dialogFrame, "Digite o código"));
            sortCodigoList();
            
            break;
            
        case "Remover código":
            print("clicked remover codigo");
            deleteCodigo();
            break;
            
        case "Pular":
            print("clicked pular");
            advanceCodigo();
            break;

        case "Próximo":
            print("clicked proximo");
            proximo();
            break;
            
        case "Antigo":
            print("clicked antigo");
            break;
            
        case "Atual":
            print("clicked atual");
            break;
            
        case "Salvar info e copiar para clipboard":
            print("clicked copy clipboard");
            break;
            
        default:
            print("Unknown command -- JButtons");
            break;
        }
    }
}

public class CardexSaver extends JFrame implements ActionListener {
    JFileChooser fc;
    Charset charset;
    CardexPanel cardexPanel;
    
    public CardexSaver() {
        super("Cardex Saver");
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        setLocation(380, 330);

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

        JMenuItem menuItemConfig = new JMenuItem("Configuração", KeyEvent.VK_C);
        menuItemConfig.addActionListener(this);
        fileMenu.add(menuItemConfig);
        menuBar.add(fileMenu);
        setJMenuBar(menuBar);
        cardexPanel = new CardexPanel();

        
        add(cardexPanel, BorderLayout.CENTER);
        pack();
        setResizable(false);
        setAlwaysOnTop(true);

        fc = new JFileChooser();
    }

    public void actionPerformed(ActionEvent e) {
        switch (e.getActionCommand()) {
        case "Nova lista":
            print("selected nova lista");
            cardexPanel.codigoListModel.removeAllElements();
            break;
        case "Abrir lista":
            print("selected abrir lista");
            int returnVal = fc.showOpenDialog(CardexSaver.this);
            
            if (returnVal == JFileChooser.APPROVE_OPTION) {
                File file = fc.getSelectedFile();

                print(file.getAbsolutePath());
                cardexPanel.setCodigoList(file.getAbsolutePath().replace("\\", "\\\\"));
                cardexPanel.sortCodigoList();
            }
            break;
        case "Salvar lista":
            print("selected salvar lista");
            int saveReturnVal = fc.showSaveDialog(CardexSaver.this);
            
            if (saveReturnVal == JFileChooser.APPROVE_OPTION) {
                File file = fc.getSelectedFile();

                print(file.getAbsolutePath());
                cardexPanel.saveCodigoList(file.getAbsolutePath().replace("\\", "\\\\"));
            }
            break;
        case "Configuração":
            print("selected config");
            break;

        case "Adicionar código":
            print("add codigo from frame");
            break;
        default:
            print("Unknown command -- Menu bar");
            break;
        }
    }
    
    public static void main(String[] args) {
        new CardexSaver().setVisible(true);
        print("WARNING USING TEST CHEGANDO_COPY");
    }
}
