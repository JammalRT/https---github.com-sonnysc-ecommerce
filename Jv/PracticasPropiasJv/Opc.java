class NPC {
    private int salud;
    private int poderdeataque;

    public NPC(int salud, int poderdeataque) {
        this.salud = salud;
        this.poderdeataque = poderdeataque;
    }

    public int getsalud() {
        return salud;
    }

    public void setsalud(int salud) {
        this.salud = salud;
    }

    public int getpoderdeataque() {
        return poderdeataque;
    }

    public void ataque(NPC target) {
        target.setsalud(target.getsalud() - this.poderdeataque);
        System.out.println(this + " ataca a " + target + " causando " + this.poderdeataque + " de daño");
    }

    public boolean isAlive() {
        return salud > 0;
    }

    public String toString() {
        return "NPC con " + salud + " puntos de salud y " + poderdeataque + " de poder de ataque";
    }
}

public class Opc {
    public static void main(String[] args) {
        NPC npc1 = new NPC(100, 20);
        NPC npc2 = new NPC(80, 25);

        System.out.println("Comienza la batalla entre " + npc1 + " y " + npc2);

        while (npc1.isAlive() && npc2.isAlive()) {
            npc1.ataque(npc2);
            if (npc2.isAlive()) {
                npc2.ataque(npc1);
            }
        }
        NPC ganador = npc1.isAlive() ? npc1 : npc2;
        NPC perdedor = npc1.isAlive() ? npc2 : npc1;
        System.out.println("La batalla ha terminado, el ganador es " + ganador + " y el perdedor es " + perdedor);
    }
}