public class Ej1 {
    static public class Persona{
        private String nombre;
        private int edad;
        public Persona(String nombre, int edad){
            this.nombre = nombre;
            this.edad = edad;
        }
        public void datos(Persona otra_persona){
            System.out.println("Hola "+otra_persona.nombre+" Mi nombre es "+nombre+" Y mi edad es "+edad);
        }
    }
    public static void main(String args[]) {
        Persona Jammal = new Persona("Jammal", 18);
        Persona Jonathan = new Persona("Jonathan", 19);
        Jammal.datos(Jonathan);
    }
}
