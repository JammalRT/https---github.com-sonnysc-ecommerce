public class HorasExtra{
    public static class Empleado {
        private String nombre;
        private double sueldoPorHora;
        private int horasTrabajadas;
        public Empleado(String nombre, double sueldoPorHora, int horasTrabajadas) {
            this.nombre = nombre;
            this.sueldoPorHora = sueldoPorHora;
            this.horasTrabajadas = horasTrabajadas;
        }
        public String getNombre() {
            return nombre;
        }
        public void setNombre(String nombre) {
            this.nombre = nombre;
        }
        public double getSueldoPorHora() {
            return sueldoPorHora;
        }
        public void setSueldoPorHora(double sueldoPorHora) {
            this.sueldoPorHora = sueldoPorHora;
        }
        public int getHorasTrabajadas() {
            return horasTrabajadas;
        }
        public void setHorasTrabajadas(int horasTrabajadas) {
            this.horasTrabajadas = horasTrabajadas;
        }
        public double calcularSalarioSemanal() {
            double salarioSemanal = sueldoPorHora * horasTrabajadas;
            if (horasTrabajadas > 40) {
                int horasExtra = horasTrabajadas - 40;
                if (horasExtra <= 5) {
                    salarioSemanal += sueldoPorHora * horasExtra;
                } else if (horasExtra <= 45) {
                    salarioSemanal += sueldoPorHora * 5;
                    salarioSemanal += sueldoPorHora * 2 * (horasExtra - 5);
                } else {
                    salarioSemanal += sueldoPorHora * 5;
                    salarioSemanal += sueldoPorHora * 2 * 5;
                    salarioSemanal += sueldoPorHora * 3 * (horasExtra - 10);
                }
            }
            return salarioSemanal;
        }
    }
    public static class EmpleadoSinHorasExtra extends Empleado {
        public EmpleadoSinHorasExtra(String nombre, double sueldoPorHora, int horasTrabajadas) {
        super(nombre, sueldoPorHora, horasTrabajadas);
        }
        @Override
        public double calcularSalarioSemanal() {
            return getSueldoPorHora() * getHorasTrabajadas();
        }
    }
    public static class EmpleadoConHorasDobles extends Empleado {
        private int horasDobles;

        public EmpleadoConHorasDobles(String nombre, double sueldoPorHora, int horasTrabajadas, int horasDobles) {
            super(nombre, sueldoPorHora, horasTrabajadas);
            this.horasDobles = horasDobles;
        }
        public int getHorasDobles() {
            return horasDobles;
        }
        public void setHorasDobles(int horasDobles) {
            this.horasDobles = horasDobles;
        }
        @Override
        public double calcularSalarioSemanal() {
            double salarioSemanal = super.calcularSalarioSemanal();
            salarioSemanal += getSueldoPorHora() * 2 * horasDobles;
            return salarioSemanal;
        }
    }
    public static class EmpleadoConHorasTriple extends Empleado {
        private int horasTriples;
        public EmpleadoConHorasTriple(String nombre, double sueldoPorHora, int horasTrabajadas, int horasTriples) {
            super(nombre, sueldoPorHora, horasTrabajadas);
            this.horasTriples = horasTriples;
        }
        public int getHorasTriples() {
            return horasTriples;
        }
        public void setHorasTriples(int horasTriples) {
            this.horasTriples = horasTriples;
        }
        @Override
        public double calcularSalarioSemanal() {
            double salarioSemanal = super.calcularSalarioSemanal();
            salarioSemanal += getSueldoPorHora() * 3 * horasTriples;
            return salarioSemanal;
        }
    }
    public static void main(String[] args) {
        Empleado[] empleados = {
            new EmpleadoSinHorasExtra("Pedro", 13.0, 40),
            new EmpleadoConHorasTriple("Julian", 13.0, 50, 10),
            new EmpleadoConHorasDobles("Maria", 13.0, 45, 5)
        };
        for (Empleado empleado : empleados) {
            System.out.println("Nombre: " + empleado.getNombre());
            System.out.println("Sueldo por hora: $" + empleado.getSueldoPorHora());
            System.out.println("Horas trabajadas: " + empleado.getHorasTrabajadas());
            System.out.println("Salario semanal: $" + empleado.calcularSalarioSemanal());
            if (empleado instanceof EmpleadoConHorasTriple) {
                System.out.println("Horas Extras: " + ((EmpleadoConHorasTriple) empleado).getHorasTriples());
            } else if (empleado instanceof EmpleadoConHorasDobles) {
                System.out.println("Horas Extras: " + (((EmpleadoConHorasDobles) empleado).getHorasTrabajadas() > 40 ? ((EmpleadoConHorasDobles) empleado).getHorasTrabajadas() - 40 : 0));
            }
            System.out.println();
        }
    }
}