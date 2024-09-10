public class prueba{
    public static void main(String args[]) {
        int numero1 = 9;
        int numero2 = 5;
        int resultado = numero1 + numero2;
        System.out.println(numero1);
        System.out.println(numero2);
        System.out.println("La suma de los 2 numeros es: " + resultado);
        if (resultado == 8)
        {
            System.out.println(resultado + " es correcto");
        }
        else{
            System.out.println(resultado + " es incorrecto");
        }
    }
}