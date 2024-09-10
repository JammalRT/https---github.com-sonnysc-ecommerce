import java.util.Random;
public class Batalla{
    //Clase del jugador 
    static public class Luchador{
        //Generador de los numeros aleatorios para el jugador 
        Random numAleatorio = new Random();
        int numram1 = numAleatorio.nextInt(100);
        private int vida;
        private int ataque;
        //Declarando los atributos del jugador
        public Luchador(int vida){
                this.vida = vida;
                this.ataque = numram1;
        }
    }
    //Clase del enemigo con herencia 
    static public class Karateca extends Luchador{
        //Generador de los numeros aleatorios para el enemigo
        Random numAleatorio = new Random();
        int numram2 = numAleatorio.nextInt(100);
        private static String nombre;
        private static int vida;
        private static int ataque;
        //Declarando los atributos del enemigo
        public Karateca(int vida, String nombre, String estilo){
            super(vida);
            this.nombre = nombre;
            this.vida = vida;
            this.ataque = numram2;
        }
    }  
    static public class Boxeador extends Luchador{
        //Generador de los numeros aleatorios para el enemigo
        Random numAleatorio = new Random();
        int numram2 = numAleatorio.nextInt(100);
        private static String nombre;
        private static int vida;
        private static int ataque;
        //Declarando los atributos del enemigo
        public Boxeador(int vida, String nombre, String estilo){
            super(vida);
            this.nombre = nombre;
            this.vida = vida;
            this.ataque = numram2;
        }   
    }
    //Inicia las simulacion de la batalla hasta que uno de los 2 llega a 0
    public static void main(String args[]){
        //Asiganamos los atributos a los persanajes 
        Luchador Sergio = new Karateca(100, "Sergio", "Karate");
        Luchador Kevin = new Boxeador(100, "Kevin", "Boxeo");
        System.out.println(Karateca.nombre + " se enfrenta a " + Boxeador.nombre);
        System.out.println("");
        //Mientras la vida de cualquiera de los 2 sea > 0 entonces segira repitiendo el bucle 
        while (Karateca.vida > 0 && Boxeador.vida > 0){
            int Player_Attack = Karateca.ataque;
            int Enemy_Attack = Boxeador.ataque;
            Karateca.vida -= Enemy_Attack;
            Boxeador.vida -= Player_Attack;
            System.out.println("");
            System.out.println(Karateca.nombre+" Ataca a Kevin y le quita " + Player_Attack + " puntos de vida");
            System.out.println("");
            System.out.println("=== Vida del Kevin ===");
            System.out.println(Boxeador.vida+"/100");
            System.out.println("");
            System.out.println(Boxeador.nombre+" Ataca a Sergio y le quita " + Enemy_Attack + " puntos de vida");
            System.out.println("");
            System.out.println("=== Vida del Sergio ===");
            System.out.println(Karateca.vida+"/100");
            //Si cualquira de los 2 llega a 0 entonces la simulacion termina e imprime el mensaje 
            if (Karateca.vida <= 0){
                System.out.println("");
                System.out.println("Sergio a sido derrotaro");
                System.out.println("");
            }
            else if (Boxeador.vida <= 0){
                System.out.println("");
                System.out.println("Kevin a sido derrotaro");
                System.out.println("");
            }
        }
    }
}