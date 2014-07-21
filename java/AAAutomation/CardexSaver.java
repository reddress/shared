import java.awt.*;
import java.awt.event.*;
import javax.swing.*;
import javax.swing.event.*;

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

        /*
        int codigoSectionHeight = 92;
        Dimension outerDimension = new Dimension(262, outerHeight);
        Container outerBox = Box.createVerticalBox();
//        outerBox.setPreferredSize(outerDimension);

        codigoListModel.addElement("Abra uma lista");
        
Container       codigoContainer = Box.createHorizontalBox();
        codigoContainer.setMaximumSize(new Dimension(262, codigoSectionHeight));
        
        JScrollPane codigoScrollPane = new JScrollPane();
        codigoScrollPane.setMaximumSize(new Dimension(105, codigoSectionHeight));
        codigoScrollPane.setViewportView(codigoList);
        codigoContainer.add(codigoScrollPane);
       
        Container codigoManagerBox = Box.createVerticalBox();
        //        codigoManagerBox.setPreferredSize(new Dimension(87, 52));
        codigoManagerBox.addContainerListener(listener);

        
        codigoManagerBox.add(new JButton("Adic. letras"));
        codigoManagerBox.add(new JButton("Adic. codigo"));
        codigoManagerBox.add(new JButton("Remover"));
        codigoManagerBox.add(new JLabel("Atualizado"));

        codigoContainer.add(codigoManagerBox);

        outerBox.add(codigoContainer);

        Container loadCardexBox = Box.createHorizontalBox();
        loadCardexBox.addContainerListener(listener);

//        loadCardexBox.add(new JLabel("Vendas: "));
        loadCardexBox.add(new JButton("Antigo"));
        loadCardexBox.add(new JButton("Atual"));
        loadCardexBox.add(new JLabel("modificado"));

        outerBox.add(loadCardexBox);

        outerBox.add(new JScrollPane(new JTextArea(5, 5)));
        outerBox.add(new JButton("Copiar para clipboard"));

//        add(outerBox, BorderLayout.CENTER);
*/
        setLayout(new GridBagLayout());
        constraints.weightx = 1.0;
        constraints.weighty = 1.0;
        constraints.fill = GridBagConstraints.BOTH;
        int x, y;
        int curRow = 0;

        codigoListModel.addElement("Abra uma lista");
        JScrollPane codigoScrollPane = new JScrollPane();
        codigoScrollPane.setViewportView(codigoList);

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
            //codigoListModel.addElement(String.valueOf(codigoContainer.getSize().height));
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

public class CardexSaver extends JFrame {
    public CardexSaver() {
        super("Cardex Saver");
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        // setSize(CardexPanel.outerWidth, CardexPanel.outerHeight);
        // frame.setLocation(0, 432);
        setLocation(0, 200); 

        JMenuBar menuBar = new JMenuBar();
        
        JMenu fileMenu = new JMenu("Arquivo");
        fileMenu.setMnemonic(KeyEvent.VK_A);

        JMenuItem menuItemAbrir = new JMenuItem("Abrir lista", KeyEvent.VK_B);
        fileMenu.add(menuItemAbrir);

        JMenuItem menuItemSalvar = new JMenuItem("Salvar lista", KeyEvent.VK_S);
        fileMenu.add(menuItemSalvar);

        JMenuItem menuItemConfig = new JMenuItem("Configuracao", KeyEvent.VK_C);
        fileMenu.add(menuItemConfig);
        menuBar.add(fileMenu);
        setJMenuBar(menuBar);
        CardexPanel cardexPanel = new CardexPanel();
        add(cardexPanel, BorderLayout.CENTER);
        pack();
        setAlwaysOnTop(true);
    }
    
    public static void main(String[] args) {
        new CardexSaver().setVisible(true);
    }
}
