function [r]=newtons_Methodfun,der,p0,iter,verbose,graph)
    pn=p0;
    for i=0:iter
        if(~der(pn)==0)
            if(verbose)
                fprintf('\n %i | p_n: %5.5f  | fun(p_n): %5.5f  | der(p_n): %5.5f ',i,pn,fun(pn),der(pn));
            end
            if(graph)
                ps(i+1)=pn;
            end
            pn=pn-(fun(pn)./der(pn));
            
        else
            fprintf('/n Error: Derivate of %10.10f equals 0',pn);
        end
    end
    r=pn;
    if (graph)
        mi=min(ps)-3;
        ma=max(ps)+3;
        x=mi:0.00001:ma;
        y=fun(x);
        y2=fun(ps);
        plot(x,y,'b-');
        hold on;
        plot(ps,y2,'g:+');
        plot(r,fun(r),'r*');
        xlim([mi-0.5,ma+0.5])
        legend('Function','X_{k}','Root','Location','southwest');
    end
end
