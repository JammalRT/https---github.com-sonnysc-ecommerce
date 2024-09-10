public class Polimorfismo {
    static public class Peleador {
        String nombre;
        int nivelPelea;
        int porcentajeVida;
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
            System.out.println("Nivel de pelea: " + this.nivelPelea);
            System.out.println("Porcentaje de vida: " + this.porcentajeVida);
        }
    }
    static public class Boxeador extends Peleador {
        int peso;
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
            int danio = this.getNivelPelea() * 5;
            oponente.recibirDanio(danio);
        }
    }
    static public class Taekwondin extends Peleador {
        String cinturon;
        public Taekwondin(String nombre, int nivelPelea, String cinturon) {
            super(nombre, nivelPelea);
            this.cinturon = cinturon;
        }
        public String getCinturon() {
            return cinturon;
        }
        public void setCinturon(String cinturon){
            this.cinturon = cinturon;
        }
        @Override
        public void atacar(Peleador oponente) {
            int danio = this.getNivelPelea() * 5;
            oponente.recibirDanio(danio);
        }
    }
    public static void main(String[] args) {
        Peleador peleador1 = new Boxeador("Jammal", 10, 90);
        Peleador peleador2 = new Taekwondin("Kevin", 8, "Negro");

        while (peleador1.getPorcentajeVida() > 0 && peleador2.getPorcentajeVida() > 0) {
            // peleador1 ataca a peleador2
            peleador1.atacar(peleador2);
            System.out.println(peleador1.getNombre() + " hace " + (peleador1.getNivelPelea() * 5) + " de daño a " + peleador2.getNombre());
            System.out.println(peleador2.getNombre() + " queda con " + peleador2.getPorcentajeVida() + " de vida.");

            // peleador2 ataca a peleador1
            peleador2.atacar(peleador1);
            System.out.println(peleador2.getNombre() + " hace " + (peleador2.getNivelPelea() * 5) + " de daño a " + peleador1.getNombre());
            System.out.println(peleador1.getNombre() + " queda con " + peleador1.getPorcentajeVida() + " de vida.");
        }

        if (peleador1.getPorcentajeVida() == 0 && peleador2.getPorcentajeVida() == 0) {
            System.out.println("¡Empate!");
        } else if (peleador1.getPorcentajeVida() == 0) {
            System.out.println(peleador2.getNombre() + " gana!");
        } else {
            System.out.println(peleador1.getNombre() + " gana!");
        }
    }
}
