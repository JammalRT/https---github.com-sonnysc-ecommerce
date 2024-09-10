package ejemplos;

// Clase que implementa la interfaz Runnable para crear una tarea concurrente
class Contador implements Runnable {
    private String nombre;
    private int max;

    public Contador(String nombre, int max) {
        this.nombre = nombre;

        this.max = max;
    }

    // Método run que define la tarea que se ejecutará concurrentemente
    @Override
    public void run() {
        for (int i = 1; i <= max; i++) {
            System.out.println(nombre + " contador: " + i);
            try {
                // Simula una pausa para demostrar la concurrencia
                Thread.sleep(1500);
            } catch (InterruptedException e) {
                System.out.println(nombre + " interrumpido.");
            }
        }
        System.out.println(nombre + " terminado.");
    }
}

public class EjemploConcurrente {
    public static void main(String[] args) {
        // Crear dos instancias de Contador
        Contador contador1 = new Contador("Hilo 1", 5);
        Contador contador2 = new Contador("Hilo 2", 5);

        // Crear dos hilos para ejecutar las tareas concurrentemente
        Thread hilo1 = new Thread(contador1);
        Thread hilo2 = new Thread(contador2);

        // Iniciar los hilos
        hilo1.start();
        hilo2.start();

        // Esperar a que ambos hilos terminen
        try {
            hilo1.join();
            hilo2.join();
        } catch (InterruptedException e) {
            System.out.println("Hilo principal interrumpido.");
        }

        System.out.println("Programa principal terminado.");
    }
}