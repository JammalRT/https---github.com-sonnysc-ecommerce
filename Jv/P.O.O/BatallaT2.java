public class BatallaT2{
    static public class Peleador {
        private String nombre;
        private int nivelPelea;
        private int porcentajeVida;
        public Peleador(String nombre, int nivelPelea) {
            this.nombre = nombre;
            this.nivelPelea = nivelPelea;
            this.porcentajeVida = 100;
        }

        public String getNombre() {
            return nombre;
        }

        public int getNivelPelea() {
            return nivelPelea;
        }
        
        public int getPorcentajeVida() {
            return porcentajeVida;
        }

        public void setNombre(String nombre) {
            this.nombre = nombre;
        }

        public void setNivelPelea(int nivelPelea) {
            this.nivelPelea = nivelPelea;
        }

        public void setPorcentajeVida(int porcentajeVida) {
            this.porcentajeVida = porcentajeVida;
        }

        public void atacar(Peleador oponente) {
            int danio = this.nivelPelea * 5;
            oponente.recibirDanio(danio);
        }

        public void recibirDanio(int danio) {
            this.porcentajeVida -= danio;
            if (this.porcentajeVida < 0) {
                this.porcentajeVida = 0;
            }
        }

        public void mostrarInformacion() {
            System.out.println("Nombre: " + this.nombre);
            System.out.println("Nivel: " + this.nivelPelea);
            System.out.println("Vida: " + this.porcentajeVida);
        }

    }
    static public class Boxeador extends Peleador {
        private int peso;
        public Boxeador(String nombre, int nivelPelea, int peso) {
            super(nombre, nivelPelea);
            this.peso = peso;
        }

        public int getPeso() {
            return peso;
        }

        public void setPeso(int peso) {
            this.peso = peso;
        }
        @Override
        public void atacar(Peleador oponente) {
            int danio = this.getNivelPelea() * 5 + this.peso / 10;
            oponente.recibirDanio(danio);
        }
    }
    static public class Karateca extends Peleador {
        private String cinta;
        public Karateca(String nombre, int nivelPelea, String cinta) {
            super(nombre, nivelPelea);
            this.cinta = cinta;
        }

        public String getCinta() {
            return cinta;
        }

        public void setCinta(String cinta) {
            this.cinta = cinta;
        }

        @Override
        public void atacar(Peleador oponente) {
            int danio = this.getNivelPelea() * 5 + this.cinta.length();
            oponente.recibirDanio(danio);
        }

    }
    public static void main(String[] args) {
        Boxeador boxeador = new Boxeador("Mike Tyson", 10, 100);
        Karateca karateca = new Karateca("Bruce Lee", 8, "Negra");
        while (boxeador.getPorcentajeVida() > 0 && karateca.getPorcentajeVida() > 0) {
            // El boxeador ataca al karateca
            boxeador.atacar(karateca);
            System.out.println(boxeador.getNombre() + " ataca a " + karateca.getNombre() + " y le hace " +
                    (boxeador.getNivelPelea() * 5 + boxeador.getPeso() / 10) + " puntos de daño.");
            // Si el karateca no queda KO, ataca al boxeador
            if (karateca.getPorcentajeVida() > 0) {
                karateca.atacar(boxeador);
                System.out.println(karateca.getNombre() + " ataca a " + boxeador.getNombre() + " y le hace " +
                        (karateca.getNivelPelea() * 5 + karateca.getCinta().length()) + " puntos de daño.");
            }
            System.out.println(boxeador.getNombre() + " tiene " + boxeador.getPorcentajeVida() + "% de vida.");
            System.out.println(karateca.getNombre() + " tiene " + karateca.getPorcentajeVida() + "% de vida.");
            System.out.println();
        }

        if (boxeador.getPorcentajeVida() == 0) {
            System.out.println(karateca.getNombre() + " ha ganado la pelea!");
        } 
        else {
            System.out.println(boxeador.getNombre() + " ha ganado la pelea!");
        }
    }
}