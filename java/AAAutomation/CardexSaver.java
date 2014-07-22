import java.awt.*;
import java.awt.event.*;
import javax.swing.*;
import javax.swing.event.*;
import javax.swing.filechooser.*;

import java.io.*;
import java.nio.file.*;
import java.nio.charset.*;

import java.util.*;

import static myutil.Convenience.print;


class CardexPanel extends JPanel implements ActionListener {
    static int outerWidth = 268;
    static int outerHeight = 292;

    GridBagConstraints constraints = new GridBagConstraints();
    
    DefaultListModel<String> codigoListModel = new DefaultListModel<String>();
    JList<String> codigoList = new JList<String>(codigoListModel);

    public CardexPanel() {
        ContainerListener listener = new ContainerAdapter() {
                public void componentAdded(ContainerEvent e) {
                    Component comp = e.getChild();
                    if (comp instanceof JButton) {
                        ((JButton) comp).addActionListener(CardexPanel.this);
                    }
                }
            };
        addContainerListener(listener);

        setLayout(new GridBagLayout());
        constraints.weightx = 1.0;
        constraints.weighty = 1.0;
        constraints.fill = GridBagConstraints.BOTH;
        int x, y;
        int curRow = 0;

//        codigoListModel.addElement("Abra uma lista");
        JScrollPane codigoScrollPane = new JScrollPane();
        codigoScrollPane.setViewportView(codigoList);
        codigoScrollPane.setPreferredSize(new Dimension(100, 100));

        rowSpan(5);
        addGB(codigoScrollPane, x = 0, y = curRow);
        
        rowSpan(1);
        colSpan(2);
        addGB(new JButton("Adicionar letras"), x = 1, y = 0);
        addGB(new JButton("Adicionar codigo"), x = 1, y = 1);
        addGB(new JButton("Remover codigo"), x = 1, y = 2);
        addGB(new JButton("Pular"), x = 1, y = 3);
        addGB(new JButton("Proximo"), x = 1, y = 4);
        curRow += 5;
            
        rowSpan(1);
        colSpan(1);
        addGB(new JLabel("Abrir Cardex"), x = 0, y = curRow);
        addGB(new JLabel("Atualizado"), x = 2, y = curRow);
        curRow += 1;

        JLabel lastModified = new JLabel();
        addGB(new JButton("Antigo"), x = 0, y = curRow);
        addGB(new JButton("Atual"), x = 1, y = curRow);
        addGB(lastModified, x = 2, y = curRow);
        curRow += 1;

        addGB(new JLabel("Ja pedido"), x = 0, y = curRow);
        curRow += 1;
        
        colSpan(3);
        addGB(new JTextField(), x = 0, y = curRow);
        curRow += 1;

        colSpan(1);
        addGB(new JLabel("Vendas antigo"), x = 0, y = curRow);
        addGB(new JLabel("Vendas atual"), x = 1, y = curRow);
        addGB(new JLabel("Qtde por caixa"), x = 2, y = curRow);
        curRow += 1;

        JTextField vendasAntigo = new JTextField();
        JTextField vendasAtual = new JTextField();
        JTextField qtdePorCaixa = new JTextField();
        addGB(vendasAntigo, x = 0, y = curRow);
        addGB(vendasAtual, x = 1, y = curRow);
        addGB(qtdePorCaixa, x = 2, y = curRow);
        curRow += 1;

        colSpan(3);
        JTextArea infoTextArea = new JTextArea();
        infoTextArea.setRows(5);
        JScrollPane infoScrollPane = new JScrollPane();
        infoScrollPane.setViewportView(infoTextArea);
        
        addGB(infoScrollPane, x = 0, y = curRow);
        curRow += 1;

        rowSpan(1);
        colSpan(3);
        addGB(new JButton("Salvar info e copiar para clipboard"), x = 0, y = curRow);
        curRow += 1;
        
        colSpan(1);
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

    public void actionPerformed(ActionEvent e) {
        switch (e.getActionCommand()) {
        case "Adicionar letras":
            print("clicked add letras");
            break;
            
        case "Adicionar codigo":
            print("clicked add codigo");
            break;
            
        case "Remover codigo":
            print("clicked remover codigo");
            break;
            
        case "Pular":
            print("clicked pular");
            break;

        case "Proximo":
            print("clicked proximo");
            break;
            
        case "Antigo":
            print("clicked antigo");
            codigoListModel.addElement("abcdef");
            break;
            
        case "Atual":
            print("clicked atual");
            codigoListModel.addElement("Atual");
            break;
            
        case "Salvar info e copiar para clipboard":
            print("clicked copy clipboard");
            break;
            
        default:
            print("unassigned function");
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

        ////////////
        // location
        setLocation(400, 200); 

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

        JMenuItem menuItemConfig = new JMenuItem("Configuracao", KeyEvent.VK_C);
        menuItemConfig.addActionListener(this);
        fileMenu.add(menuItemConfig);
        menuBar.add(fileMenu);
        setJMenuBar(menuBar);
        cardexPanel = new CardexPanel();
        add(cardexPanel, BorderLayout.CENTER);
        pack();
        setAlwaysOnTop(true);

        fc = new JFileChooser();
    }

    public void sortCodigoList() {
        Enumeration<String> codigoEnum = cardexPanel.codigoListModel.elements();
        ArrayList<String> codigoList = new ArrayList<String>();

        while (codigoEnum.hasMoreElements()) {
            codigoList.add(codigoEnum.nextElement());
        }
        cardexPanel.codigoListModel.removeAllElements();
        Collections.sort(codigoList);

        for (String codigo : codigoList) {
            cardexPanel.codigoListModel.addElement(codigo);
        }

    }

    public void setCodigoList(String sourcePathString) {
        cardexPanel.codigoListModel.removeAllElements();

        print("Newer style file load");
        
        Charset charset = Charset.forName("US-ASCII");
        Path configFile = Paths.get(sourcePathString);
        try (BufferedReader reader = Files.newBufferedReader(configFile, charset)) {
                String line = null;
                while ((line = reader.readLine()) != null) {
                    cardexPanel.codigoListModel.addElement(line);
                }
            }
        catch (IOException x) {
            System.err.println("IOException when setting codigo list");
        }
    }

    public void actionPerformed(ActionEvent e) {
        switch (e.getActionCommand()) {
        case "Nova lista":
            cardexPanel.codigoListModel.removeAllElements();
            break;
        case "Abrir lista":
            print("selected abrir lista");
            int returnVal = fc.showOpenDialog(CardexSaver.this);
            
            if (returnVal == JFileChooser.APPROVE_OPTION) {
                File file = fc.getSelectedFile();

                print(file.getAbsolutePath());
                setCodigoList(file.getAbsolutePath().replace("\\", "\\\\"));
                sortCodigoList();
            }
            break;
        case "Salvar lista":
            print("selected salvar lista");
            break;
        case "Configuracao":
            print("selected config");
            break;
        default:
            print("Unknown command");
            break;
        }
    }
    
    public static void main(String[] args) {
        new CardexSaver().setVisible(true);
    }
}
