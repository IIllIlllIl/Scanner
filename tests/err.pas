begin
  integer k01234567890123456789;
  integer function F(n);
    begin
      integer n;
      if n<=0 then F:=1
      else $F:n*F(n-1)
    end;
  read(m);
  k:=F(m);
  write(k)
end