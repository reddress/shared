import java.awt.*;
import java.awt.event.*;
import javax.swing.*;
import javax.swing.event.*;

import static myutil.Convenience.print;

public class CardexSaver extends JPanel implements ActionListener {
    DefaultListModel<String> codigoListModel = new DefaultListModel<String>();
    JList<String> codigoList = new JList<String>(codigoListModel);
    
    public CardexSaver() {
        ContainerListener listener = new ContainerAdapter() {
                public void componentAdded(ContainerEvent e) {
                    Component comp = e.getChild();
                    if (comp instanceof JButton) {
                        ((JButton) comp).addActionListener(CardexSaver.this);
                    }
                }
            };
        addContainerListener(listener);

        // add JMenuBar;
        
        // setLayout(new FlowLayout());

        Container outerBox = Box.createVerticalBox();

        codigoListModel.addElement("Carregue a lista");

        JScrollPane codigoScrollPane = new JScrollPane();
        codigoScrollPane.setViewportView(codigoList);
        outerBox.add(codigoScrollPane);
        
        Container codigoManagerBox = Box.createVerticalBox();
        codigoManagerBox.addContainerListener(listener);

        codigoManagerBox.add(new JButton("Adicionar letras"));
        codigoManagerBox.add(new JButton("Adicionar codigo"));
        codigoManagerBox.add(new JButton("Remover codigo"));

        outerBox.add(codigoManagerBox);

        Container loadCardexBox = Box.createHorizontalBox();
        loadCardexBox.addContainerListener(listener);

        loadCardexBox.add(new JLabel("Vendas: "));
        loadCardexBox.add(new JButton("Antigo"));
        loadCardexBox.add(new JButton("Atual"));
        loadCardexBox.add(new JLabel("modificado"));

        outerBox.add(loadCardexBox);

        outerBox.add(new JScrollPane(new JTextArea()));
        outerBox.add(new JButton("Copiar para clipboard"));

        add(outerBox, BorderLayout.CENTER);
         
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
        case "Antigo":
            print("clicked antigo");
            codigoListModel.addElement("supercalifragilisticexpialidocious");
            codigoList.setModel(codigoListModel);
            break;
        case "Atual":
            print("clicked atual");
            codigoListModel.addElement("Atual");
            codigoList.setModel(codigoListModel);
            break;
        case "Copiar para clipboard":
            print("clicked copy clipboard");
            break;
        default:
            print("unassigned function");
            break;
        }
    }

    public static void main(String[] args) {
        JFrame frame = new JFrame("Cardex Saver");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(268,292);
        frame.setLocation(0, 432);
        frame.setContentPane(new CardexSaver());
        frame.setVisible(true);
    }
}
