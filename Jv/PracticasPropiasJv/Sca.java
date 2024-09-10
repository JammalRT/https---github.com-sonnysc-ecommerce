import java.util.Scanner;
public class Sca
{
    public static void main(String args[])
    {
        Scanner nom = new Scanner(System.in);
        String nombre = "";
        int num1 = 0, num2 = 0, res = 0;
        System.out.println("Cual es tu nombre? ");
        nombre = nom.nextLine();
        System.out.println("Dame el primer valor para la suma: ");
        num1 = nom.nextInt();
        System.out.println("Dame el segundo valor para la suma: ");
        num2 = nom.nextInt();
        res = num1 + num2;
        System.out.println("Hola "+nombre+" el resultado de tu suma es: "+ res);
    }
}