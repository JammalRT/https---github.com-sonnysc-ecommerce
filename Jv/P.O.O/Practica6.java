//Josue Jammal Rodriguez Torres 2^B
public class Practica6{
    static public class Producto {
        private String Caducidad;
        private int numLote;
        public Producto(String Caducidad, int numLote) {
            this.Caducidad = Caducidad;
            this.numLote = numLote;
        }
        public String getCaducidad() {
            return Caducidad;
        }
        public void setCaducidad(String Caducidad) {
            this.Caducidad = Caducidad;
        }
        public int getNumLote() {
            return numLote;
        }
        public void setNumLote(int numLote) {
            this.numLote = numLote;
        }
        public void mostrarInformacion() {
            System.out.println("Fecha de caducidad: " + Caducidad);
            System.out.println("Número de lote: " + numLote);
        }
    }
    static public class ProductoFresco extends Producto {
        private String fechaEnvasado;
        private String Origen;
        public ProductoFresco(String Caducidad, int numLote, String fechaEnvasado, String Origen) {
            super(Caducidad, numLote);
            this.fechaEnvasado = fechaEnvasado;
            this.Origen = Origen;
        }
        public String getFechaEnvasado() {
            return fechaEnvasado;
        }
        public void setFechaEnvasado(String fechaEnvasado) {
            this.fechaEnvasado = fechaEnvasado;
        }
        public String getOrigen() {
            return Origen;
        }
        public void setOrigen(String Origen) {
            this.Origen = Origen;
        }
        public void mostrarInformacion() {
            super.mostrarInformacion();
            System.out.println("Fecha de envasado: " + fechaEnvasado);
            System.out.println("País de origen: " + Origen);
        }
    }
    static public class ProductoRefrigerado extends Producto {
        private String codigoOrganismo;
        public ProductoRefrigerado(String Caducidad, int numLote, String codigoOrganismo) {
            super(Caducidad, numLote);
            this.codigoOrganismo = codigoOrganismo;
        }
        public String getCodigoOrganismo() {
            return codigoOrganismo;
        }
        public void setCodigoOrganismo(String codigoOrganismo) {
            this.codigoOrganismo = codigoOrganismo;
        }
        public void mostrarInformacion() {
            super.mostrarInformacion();
            System.out.println("El codigo es : " + codigoOrganismo);
        }
    }
    static public class Congelado extends Producto {
        private String Temperatura;
        public Congelado(String Caducidad, int numLote, String Temperatura) {
            super(Caducidad, numLote);
            this.Temperatura = Temperatura;
        }
        public String getTemperatura() {
            return Temperatura;
        }
        public void setTemperatura(String Temperatura) {
            this.Temperatura = Temperatura;
        }
        public void mostrarInformacion() {
            super.mostrarInformacion();
            System.out.println("Temperatura recomendada para la congelacio: "+Temperatura);
    
        } 
    }
    public static void main(String[] args) {
        Producto ProductoFresco = new ProductoFresco("02/12/23",1234567890,"12/31/22","MEXICO");
        System.out.println("La informacion de el ProductoFresco es ");
        ProductoFresco.mostrarInformacion();
        System.out.println(" ");
        Producto ProductoRefrigerado = new ProductoRefrigerado("23/09/23",1987654321,"1a2b3c4d5e");
        System.out.println("La informacion de el ProdutoRefrigerado es ");
        ProductoRefrigerado.mostrarInformacion();
        System.out.println(" ");
        Producto ProductoCongelado = new Congelado("12/12/23", 2004200846,"0 grados");
        System.out.println("La informacion de el Produtofresco es ");
        ProductoCongelado.mostrarInformacion();
        System.out.println(" ");
    }
}