package A8;

import java.io.DataOutputStream;
import java.net.Socket;
import java.util.Random;

public class Klient2 {

    public static void main(String[] args) {
        System.out.println("Detta är Klient-programmet.");
        Random rand = new Random();
        try {
            Socket klient = new Socket("127.0.0.1", 40000);
            System.out.println("Vi lyckades ansluta till servern.");

            // skicka siffermeddelande till klienten
            DataOutputStream output = new DataOutputStream(klient.getOutputStream());
            output.writeInt(rand.nextInt(64) + 1);

            // stäng ner anslutningen
            output.close();
            klient.close();

        } catch (Exception e) {
            System.out.println("Kunde inte ansluta till servern: " + e.getMessage());

        }
        System.out.println("Nu avslutas Klient-programmet.");
    }

}
