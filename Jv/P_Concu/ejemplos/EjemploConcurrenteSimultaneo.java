package ejemplos;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

public class EjemploConcurrenteSimultaneo {

    public static void main(String[] args) {
        // Crear un ExecutorService con un pool fijo de 2 hilos
        ExecutorService executorService = Executors.newFixedThreadPool(2);

        // Crear y enviar la tarea de imprimir números del 1 al 100
        Runnable imprimirNumeros = () -> {
            for (int i = 1; i <= 100; i++) {
                System.out.println("Número: " + i);
                try {
                    Thread.sleep(50); // Pausa para simular trabajo
                } catch (InterruptedException e) {
                    Thread.currentThread().interrupt();
                }
            }
        };

        // Crear y enviar la tarea de imprimir una lista de 20 palabras
        Runnable imprimirPalabras = () -> {
            String[] palabras = {
                "Java", "Concurrente", "Ejemplo", "Hilo", "Ejecución",
                "Código", "Programa", "Palabra", "Impresión", "Tarea",
                "Simultáneo", "Runnable", "ExecutorService", "Pool", "Thread",
                "Proceso", "Número", "Lista", "Paralelo", "Concurrencia"
            };

            for (String palabra : palabras) {
                System.out.println("Palabra: " + palabra);
                try {
                    Thread.sleep(150); // Pausa para simular trabajo
                } catch (InterruptedException e) {
                    Thread.currentThread().interrupt();
                }
            }
        };

        // Ejecutar ambas tareas concurrentemente
        executorService.submit(imprimirNumeros);
        executorService.submit(imprimirPalabras);

        // Solicitar el apagado del ExecutorService
        executorService.shutdown();
    }
}