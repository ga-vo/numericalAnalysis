package numericalIntegration;

public class Integral {
	private Fun fun;
	private double a, b;

	public Integral(Fun fun, double a, double b) {
		this.fun = fun;
		this.a = a;
		this.b = b;
	}

	public double[] getLimits() {
		double[] limits = { a, b };
		return limits;
	}

	public void setParams(Fun fun, double a, double b) {
		this.fun = fun;
		this.a = a;
		this.b = b;
	}

	public double trapezoidal_rule(int N) {
		double x_k_1, x_k, h, intgrl;
		h = (b - a) / N;
		intgrl = 0;
		x_k = a;
		for (int i = 1; i <= N; i++) {
			x_k_1 = x_k;
			x_k += h;
			intgrl += fun.result(x_k_1) + fun.result(x_k);
		}
		intgrl *= h / 2;

		return intgrl;
	}

	public double componsite_simpson(int N) {
		double x_2k_2, x_2k_1, x_2k, h, intgrl;

		h = (b - a) / N;
		intgrl = 0;

		for (int k = 1; k < (N / 2); k++) {
			x_2k_2 = a + ((2 * k) - 2) * h;
			x_2k_1 = a + ((2 * k) - 1) * h;
			x_2k = a + (2 * k) * h;

			intgrl += fun.result(x_2k_2) + 4 * fun.result(x_2k_1) + fun.result(x_2k);
		}

		intgrl = intgrl * h / 3;
		return intgrl;
	}

	public double composite_simpson_3_8(int N) {
		double h, intgrl, x_k, x_3k;
		h = (b - a) / N;
		intgrl = fun.result(a);
		x_k = a;

		for (int k = 1; k < N; k++) {
			if (k % 3 != 0) {
				x_k = a + k * h;
				intgrl += 3 * fun.result(x_k);
			}
		}

		for (int k = 1; k < N / 3; k++) {
			x_3k = a + (3 * k * h);
			intgrl += 2 * fun.result(x_3k);
		}
		x_k = b;
		intgrl += fun.result(x_k);
		intgrl *= 3 * h / 8;
		intgrl = Math.round(intgrl * Math.pow(10, 9)) / Math.pow(10, 9);
		return intgrl;
	}
}
