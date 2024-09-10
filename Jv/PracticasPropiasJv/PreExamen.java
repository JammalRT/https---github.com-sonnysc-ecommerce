public class Pre_examen {
    static public class Electrodomenstico{
        private int Precio;
        private String Color;
        private int ConsumoW;
        private int PesoK;
        public Electrodomenstico(int Precio, String Color, int ConsumoW, int PesoK){
            this.Color = Color;
            this.ConsumoW = ConsumoW;
            this.Precio = Precio;
            this.PesoK = PesoK;
        }
        public void mostrarInformacion(){
            System.out.println("Colores disponibles: blanco, Negro, Rojo, Azul y gris ");
            System.out.println("=========================================");
            System.out.println("El color es: " + Color);
            System.out.println("El precio es: " + Precio);
            System.out.println("EL consumo es: " + ConsumoW + " Watts");
            System.out.println("Sue peso es de: " + PesoK + " Kilos");
            System.out.println("=========================================");
        }
        public int getPrecio(){
            return Precio;
        }
        public String getColor(){
            return Color;
        }
        public int getConsumoW(){
            return ConsumoW;
        }
        public int getPesoK(){
            return PesoK;
        }
        public void setPrecio(int Precio){
            this.Precio = Precio;
        }
        public void setColor(String Color){
            this.Color = Color;
        }
        public void setConsumoW(int ConsumoW){
            this.ConsumoW = ConsumoW;
        }
        public void setPesoK(int PesoK){
            this.PesoK = PesoK;
        }
    }
    static public class Lavadora extends Electrodomenstico{
        private int Carga;
        public Lavadora(int Carga, int Precio, String Color, int ConsumoW, int PesoK){
            super(Precio, Color, ConsumoW, PesoK);
            this.Carga = Carga;
        }
        public int getCarga(){
            return Carga;
        }
        public void mostrarInformacion(){
            super.mostrarInformacion();
            System.out.println("La carga es de: " + getCarga());
            System.out.println(this.PrecioFinalL());
        }
        public void setCarga(int Carga){
            this.Carga = Carga;
        }
        public int PrecioFinalL() {
            int Precio = super.Precio;
            if (this.Carga >= 30) {
                Precio += 500;
                System.out.println("Su Carga es de mas de 30 kilos el precio aumenta a:");
            }
            return Precio;
        }
    }
    static public class Television extends Electrodomenstico{
        private int Pulgadas;
        private boolean Smart;
        public Television(int Pulgadas, boolean Smart, int Precio, String Color, int ConsumoW, int PesoK){
            super(Precio, Color, ConsumoW, PesoK);
            this.Pulgadas = Pulgadas;
            this.Smart = Smart;
        }
        public int getPulgadas(){
            return Pulgadas;
        }
        public void mostrarInformacion(){
            super.mostrarInformacion();
            System.out.println("El tamano es de: " + Pulgadas);
            System.out.println(this.PrecioFinal());
        }
        public void setPulgadas(int Pulgadas){
            this.Pulgadas = Pulgadas;
        }
        public boolean getSmart(){
            return Smart;
        }
        public void setSmart(Boolean Smart){
            this.Smart = Smart;
        }
        public int PrecioFinal(){
            int Precio = super.Precio;
            if (Pulgadas > 40){
                int aumento = (super.Precio * 30)/100;
                Precio += aumento;
                System.out.println("La Televicion es de las de 40 pulgadas y el precio aumento");
                if (Smart == true){
                    System.out.println("La televicion es SmarTV, el precio aumento: ");
                    Precio += 1500;
                }
            }
            return Precio;
        }
    }
    public static void main(String[] args) {
        Electrodomenstico Mabe = new Lavadora(35, 2000, "Negro", 100, 10);
        Electrodomenstico Lg = new Television(50, true, 3000, "Rojo", 100, 5);
        Mabe.mostrarInformacion();
        System.out.println("====================================");
        Lg.mostrarInformacion();
    }
}