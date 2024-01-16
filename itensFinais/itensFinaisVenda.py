
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


#Visualização Venda
print("############ RESULTADOS VENDA ##############")

#Subtotais Venda
print("\n ############ SUBTOTAL ##############")
print("difPerFaltante: " , difPerFaltante)
print("somatoriaSemDesconto: " , somatoriaSemDesconto)
print("percentualTaxaProdutora: " , percentualTaxaProdutora)
print("descontoFinanceiro: " , descontoFinanceiro)
print("subTotalCompra: ", subTotal)

#Percentuais
print("\n ############ PERCENTUAIS ##############")
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

#Taxas Respectivas
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


#Visualização Compra
print("############ RESULTADOS COMPRAS ##############")

#Subtotais Compra
print("\n ############ SUBTOTAL ##############")
print("somatoriaCompra: ", somatoriaCompra)
print("subTotalCompra: ", subTotalCompra)

#Percentuais
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

#Taxas Respectivas
print("\n ######## TAXAS RESPECTIVAS ########")
print("txBvAgencia1Compra: ", txBvAgencia1Compra)
print("txBvAgencia2Compra: ", txBvAgencia2Compra)
print("txBvAgencia3Compra: ", txBvAgencia3Compra)
print("txConsultoriaCompra: ", txConsultoriaCompra)
print("txComissao1Compra: ", txComissao1Compra)
print("txComissao2Compra: ", txComissao2Compra)
print("txComissao5Compra: ", txComissao5Compra)
print("txComissao10Compra: ", txComissao10Compra)
print("txImpostoCompra: ", txImpostoCompra)
print("txDirCompra: ", txDirCompra)


print("######## FIM RESULTADOS COMPRA ########")


#Margem Bruta Valor
margemBrutaValorCompraBvAgencia1 = float((txBvAgencia1 - txBvAgencia1Compra))
margemBrutaValorCompraBvAgencia2 = float((txBvAgencia2 - txBvAgencia2Compra))
margemBrutaValorCompraBvAgencia3 = float((txBvAgencia3 - txBvAgencia3Compra))
margemBrutaValorCompraConsultoria = float((txConsultoria - txConsultoriaCompra))
margemBrutaValorCompraComissao1 = float((txComissao1 - txComissao1Compra))
margemBrutaValorCompraComissao2 = float((txComissao2 - txComissao2Compra))
margemBrutaValorCompraComissao5 = float((txComissao5 - txComissao5Compra))
margemBrutaValorCompraComissao10 = float((txComissao10 - txComissao10Compra))
margemBrutaValorCompraImposto = float((txImposto - txImpostoCompra))
margemBrutaValorCompraParcialDiretoria = float((txImpostoParcialDiretoria - txDirCompra))
margemBrutaValorTotalCompra = float((somatoriaSemDesconto - somatoriaCompra))

#Margem Bruta Percentual

margemBrutaPercentualCompraBvAgencia1 = float((txBvAgencia1 / txBvAgencia1Compra) * 100)
margemBrutaPercentualCompraBvAgencia2 = float((txBvAgencia2 / txBvAgencia2Compra) * 100)
margemBrutaPercentualCompraBvAgencia3 = float((txBvAgencia3 / txBvAgencia3Compra) * 100)
margemBrutaPercentualCompraConsultoria = float((txConsultoria / txConsultoriaCompra) * 100)
margemBrutaPercentualCompraComissao1 = float((txComissao1 / txComissao1Compra) * 100)
margemBrutaPercentualCompraComissao2 = float((txComissao2 / txComissao2Compra) * 100)
margemBrutaPercentualCompraComissao5 = float((txComissao5 / txComissao5Compra) * 100)
margemBrutaPercentualCompraComissao10 = float((txComissao10 / txComissao10Compra) * 100)
margemBrutaPercentualCompraImposto = float((txImposto / txImpostoCompra) * 100)
margemBrutaPercentualCompraParcialDiretoria = float((txImpostoParcialDiretoria / txDirCompra) * 100)
margemBrutaPercentualTotalCompra = float((somatoriaSemDesconto / somatoriaCompra) * 100)


print("######## MARGEM BRUTA PERCENTUAL ########")

print("margemBrutaPercentualCompraBvAgencia1: ", margemBrutaPercentualCompraBvAgencia1)
print("margemBrutaPercentualCompraBvAgencia2: ", margemBrutaPercentualCompraBvAgencia2)
print("margemBrutaPercentualCompraBvAgencia3: ", margemBrutaPercentualCompraBvAgencia3)
print("margemBrutaPercentualCompraConsultoria: ", margemBrutaPercentualCompraConsultoria)
print("margemBrutaPercentualCompraComissao1: ", margemBrutaPercentualCompraComissao1)
print("margemBrutaPercentualCompraComissao2: ", margemBrutaPercentualCompraComissao2)
print("margemBrutaPercentualCompraComissao5: ", margemBrutaPercentualCompraComissao5)
print("margemBrutaPercentualCompraComissao10: ", margemBrutaPercentualCompraComissao10)
print("margemBrutaPercentualCompraImposto: ", margemBrutaPercentualCompraImposto)
print("margemBrutaPercentualCompraParcialDiretoria: ", margemBrutaPercentualCompraParcialDiretoria)
print("margemBrutaPercentualTotalCompra: ", margemBrutaPercentualTotalCompra)



print("######## MARGEM BRUTA VALOR ########")

print("margemBrutaValorCompraBvAgencia1: ", margemBrutaValorCompraBvAgencia1)
print("margemBrutaValorCompraBvAgencia2: ", margemBrutaValorCompraBvAgencia2)
print("margemBrutaValorCompraBvAgencia3: ", margemBrutaValorCompraBvAgencia3)
print("margemBrutaValorCompraConsultoria: ", margemBrutaValorCompraConsultoria)
print("margemBrutaValorCompraComissao1: ", margemBrutaValorCompraComissao1)
print("margemBrutaValorCompraComissao2: ", margemBrutaValorCompraComissao2)
print("margemBrutaValorCompraComissao5: ", margemBrutaValorCompraComissao5)
print("margemBrutaValorCompraComissao10: ", margemBrutaValorCompraComissao10)
print("margemBrutaValorCompraImposto: ", margemBrutaValorCompraImposto)
print("margemBrutaValorCompraParcialDiretoria: ", margemBrutaValorCompraParcialDiretoria)
print("margemBrutaValorTotalCompra: ", margemBrutaValorTotalCompra)


print("######## FIM MARGEM BRUTA ########")