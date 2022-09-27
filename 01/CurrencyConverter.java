package homework;

public class CurrencyConverter {
	static double dollarToReal(double quantidade, double preco){
        double converter = quantidade * (preco + (preco * 0.06));
        return converter;

}
}
