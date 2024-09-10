public class Examen {
    static public class Bebidas{
        private int Precio;
        private int Codigo;
        private int Mililitros;
        private String Marca;
        public Bebidas(){
        }
        public Bebidas(int Precio, int Mililitros){
            this.Mililitros = Precio;
            this.Precio = Precio;
        }
        public Bebidas(int Precio, int Mililitros, String Marca, int Codigo){
            this.Codigo = Codigo;
            this.Mililitros = 600;
            this.Precio = 18;
            this.Marca = Marca;
        }
        public void mostrarInformacion(){
            System.out.println("=========================================");
            System.out.println("El codigo es: " + Codigo);
            System.out.println("El precio es: " + Precio + " Pesos");
            System.out.println("EL contenido es: " + Mililitros + " Mlt");
            System.out.println("El producto es de marca: " + Marca );
            System.out.println("=========================================");
        }
        public int getPrecio(){
            return Precio;
        }
        public int getCodigo(){
            return Codigo;
        }
        public int getMililitros(){
            return Mililitros;
        }
        public String getMarca(){
            return Marca;
        }
        public void setPrecio(int Precio){
            this.Precio = Precio;
        }
        public void setMarca(String Marca){
            this.Marca = Marca;
        }
        public void setMililitros(int Mililitros){
            this.Mililitros = Mililitros;
        }
        public void setCodigo(int Codigo){
            this.Codigo = Codigo;
        }
    }
    static public class AguaMineral extends Bebidas{
        private String Origen;
        public AguaMineral(){
        }
        public AguaMineral(String Origen, int Precio, int Mililitros){
            super(Precio, Mililitros);
            this.Origen = Origen;
        }
        public AguaMineral(String Origen, int Precio, int Mililitros, String Marca, int Codigo ){
            super(Precio, Mililitros, Marca, Codigo);
            this.Origen = Origen;
        }
        public String getOrigen(){
            return Origen;
        }
        public void setOrigen(String Origen){
            this.Origen = Origen;
        }
        public void mostrarInformacion(){
            super.mostrarInformacion();
            System.out.println("la Bebida es de: " + getOrigen());
            System.out.println(this.PrecioFinalL());
        }
        
        public int PrecioFinalL() {
            int Precio = super.Precio;
            if (this.Origen == "Manantial") {
                int aumento = (super.Precio * 50)/100;
                Precio += aumento;
                System.out.println("Su bebida es de manantial precio aumenta a:");
            }
            return Precio;
        }
    }
    static public class BebidaAzucarada extends Bebidas{
        private int Porcentaje;
        private boolean Promocion;
        public BebidaAzucarada(){
        }
        public BebidaAzucarada(int Porcentaje, boolean Promocion, int Precio, int Mililitros){
            super(Precio, Mililitros);
            this.Porcentaje = Porcentaje;
            this.Promocion = Promocion;
        }
        public BebidaAzucarada(int Porcentaje, boolean Promocion, int Precio, int Mililitros,  String Marca, int Codigo ){
            super(Precio, Mililitros, Marca, Codigo);
            this.Porcentaje = Porcentaje;
            this.Promocion = Promocion;
        }
        public int getPorcentaje(){
            return Porcentaje;
        }
        public void setPorcentaje(int Porcentaje){
            this.Porcentaje = 10;
        }
        public boolean getPromocion(){
            return Promocion;
        }
        public void setPromocion(Boolean Promocion){
            this.Promocion = false;
        }
        public void mostrarInformacion(){
            super.mostrarInformacion();
            System.out.println("La bebida esta en promocion: ");
            System.out.println(this.PrecioFinal());
        }
        public int PrecioFinal(){
            int Precio = super.Precio;
            if (Promocion == true){
                int decre = (super.Precio * 50)/100;
                Precio -= decre;
                System.out.println("El precio actual es de: ");
            }
            return Precio;
        }
    }
    public static void main(String[] args) {
        Bebidas TopoChico = new AguaMineral("Manantial", 0, 0, "Pepsi", 87654321);
        Bebidas Fanta = new BebidaAzucarada(10, true, 0, 0, "CocaCola", 12345678);
        TopoChico.mostrarInformacion();
        Fanta.mostrarInformacion();
    }
}