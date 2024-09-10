import java.util.Random;
public class Practica3 {
    static public class lampara {
        String tipo;
        String colorLuz;
        int watts;
        boolean estado;
        
        public lampara(String tipo, String colorLuz, int watts) {
          this.tipo = tipo;
          this.colorLuz = colorLuz;
          this.watts = watts;
          this.estado = true;
        }
        
        public void encender() {
          estado = true;
          System.out.println("La lampara se ha encendido");
          System.out.println("");
          System.out.println("============================================");
        }
        public void apagar() {
          estado = false;
          System.out.println("La lampara se ha apagado");
          System.out.println("");
          System.out.println("============================================");
        }
        public void mostrarEstado() {
          System.out.println("Estado de la lampara: " + (estado ? "Prendida" : "Apagada"));
        }
        public void mostrarInfo() {
          System.out.println("Tipo de lampara: " + tipo);
          System.out.println("");
          System.out.println("Color de luz: " + colorLuz);
          System.out.println("");
          System.out.println("Watts consume: " + watts);
          System.out.println("");
        }
        public static void main(String[] args) {
            lampara tradicional = new lampara("Tradicional" , "blanca", 100);
            lampara led = new lampara("LED", "Blanco hielo", 50);
            lampara ahorradora = new lampara("Ahorradora", "Blanco palido", 30);
            Random voltaje = new Random();
            boolean voltramtra = voltaje.nextBoolean();
            boolean voltramled = voltaje.nextBoolean();
            boolean voltramaho = voltaje.nextBoolean();
            tradicional.mostrarInfo();
            if (voltramtra == false){
                tradicional.apagar();
            }
            else if (voltramtra == true){
                tradicional.encender();
            }
            led.mostrarInfo();
            if (voltramled == false){
                led.apagar();
            }
            else if (voltramled == true){
                led.encender();
            }
            ahorradora.mostrarInfo();
            if (voltramaho == false){
                ahorradora.apagar();
            }
            else if (voltramaho == true){
                ahorradora.encender();
            }
        }
    }
}
