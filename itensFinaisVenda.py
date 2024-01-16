#Taxa dos dados
valoresTaxas = []

print("########## ITENS FINAIS VENDA ########")

#Formulas de itens Finais Venda
subTotal = float(input("Valor Total Venda: "))

#VENDA
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

difPerFaltante = abs(((
    percentualBv1 + 
    percentualBv2 + 
    percentualBv3 + 
    percentualConsultoria + 
    percerntualComissao1 + 
    percerntualComissao2 + 
    percerntualComissao5 + 
    percerntualComissao10 + 
    percentualImposto +
    percentualParcialDiretoria) - 100) / 100)

somaPercentualDespesa = abs((
    percentualBv1 + 
    percentualBv2 + 
    percentualBv3 +
    percentualConsultoria + 
    percerntualComissao1 + 
    percerntualComissao2 + 
    percerntualComissao5 + 
    percerntualComissao10 +
    percentualImposto + 
    percentualParcialDiretoria) / 100)

valorPretendido = float(input("Valor Pretendido: ") or 0)

if valorPretendido == 0 or valorPretendido == None:
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
    print(txBvAgencia1)
    
else:
    total = valorPretendido
    txBvAgencia1 = (total) * (percentualBv1 / 100)
    
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


#visualização Venda
print("############ RESULTADOS VENDAS ##############")

print("\n ############ SUBTOTAL ##############")

#subtotal
print("subTotal: " , subTotal)
print("difPerFaltante: " , difPerFaltante)
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

print("\n######## INÍCIO RESULTADOS COMPRA ########")

#COMPRA
subTotalCompra = float(input("SubTotalCompra: "))

percentualBv1Compra = float(input("percentualBv1Compra: ") or 10)
percentualBv2Compra = float(input("percentualBv2Compra: ") or 0)
percentualBv3Compra = float(input("percentualBv3Compra: ") or 0)
percentualConsultoriaCompra = float(input("percentualConsultoriaCompra: ") or 0)
percerntualComissao1Compra = float(input("percerntualComissao1Compra: ") or 1)
percerntualComissao2Compra = float(input("percerntualComissao2Compra: ") or 2)
percerntualComissao5Compra = float(input("percerntualComissao5Compra: ") or 5)
percerntualComissao10Compra = float(input("percerntualComissao10Compra: ") or 10)
percentualImpostoCompra = float(input("percentualImpostoCompra: ") or 21)
percentualParcialDiretoriaCompra = float(input("percentualParcialDiretoriaCompra: ") or 2.5)


txBvAgencia1Compra = float(somatoriaSemDesconto * (percentualBv1Compra/100))
txBvAgencia2Compra = float(somatoriaSemDesconto * (percentualBv2Compra/100))
txBvAgencia3Compra = float(somatoriaSemDesconto * (percentualBv3Compra/100))

txImpostoCompra = float(somatoriaSemDesconto * (percentualImpostoCompra/100))

txConsultoriaCompra = float(somatoriaSemDesconto - txImpostoCompra - txBvAgencia1Compra - txBvAgencia2Compra - txBvAgencia3Compra * (percentualConsultoriaCompra/100))

txComissao5Compra = float(somatoriaSemDesconto - txImpostoCompra - txBvAgencia1Compra - txBvAgencia2Compra - txBvAgencia3Compra * (percerntualComissao5Compra/100))
txComissao1Compra = float(somatoriaSemDesconto - txBvAgencia1Compra - txBvAgencia2Compra - txBvAgencia3Compra - txComissao5Compra - txConsultoriaCompra * (percerntualComissao1Compra/100))
txComissao2Compra = float(somatoriaSemDesconto - txBvAgencia1Compra - txBvAgencia2Compra - txBvAgencia3Compra - txComissao5Compra - txConsultoriaCompra - txComissao1Compra * (percerntualComissao2Compra/100))
txComissao10Compra = float(somatoriaSemDesconto - txBvAgencia1Compra - txBvAgencia2Compra - txBvAgencia3Compra * (percerntualComissao10Compra/100))

somaDespesaDir = float(
    txBvAgencia1Compra +
    txBvAgencia2Compra +
    txBvAgencia3Compra + 
    txConsultoriaCompra +
    txComissao1Compra + 
    txComissao2Compra + 
    txComissao5Compra + 
    txComissao10Compra +
    txImpostoCompra
)

txDirCompra = float((somatoriaSemDesconto - subTotalCompra - somaDespesaDir) * (percentualParcialDiretoriaCompra/100))

somatoriaCompra = (
    subTotalCompra +
    txBvAgencia1Compra + 
    txBvAgencia2Compra + 
    txBvAgencia3Compra + 
    txConsultoriaCompra + 
    txComissao1Compra + 
    txComissao2Compra + 
    txComissao5Compra + 
    txComissao10Compra + 
    txImpostoCompra + 
    txDirCompra
)


#visualização Compra
print("############ RESULTADOS COMPRAS ##############")

#subtotal
print("\n ############ SUBTOTAL ##############")
print("somatoriaCompra: ", somatoriaCompra)
print("subTotalCompra: ", subTotalCompra)


#percentuais
print("\n ############ PERCENTUAIS ##############")
print("percentualBvAgencia1Compra: ", percentualBv1Compra)
print("percentualBvAgencia2Compra: ", percentualBv2Compra)
print("percentualBvAgencia3Compra: ", percentualBv3Compra)
print("percentualConsultoriaCompra: ", percentualConsultoriaCompra)
print("percentualNca1Compra: ", percerntualComissao1Compra)
print("percentualNca2Compra: ", percerntualComissao2Compra)
print("percentalNca5Compra: ", percerntualComissao5Compra)
print("percentualNca10: ", percerntualComissao10Compra)
print("percentualImpostoCompra: ", percentualImpostoCompra)
print("percentualParcialDiretoriaCompra: ", percentualParcialDiretoriaCompra)

#taxas Respectivas
print("\n ######## TAXAS RESPECTIVAS ########")
print("txBvAgencia1Compra: ", txBvAgencia1Compra)
print("txBvAgencia2Compra: ", txBvAgencia2Compra)
print("txBvAgencia3Compra: ", txBvAgencia3Compra)
print("txConsultoria: ", txConsultoria)
print("txComissao1Compra: ", txComissao1Compra)
print("txComissao2Compra: ", txComissao2Compra)
print("txComissao5Compra: ", txComissao5Compra)
print("txComissao10Compra: ", txComissao10Compra)
print("txImpostoCompra: ", txImpostoCompra)
print("txDirCompra: ", txDirCompra)


print("######## FIM RESULTADOS COMPRA ########")