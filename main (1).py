print("escolha qual operação voce deseja entre 1 a 4 sabendo que f(x)= 2X+1 e g(x)= 2x+3")
print(" 1 = (g º f)")
print(" 2 = (g º g)")
print(" 3 = (f º f)")
print(" 4 = (f º g)")
operacao = int(input("digite a operação:"))
x = int(input("digite o valor de x:"))



resultado_gof = 2*(2*x+1)+3
resultado_gog = 2*(2*x+3)+3
resultado_fof = 2*(2*x+1)+1
resultado_fog = 2*(2*x+3)+1

if operacao == 1:
  print(f"(g ° f)(x) = {resultado_gof}")
elif operacao == 2:
  print(f"(g ° g)(x) = {resultado_gog}")
elif operacao == 3:
  print(f"(f ° f)(x) = {resultado_fof}")
elif operacao == 4:
  print(f"(f ° g)(x) = {resultado_fog}")
else:
  print("opçao invalida")

#