function intgrl = composite_simpson_3_8_integration_rule(fun,a,b,N)
    while mod(N,3) ~= 0
        N=N+1;
    end
    h=(b-a)./N;
    intgrl=fun(a);
    for k=1:M-1
        if mod(N,3) ~= 0
            x_k=a + k.*h;
            intgrl = intgrl + 3.*fun(x_k);
        end
    end
    for k=1:(M./3)-1
        x_3k= a + (3.*k.*h);
        intgrl = intgrl + 2.*fun(x_3k);
    end
    intgrl = intgrl + fun(b);
    intgrl=intgrl.*(3.*h./8);
end
