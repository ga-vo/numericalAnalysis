public class NewtonsMethod {
	public NewtonsMethod() {
		
	}
	
	public double perform(Fun fun, Fun der,double p0, int iter, boolean verbose) {
		double pn=p0;
		for(int i=0; i <= iter;i++) {
			if(der.result(pn)!=0) {
				if(verbose) {
					System.out.println(""+i+" | pn:"+pn+" | fun(pn):"+fun.result(pn)+" | der(pn): "+ der.result(pn));
				}
				pn=pn-(fun.result(pn)/der.result(pn));
				
			}else {
				System.out.println("Error: Derivate of "+pn+" f equals 0");
			}
		}
		return pn; 
	}
}
