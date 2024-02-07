public class UsesRutNat {

    public static void main(String[] args) {

        Integer[][] bokstaver = new Integer[3][3];

        bokstaver[0][0] = 1;
        bokstaver[0][1] = 2;
        bokstaver[0][2] = 3;

        bokstaver[1][0] = 4;
        bokstaver[1][1] = 5;
        bokstaver[1][2] = 6;

        bokstaver[2][0] = 7;
        bokstaver[2][1] = 8;
        bokstaver[2][2] = 9;

        RutNat.printaRutnat(bokstaver);
    }
}
