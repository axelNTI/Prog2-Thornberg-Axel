package A8;

import java.io.IOException;
import java.net.Socket;

public class Klient {
    public static void main(String[] args) {
        System.out.println("Detta är Klient-programmet.");

        try {
            Socket klient = new Socket("127.0.0.1", 40000);
            System.out.println("Vi lyckades ansluta till servern.");
            klient.close();

        } catch (IOException e) {
            System.out.println("Kunde inte ansluta till servern: " + e.getMessage());
        }
        System.out.println("Nu avslutas Klient-programmet.");
    }

}
