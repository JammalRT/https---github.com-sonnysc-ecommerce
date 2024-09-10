public class Polimorfismo4{
    public static class Empleado{
        private int antiguedad,id;
        private String nombre, apellidos, direccion, telefono;
        private double salario;
        public Empleado(int id, String nombre, String apellidos, double salario){
            this.id = id;
            this.nombre = nombre;
            this.apellidos = apellidos;
            this.direccion = "";
            this.antiguedad = 0; 
            this.telefono = "";
            this.salario = salario;
        }
        public Empleado(){
            this(0, "", "", 0);
        }
        public void setDireccion(String direccion){
            this.direccion = direccion;
        }
    
        public void setAntiguedad(int antiguedad){
            this.antiguedad = antiguedad;
        }
    
        public void setTelefono(String telefono){
            this.telefono = telefono;
        }
        public void incrementarSalario(double porcentaje){
            salario = salario * (1 + porcentaje/100);
            System.out.println("Salario del empleado con aumento anual: " + salario);
            System.out.println("");
        }        
        public void mostrarinfo(){
            System.out.println("Informacion del empleado: ");
            System.out.println("================================");
            System.out.println("ID: " + id);
            System.out.println("Nombre: " + nombre);
            System.out.println("Apellido: " + apellidos);
            System.out.println("Dirección: " + direccion);
            System.out.println("Antigüedad de: " + antiguedad + " años");
            System.out.println("Teléfono: " + telefono);
            System.out.println("Salario original: " + salario);
            
        }
    }
    public static class Secretario extends Empleado{
        private int despacho, numero;
        public Secretario(int id, String nombre, String apellidos, int salario, int despacho, int numero){
            super(id, nombre, apellidos, salario);
            this.despacho = despacho;
            this.numero = numero;
        }
        public Secretario(int despacho, int numero){
            this.despacho = despacho;
            this.numero = numero;
        }
        public Secretario(){
            this(0, 0);
        }
        @Override
        public void incrementarSalario(double porcentaje){
            super.incrementarSalario(porcentaje);
        }
        @Override
        public void mostrarinfo(){
            super.mostrarinfo();
            System.out.println("Puesto: Secretario");
        }
    }
    public static class Vendedor extends Empleado{
        private String marcaCoche, area;
        public Vendedor(int id, String nombre, String apellidos, double salario, String marcaCoche, String area){
            super(id, nombre, apellidos, salario);
            this.marcaCoche = marcaCoche;
            this.area = area;
        }
        public Vendedor(String marcaCoche, int telefono, String area){
            this.marcaCoche = marcaCoche;
            this.area = area;
        }
        public Vendedor(){
            this("", 0, "");
        }
        @Override
        public void incrementarSalario(double porcentaje){
            super.incrementarSalario(porcentaje);
        }
        @Override
        public void mostrarinfo(){
            super.mostrarinfo();
            System.out.println("Puesto: Vendedor");
        }
        public void cambiarCoche(String marcaCoche) {
            this.marcaCoche = marcaCoche;
            System.out.println("Cambio de coche a un: "+ this.marcaCoche);
        }
    }
    public static class JefeDeZona extends Empleado{
        private int despacho;
        public JefeDeZona(int id, String nombre, String apellidos, double salario, int despacho){
            super(id, nombre, apellidos, salario);
            this.despacho = despacho;
        }
        public JefeDeZona(int despacho){
            this.despacho = despacho;
        }
        public JefeDeZona(){
            this(0);
        }
        @Override
        public void incrementarSalario(double porcentaje){
            super.incrementarSalario(porcentaje);
        }
        @Override
        public void mostrarinfo(){
            super.mostrarinfo();
            System.out.println("Puesto: Jefe de zona");
        }
    }
    public static void main(String[] args) {
        Secretario Kevin = new Secretario(289171561, "Kevin", "Valecia", 240000, 5, 19);
        Vendedor Sergio = new Vendedor(154259354, "Sergio", "de Jesus", 216000, "Renault", "A-18");
        JefeDeZona Jammal = new JefeDeZona(487465113, "Jammal", "Rodriguez", 360000, 2);
        //=================================================
        Kevin.setDireccion("Fracc. Vinedos");
        Kevin.setAntiguedad(5);
        Kevin.setTelefono("618-327-6234");
        Kevin.mostrarinfo();
        Kevin.incrementarSalario(5);
        //=================================================
        Sergio.setDireccion("Calle Washinton");
        Sergio.setAntiguedad(3);
        Sergio.mostrarinfo();
        Sergio.setTelefono("618-109-6437");
        Sergio.cambiarCoche("Ford");
        Sergio.incrementarSalario(10);
        //=================================================
        Jammal.setDireccion("Calle Blvd. Ameyal");
        Jammal.setAntiguedad(10);
        Jammal.setTelefono("618-157-1862");
        Jammal.mostrarinfo();
        Jammal.incrementarSalario(20);
    }
}