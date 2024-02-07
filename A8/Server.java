package A8;

import java.net.ServerSocket;
import java.net.Socket;

public class Server {

    public static void main(String[] args) {

        System.out.println("Detta är Server-programmet.");

        try {
            ServerSocket server = new ServerSocket(40000);

            System.out.println("Väntar på att en klient ska ansluta...");
            Socket anslutning = server.accept();
            System.out.println("Nu anslöt en klient!");

            System.out.println("Klienten anslöt från adress: " + anslutning.getInetAddress());
            server.close();

        } catch (Exception e) {
            System.out.println("Något gick fel: " + e.getMessage());
        }

        System.out.println("Nu avslutas Server-programmet.");
    }

}
