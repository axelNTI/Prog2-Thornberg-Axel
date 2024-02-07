public class RutNat {

    public static <T> void printaRutnat(T[][] element) {

        for (int i = 0; i < element.length; i++) {
            for (int j = 0; j < element[i].length; j++) {
                System.out.print(element[i][j] + " ");
            }
            System.out.print("\n");
        }
    }
}
