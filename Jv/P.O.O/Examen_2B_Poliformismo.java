public class Examen_2B_Poliformismo{
    static public class Seleccion {
        private int id, edad;
        private String nombre, apellidos;
        public Seleccion(int id, String nombre, String apellidos, int edad) {
            this.id = id;
            this.nombre = nombre;
            this.apellidos = apellidos;
            this.edad = edad;
        }
        public Seleccion() {
            this.id = 0;
            this.nombre = "";
            this.apellidos = "";
            this.edad = 0;
        }
        public int getId() {
            return id;
        }
        public String getNombre() {
            return nombre;
        }
        public String getApellidos() {
            return apellidos;
        }
        public int getEdad() {
            return edad;
        }
        public void setId(int id) {
            this.id = id;
        }
        public void setNombre(String nombre) {
            this.nombre = nombre;
        }
        public void setApellidos(String apellidos) {
            this.apellidos = apellidos;
        }
        public void setEdad(int edad) {
            this.edad = edad;
        }
        public void imprimir() {
            System.out.println("");
            System.out.println("==========================================================");
            System.out.println("ID: " + this.id);
            System.out.println("Nombre: " + this.nombre);
            System.out.println("Apellidos: " + this.apellidos);
            System.out.println("Edad: " + this.edad);
            System.out.println("");
        }
        public void concentrarse() {
            System.out.println("La selección está concentrándose");
        }
        public void viajar() {
            System.out.println("La selección está viajando");
        }
    }
    static public class Futbolista extends Seleccion {
        private int numero_playera;
        private String posicion;
        public Futbolista(int id, String nombre, String apellidos, int edad, int numero_playera, String posicion) {
            super(id, nombre, apellidos, edad);
            this.numero_playera = numero_playera;
            this.posicion = posicion;
        }
        public Futbolista() {
            super();
            this.numero_playera = 0;
            this.posicion = "";
        }
        @Override
        public void imprimir() {
            super.imprimir();
            System.out.println("Número de playera: " + this.numero_playera);
            System.out.println("Posición: " + this.posicion);
        }
        public void jugarPartido() {
            System.out.println("El jugador " + this.getNombre() + " está jugando un partido");
        }
        public void entrenar() {
            System.out.println("El jugador " + this.getNombre() + " está entrenando");
        }
        @Override
        public void concentrarse() {
            super.concentrarse();
            System.out.println("El jugador " + this.getNombre() + " también está concentrándose");
        }
        @Override
        public void viajar() {
            super.viajar();
            System.out.println("El jugador " + this.getNombre() + " también está viajando");
        }
    }
    static public class Entrenador extends Seleccion {
        private String nacionalidad;
        public Entrenador(int id, String nombre, String apellidos, int edad, String nacionalidad) {
            super(id, nombre, apellidos, edad);
            this.nacionalidad = nacionalidad;
        }
        public Entrenador() {
            super();
            this.nacionalidad = "";
        }
        @Override
        public void imprimir() {
            super.imprimir();
            System.out.println("Nacionalidad: " + this.nacionalidad);
        }
        public void dirigirPartido() {
            System.out.println("El entrenador " + this.getNombre() + " está dirigiendo un partido");
        }
        public void dirigirEntrenamiento() {
            System.out.println("El entrenador " + this.getNombre() + " está dirigiendo un entrenamiento");
        }
        @Override
        public void concentrarse() {
            super.concentrarse();
            System.out.println("El entrenador " + this.getNombre() + " también está concentrándose");
        }
        @Override
        public void viajar() {
            super.viajar();
            System.out.println("El entrenador " + this.getNombre() + " también está viajando");
        }
    }
    static public class Masajista extends Seleccion {
        private int anios_experiencia;
    
        public Masajista(int id, String nombre, String apellidos, int edad, int anios_experiencia) {
            super(id, nombre, apellidos, edad);
            this.anios_experiencia = anios_experiencia;
        }
        public Masajista() {
            super();
            this.anios_experiencia = 0;
        }
        @Override
        public void imprimir() {
            super.imprimir();
            System.out.println("Años de experiencia: " + this.anios_experiencia);
        }
        public void darMasaje() {
            System.out.println("El masajista " + this.getNombre() + " está dando un masaje");
        }
        @Override
        public void viajar() {
            super.viajar();
            System.out.println("El masajista " + this.getNombre() + " también está viajando");
        }
    }
    public static void main(String[] args) {
        Futbolista messi = new Futbolista(351654321, "Lionel", "Messi", 34, 10, "Delantero");
        Entrenador Soto = new Entrenador(1186468438, "Sergio", "Soto", 51, "Español");
        Masajista Kevin = new Masajista(568435468, "Kevin", "Valencia", 40, 15);
        messi.imprimir();
        messi.jugarPartido();
        messi.entrenar();
        messi.concentrarse();
        messi.viajar();
        //======================================
        Soto.imprimir();
        Soto.dirigirPartido();
        Soto.dirigirEntrenamiento();
        Soto.concentrarse();
        Soto.viajar();
        //======================================
        Kevin.imprimir();
        Kevin.darMasaje();
        Kevin.concentrarse();
        Kevin.viajar();
        System.out.println("");
    }
}