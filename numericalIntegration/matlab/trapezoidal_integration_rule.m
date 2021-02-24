function intgrl = trapezoidal_integration_rule(fun,a,b,N)
    dx=(b-a)./N;
    intgrl=0;
    for k=1:M
        x_k_1=x_k;
        x_k=x_k+dx;
        intgrl=intgrl + (fun(x_k1)+fun(x_k));
    end
    intgrl=intgrl.*(h./2);
end
