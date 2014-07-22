import java.awt.*;
import java.awt.event.*;
import javax.swing.*;
import javax.swing.event.*;

import java.io.*;
import java.nio.file.*;
import java.nio.charset.*;

// import java.util.*;

public class FileOpener extends JFrame implements ActionListener {
    Charset charset;
    JButton button;
    JLabel label;
    
    public FileOpener() {
        super("File opener");
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setSize(200, 200);
        button = new JButton("Load the file");
        button.addActionListener(this);

        label = new JLabel("the label");
        
        add(button, BorderLayout.NORTH);
        add(label, BorderLayout.CENTER);
        
    }

    public void readFromFile() {
        Charset charset = Charset.forName("US-ASCII");
        Path configFile = Paths.get("contents.txt");
        try (BufferedReader reader = Files.newBufferedReader(configFile, charset)) {
                String contents = "";
                String line = null;
                while ((line = reader.readLine()) != null) {
                    contents += line;
                }
                label.setText(contents);
            }
        catch (IOException x) {
            System.err.println("IOException when setting codigo list");
        }

    }

    public void actionPerformed(ActionEvent e) {
        if (e.getActionCommand() == "Load the file") {
            System.out.println("clicked button");
            readFromFile();
        }
    }
    
    public static void main(String[] args) {
        new FileOpener().setVisible(true);
    }
}
