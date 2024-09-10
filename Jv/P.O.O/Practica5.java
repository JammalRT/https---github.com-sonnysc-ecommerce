public class Practica5{
    static public class Magos{ 
        private String Nombre;
        private int Nivel;
        private String Tipo;
        private String Habilidad;
        public Magos(String Nombre, int Nivel,String Tipo, String Habilidad){
                this.Nombre =   Nombre;
                this.Nivel = Nivel;
                this.Habilidad = Habilidad;
                this.Tipo = Tipo;
        }
        public void setNombre(String Nombre){
            this.Nombre = Nombre;
        }
        public String getNombre(){
            return Nombre;
        }
        public int getNivel(){
            return Nivel;
        }
        public String getTipo(){
            return Tipo;
        }
        public String getHabilidad(){
            return Habilidad;
        }
        public void muestra_info(){
        }
        
    }
    public static void main(String args[]){
        Magos JonaThan = new Magos("JonaTAN", 50, "Hechicero", "MAgia de fuego");
        System.out.println(JonaThan);
    }
}