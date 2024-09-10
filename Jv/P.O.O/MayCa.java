public class MayCa{
    static public class Magos{ 
        private String nombre;
        private int nivel;
        private String habilidad;
        public Magos(String nombre, int nivel, String habilidad){
                this.nombre = nombre;
                this.nivel = nivel;
                this.habilidad = habilidad;
        }
    }
    static public class Caballeros{ 
        private String nombre;
        private int nivel;
        private String habilidad;
        public Caballeros(String nombre, int nivel, String habilidad){
                this.nombre = nombre;
                this.nivel = nivel;
                this.habilidad = habilidad;
        }
    }
    public static void main(String args[]){
        Magos JonaThan = new Magos("JonaThan", 100, "Fuego");
        Caballeros Kevin = new Caballeros("Kevin", 99, "Fuerza");
        System.out.println("El Mago lleva por nombre: "+JonaThan.nombre);
        System.out.println("Su nivel es: "+JonaThan.nivel);
        System.out.println("Y su habilidad es el: "+JonaThan.habilidad);
        System.out.println("");
        System.out.println("El Caballero lleva por nombre: "+Kevin.nombre);
        System.out.println("Su nivel es: "+Kevin.nivel);
        System.out.println("Y su habilidad es la: "+Kevin.habilidad);
        System.out.println("");
        System.out.println("");
        System.out.println("Comienza un combate mortal entre: "+JonaThan.nombre+" Y "+Kevin.nombre);
        System.out.println("");
        System.out.println("");
    }
}