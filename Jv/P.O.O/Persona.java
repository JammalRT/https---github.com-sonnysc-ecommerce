import java.util.Random;
import java.util.Scanner;
public class Persona {
    private String nombre;
    private int edad;
    private String DNI;
    private String sexo;
    private double peso;
    private double altura;
    public Persona() {
        this.nombre = null;
        this.edad = 0;
        this.DNI = null;
        this.sexo = null;
        this.peso = 0;
        this.altura = 0;
    }
    public void calcularIMC() {
        double imc = peso / (altura * altura);
        if (imc < 20) {
            System.out.println("Peso bajo");
            System.out.println("==================================");
        } 
        else if (imc >= 20 && imc <= 25) {
            System.out.println("Peso ideal");
            System.out.println("==================================");
        } 
        else {
            System.out.println("Sobrepeso");
            System.out.println("==================================");
        }
    }
    public boolean esMayorDeEdad() {
        if (edad >= 18) {
            return true;
        }
        return false;
    }
    public void muestraDatos() {
        System.out.println("Nombre: " + nombre);
        System.out.println("Edad: " + edad);
        System.out.println("DNI: " + DNI);
        System.out.println("Sexo: " + sexo);
        System.out.println("Peso: " + peso);
        System.out.println("Altura: " + altura);
    }
    public void generaDNI() {
        Random rnd = new Random(10000000);
        int numero = rnd.nextInt(99999999);
        char letra = (char) (rnd.nextInt(26)+65);
        DNI = numero + "" + letra;
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Persona persona1 = new Persona();
        System.out.println("Ingrese su Nombre: ");
        persona1.nombre = sc.next();
        System.out.println("Ingrese su Edad: ");
        persona1.edad = sc.nextInt();
        persona1.generaDNI();
        System.out.println("Ingrese su Peso: ");
        persona1.peso = sc.nextDouble();
        System.out.println("Ingrese su Sexo: ");
        persona1.sexo = sc.next();
        System.out.println("Ingrese su Altura: ");
        persona1.altura = sc.nextDouble();
        persona1.calcularIMC();
        persona1.esMayorDeEdad();
        persona1.muestraDatos();
        
    }
}