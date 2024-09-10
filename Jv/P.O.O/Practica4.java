import java.util.Scanner;
public class Practica4 {
   static public class Carro{
        String Marca;
        boolean Estado;
        int Km, Modelo;
        public Carro(String Marca, boolean Estado, int Km, int Modelo){
            this.Marca = Marca;
            this.Estado = Estado;
            this.Km = Km;
            this.Modelo = Modelo;
        }
        public void setEstado(boolean estado){
            this.Estado = estado;
        }
        public boolean getEstado(){
            return Estado;
        }
        public String getMarca(){
            return Marca;
        }
        public void muestra_info(){
            System.out.println("La marca del carro es: "+Marca+" etc..........");
        }
    }
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        System.out.println("Ingresa la marca del carro: ");
        String marca_e = entrada.nextLine();
        System.out.println("Ingrese los Km: ");
        String Km_e = entrada.nextLine();
        int Km = Integer.parseInt(Km_e, 0);
        Carro carro1 = new Carro("BMW", false, 300, 2022);
        carro1.setEstado(true);
        System.out.println(carro1.getEstado());
    }
}