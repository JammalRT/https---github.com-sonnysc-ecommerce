public class P8{
    static public class Veiculo{
        String nPlaca, marca;
        int modelo;
        public Veiculo(String nPlaca, String marca, int modelo){
            this.nPlaca = nPlaca;
            this.modelo = modelo;
            this.marca = marca;
        }
        public String getnPlaca(){
            return nPlaca;
        }
        public String getMarca(){
            return marca;
        }
        public int getModelo(){
            return modelo;
        }
        public String mostrarInfo(){
            return "Placa: "+nPlaca+"\nMarca: "+marca+"\nModelo: "+modelo;
        }
    }
    static public class VeiculoDepotivo extends Veiculo{
        int cilindrada;
        public VeiculoDepotivo(String nPlaca, String marca, int modelo, int cilindrada){
            super(nPlaca, marca, modelo);
            this.cilindrada = cilindrada;
        }
        public int getCilindrada(){
            return cilindrada;
        }
        public String mostrarInfo(){
            return "Placa: "+nPlaca+"\nMarca: "+marca+"\nModelo: "+modelo+"\nCilindrada: "+cilindrada;
        }
    }
    static public class VeiculoTurismo extends Veiculo{
        int nPasajeros;
        public VeiculoTurismo(String nPlaca, String marca, int modelo, int nPasajeros){
            super(nPlaca, marca, modelo);
            this.nPasajeros = nPasajeros;
        }
        public int getnPasajeros(){
            return nPasajeros;
        }
        @Override
        public String mostrarInfo(){
            return "Placa: "+nPlaca+"\nMarca: "+marca+"\nModelo: "+modelo+"\nNumero de pasajeros: "+nPasajeros;
        }
    }
    public static void main(String[] args) {
        Veiculo misVeiculos[] = new Veiculo[3];
        misVeiculos[0] = new Veiculo("ADL34", "AUDI", 2023);
        misVeiculos[1] = new VeiculoDepotivo("FELD903", "FERRARI", 2019, 8);
        misVeiculos[2] = new VeiculoTurismo("DDCF903", "Toyota", 2020, 10);
        for(Veiculo veiculo: misVeiculos){
            System.out.println(veiculo.mostrarInfo());
            System.out.println("");
        }
    }
}