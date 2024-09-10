public class Polimorfismo2 {
    public static class Figura {
        private String nombre;
        public Figura(String nombre) {
            this.nombre = nombre;
        }
        public String getNombre() {
            return nombre;
        }
        public void setNombre(String nombre) {
            this.nombre = nombre;
        }
        public double calcularArea() {
            return 0.0;
        }
    }
    public static class Rectangulo extends Figura{
        private double largo;
        private double ancho;
        public Rectangulo(String nombre, double largo, double ancho){
            super(nombre);
            this.largo = largo;
            this.ancho = ancho;
        }
        public double getLargo(){
            return largo;
        }
        public void setLargo(double largo){
            this.largo = largo;
        }
        public double getAncho(){
            return ancho;
        }
        public void setAncho(double ancho){
            this.ancho = ancho;
        }
        @Override
        public double calcularArea(){
            return largo * ancho;
        }
    }
    public static class Circulo extends Figura {
        private double radio;
        public Circulo(String nombre, double radio){
            super(nombre);
            this.radio = radio;
        }
        public double getRadio(){
            return radio;
        }
        public void setRadio(double radio){
            this.radio = radio;
        }
        @Override
        public double calcularArea(){
            return Math.PI * Math.pow(radio, 2);
        }
    }
    public static class Triangulo extends Figura{
        private double base;
        private double altura;
        public Triangulo(String nombre, double base, double altura){
            super(nombre);
            this.base = base;
            this.altura = altura;
        }
        public double getBase(){
            return base;
        }
        public void setBase(double base){
            this.base = base;
        }
        public double getAltura(){
            return altura;
        }
        public void setAltura(double altura){
            this.altura = altura;
        }
        @Override
        public double calcularArea(){
            return ((base * altura) / 2);
        }
    }
    public static void main(String[] args) {
        Polimorfismo2.Rectangulo rectangulo = new Polimorfismo2.Rectangulo("Rectángulo", 10, 15);
        Polimorfismo2.Circulo circulo = new Polimorfismo2.Circulo("Círculo", 5);
        Polimorfismo2.Triangulo triangulo = new Polimorfismo2.Triangulo("Triángulo", 12, 3);
        Polimorfismo2.Figura[] figuras = {rectangulo, circulo, triangulo};
    
        System.out.println("INFORMACION DE LAS FIGURAS");
        System.out.println("==========================");
        for (Polimorfismo2.Figura figura : figuras){
            String formato = "El área del %-10s es: %.2f";
            System.out.println(String.format(formato, figura.getNombre(), figura.calcularArea()));
            System.out.println("===============================================");
        }
    }
}