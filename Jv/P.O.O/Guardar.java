import java.awt.*;
import javax.swing.*;

public class Guardar {

    public static void main(String[] args) {
        final int MAXIMUM = 100;
        final JFrame jFrame = new JFrame("JProgress Demo One");

        // create horizontal progress bar
        final JProgressBar progressBar = new JProgressBar();
        progressBar.setMinimum(0);
        progressBar.setMaximum(MAXIMUM);
        progressBar.setStringPainted(true);

        // add progress bar to the content pane layer
        jFrame.setLayout(new FlowLayout());
        jFrame.getContentPane().add(progressBar);
        jFrame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        jFrame.setSize(300, 200);
        jFrame.setVisible(true);

        // update progressbar staring from 0 to 100
        for (int i = 0; i <= MAXIMUM; i++) {
            final int currentNumber = i;
            try {
                SwingUtilities.invokeLater(new Runnable() {
                    public void run() {
                        progressBar.setValue(currentNumber);
                    }
                });
                java.lang.Thread.sleep(1);
            } catch (InterruptedException event) {
                JOptionPane.showMessageDialog(jFrame, event.getMessage());
            }
        }
    }
}