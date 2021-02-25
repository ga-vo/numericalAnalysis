function intgrl = composite_simpson_integration_rule(fun,a,b,N)
    if mod(N,2) ~= 0
        N=N+1;
    end
    h=(b-a)./N;
    intgrl=0;
    for k=1:M
        x_2k_2 = (a+(((2.*k)-2).*h));
        x_2k_1 = (a+(((2.*k)-1).*h));
        x_2k = (a+((2.*k).*h));
        intgrl = intgrl + fun(x_2k_2)+(4*fun(x_2k_1))+(fun(x_2k));
    end
    intgrl=intgrl.*(h./3);
end
