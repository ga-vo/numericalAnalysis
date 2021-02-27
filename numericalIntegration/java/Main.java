package numericalIntegration;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Integral intg = new Integral(x -> (Math.pow(x, 2) + 12 * x + 2), 0, 5);

		System.out.println(intg.composite_simpson_3_8(360));

		intg.setParams(x -> Math.exp(x), 1, 5);

		System.out.println(intg.composite_simpson_3_8(360));

	}

}
