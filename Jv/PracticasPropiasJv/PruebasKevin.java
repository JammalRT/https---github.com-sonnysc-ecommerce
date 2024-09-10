public class PruebasKevin {
    public class Peleador {
        private String nombre;
        private int nivelPelea;
        private int porcentajeVida;
    
        public Peleador(String nombre, int nivelPelea) {
            this.nombre = nombre;
            this.nivelPelea = nivelPelea;
            this.porcentajeVida = 100;
        }
    
        public void setNombre(String nombre) {
            this.nombre = nombre;
        }
    
        public String getNombre() {
            return nombre;
        }
    
        public void setNivelPelea(int nivelPelea) {
            this.nivelPelea = nivelPelea;
        }
    
        public int getNivelPelea() {
            return nivelPelea;
        }
    
        public void setPorcentajeVida(int porcentajeVida) {
            this.porcentajeVida = porcentajeVida;
        }
    
        public int getPorcentajeVida() {
            return porcentajeVida;
        }
    
        public void atacar(Peleador oponente) {
            int danio = nivelPelea * 5;
            oponente.setPorcentajeVida(oponente.getPorcentajeVida() - danio);
        }
    }
    
    public class Boxeador extends Peleador {
        private int peso;
    
        public Boxeador(String nombre, int nivelPelea, int peso) {
            super(nombre, nivelPelea);
            this.peso = peso;
        }
    
        public void setPeso(int peso) {
            this.peso = peso;
        }
    
        public int getPeso() {
            return peso;
        }
    
        @Override
        public void atacar(Peleador oponente) {
            int danio = getNivelPelea() * 7;
            oponente.setPorcentajeVida(oponente.getPorcentajeVida() - danio);
        }
    }
    
    static public class Taekwondin extends Peleador {
        private String cinta;
    
        public Taekwondin(String nombre, int nivelPelea, String cinta) {
            super(nombre, nivelPelea);
            this.cinta = cinta;
        }
    
        public void setCinta(String cinta) {
            this.cinta = cinta;
        }
    
        public String getCinta() {
            return cinta;
        }
    
        @Override
        public void atacar(Peleador oponente) {
            int danio = getNivelPelea() * 6;
            oponente.setPorcentajeVida(oponente.getPorcentajeVida() - danio);
        }
    }


        public static void main(String[] args) {

            actividad1peleadores.Boxeador boxeador1 = new actividad1peleadores.Boxeador("Mike Tyson", 10, 90);
            actividad1peleadores.Taekwondin taekwondin1 = new actividad1peleadores.Taekwondin("Bruce Lee", 8, "Negra");
            actividad1peleadores.Peleador peleador1 = new actividad1peleadores.Peleador("Chuck Norris", 9);
    
            System.out.println("Comienza la pelea: " + boxeador1.getNombre() + " vs " + taekwondin1.getNombre());
            System.out.println(boxeador1.getNombre() + " tiene un nivel de pelea de " + boxeador1.getNivelPelea() + " y un peso de " + boxeador1.getPeso() + " kg");
            System.out.println(taekwondin1.getNombre() + " tiene un nivel de pelea de " + taekwondin1.getNivelPelea() + " y una cinta " + taekwondin1.getCinta());
    
            while (boxeador1.getPorcentajeVida() > 0 && taekwondin1.getPorcentajeVida() > 0) {
                boxeador1.atacar(taekwondin1);
                taekwondin1.atacar(boxeador1);
                System.out.println(boxeador1.getNombre() + " ataca a " + taekwondin1.getNombre() + " y le quita " + boxeador1.getNivelPelea() * 7 + " puntos de vida");
                System.out.println(taekwondin1.getNombre() + " ataca a " + boxeador1.getNombre() + " y le quita " + taekwondin1.getNivelPelea() * 6 + " puntos de vida");
                System.out.println(boxeador1.getNombre() + " tiene " + boxeador1.getPorcentajeVida() + "% de vida restante");
                System.out.println(taekwondin1.getNombre() + " tiene " + taekwondin1.getPorcentajeVida() + "% de vida restante");
            }
    
            if (boxeador1.getPorcentajeVida() > 0) {
                System.out.println(boxeador1.getNombre() + " ha ganado la pelea!");
            } else {
                System.out.println(taekwondin1.getNombre() + " ha ganado la pelea!");
            }
    
        }
        
    
}


