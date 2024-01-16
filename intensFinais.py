




#Taxa dos dados
valoresTaxas = []

print("########## ITENS FINAIS VENDA ########")

#Formulas de itens Finais Venda
subTotal = float(input("Valor Total Venda: "))



#Venda


percentualTaxaProdutora = float(input("percentualTaxaProdutora: ") or 30)
percentualBv1 = float(input("percentualBv1: ") or 10)
percentualBv2 = float(input("percentualBv2: ") or 0)
percentualBv3 = float(input("percentualBv3: ") or 0)
percentualConsultoria = float(input("percentualConsultoria: ") or 0)
percerntualComissao1 = float(input("percerntualComissao1: ") or 0)
percerntualComissao2 = float(input("percerntualComissao2: ") or 0)
percerntualComissao5 = float(input("percerntualComissao5: ") or 0)
percerntualComissao10 = float(input("percerntualComissao10: ") or 0)
percentualImposto = float(input("percentualImposto: ") or 21)
percentualParcialDiretoria = float(input("percentualParcialDiretoria: ") or 0)

taxaProdutora = float(subTotal * (percentualTaxaProdutora / 100))

totalOrcado = subTotal + taxaProdutora

difPerFaltante = abs((
    percentualBv1 + 
    percentualBv2 + 
    percentualBv3 + 
    percentualConsultoria + 
    percerntualComissao1 + 
    percerntualComissao2 + 
    percerntualComissao5 + 
    percerntualComissao10 + 
    percentualImposto +
    percentualParcialDiretoria) - 100) / 100

somaPercentualDespesa = abs(
    percentualBv1 + 
    percentualBv2 + 
    percentualBv3 +
    percentualConsultoria + 
    percerntualComissao1 + 
    percerntualComissao2 + 
    percerntualComissao5 + 
    percerntualComissao10 +
    percentualImposto + 
    percentualParcialDiretoria) / 100

valorPretendido = float(input("Valor Pretendido: ") or totalOrcado)

if valorPretendido == 0:
    total = totalOrcado
    txBvAgencia1 = (total / difPerFaltante) * (percentualBv1 / 100)
    txBvAgencia2 = (total / difPerFaltante) * (percentualBv2 / 100)
    txBvAgencia3 = (total / difPerFaltante) * (percentualBv3 / 100)
    txConsultoria = (total / difPerFaltante) * (percentualConsultoria / 100)
    txComissao1 = (total / difPerFaltante) * (percerntualComissao1 / 100)
    txComissao2 = (total / difPerFaltante) * (percerntualComissao2 / 100)
    txComissao5 = (total / difPerFaltante) * (percerntualComissao5 / 100)
    txComissao10 = (total / difPerFaltante) * (percerntualComissao10 / 100)
    txImposto = (total / difPerFaltante) * (percentualImposto / 100)
    txImpostoParcialDiretoria = (total / difPerFaltante) * (percentualParcialDiretoria / 100)
    
else:
    total = valorPretendido
    txBvAgencia1 = total * (percentualBv1 / 100)
    
    txBvAgencia1 = (total) * (percentualBv1 / 100)
    txBvAgencia2 = (total) * (percentualBv2 / 100)
    txBvAgencia3 = (total) * (percentualBv3 / 100)
    txConsultoria = (total) * (percentualConsultoria / 100)
    txComissao1 = (total) * (percerntualComissao1 / 100)
    txComissao2 = (total) * (percerntualComissao2 / 100)
    txComissao5 = (total) * (percerntualComissao5 / 100)
    txComissao10 = (total) * (percerntualComissao10 / 100)
    txImposto = (total) * (percentualImposto / 100)
    txImpostoParcialDiretoria = (total) * (percentualParcialDiretoria / 100)

somatoriaImpostos = (
    txBvAgencia1 +
    txBvAgencia1 +
    txBvAgencia2 +
    txBvAgencia3 +
    txConsultoria +
    txComissao1 +
    txComissao2 +
    txComissao5 +
    txComissao10 +
    txImposto +
    txImpostoParcialDiretoria)



somatoriaSemDesconto = totalOrcado + somatoriaImpostos



descontoFinanceiro = abs((valorPretendido) * (1 - somaPercentualDespesa) - totalOrcado)


#visualização

print("############ RESULTADOS ##############")

print("\n ############ SUBTOTAL ##############")

#subtotal
print("subTotal: " , subTotal)
print("somatoriaSemDesconto: " , somatoriaSemDesconto)
print("percentualTaxaProdutora: " , percentualTaxaProdutora)
print("descontoFinanceiro: " , descontoFinanceiro)

print("\n ############ PERCENTUAIS ##############")

#percentuais
print("percentualBv1: " , percentualBv1)
print("percentualBv2: " , percentualBv2)
print("percentualBv3: " , percentualBv3)
print("percentualConsultoria: " , percentualConsultoria)
print("percerntualComissao1: " , percerntualComissao1)
print("percerntualComissao2: " , percerntualComissao2)
print("percerntualComissao5: " , percerntualComissao5)
print("percerntualComissao10: " , percerntualComissao10)
print("percentualImposto: " , percentualImposto)
print("percentualParcialDiretoria: " , percentualParcialDiretoria)
print("valorPretendido: " , valorPretendido)

print("\n ######## TAXAS RESPECTIVAS ########")

#taxas Respectivas
print("txBvAgencia1: " , txBvAgencia1)
print("txBvAgencia2: " , txBvAgencia2)
print("txBvAgencia3: " , txBvAgencia3)
print("txConsultoria: " , txConsultoria)
print("txComissao1: " , txComissao1)
print("txComissao2: " , txComissao2)
print("txComissao5: " , txComissao5)
print("txComissao10: " , txComissao10)
print("txImposto: " , txImposto)
print("txImpostoParcialDiretoria: " , txImpostoParcialDiretoria)
print("totalOrcado: " , totalOrcado)
print("taxaProdutora: " , taxaProdutora)

print("######## FIM RESULTADOS VENDA ########")


