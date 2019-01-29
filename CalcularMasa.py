"""
Program that calculate the amount of solvent and ionic liquid need to prepare solutions of luminescent complexes.

Programa que calcula la cantidad de disolvente y de ionic liquid que necesitas para
preparar la disolución de complejo

"""


print(' Ionic Liquid used BMIM:PF6') #Muestra los datos del IL que usamos siempre
print('MolecularMass = 284.18 g/mol')
print('Solution 13 mg/ml acetonitrile')

PesoMolecularIL = 284.18           # los datos del IL que usamos siempre
ConcentracionDisolucionIL = 13

CambiarIL = input('Is correct IL dates?(y/n): ') #Pregunta para cambiar los datos de IL si quieres utilizar una diferente
if CambiarIL == "n":
    PesoMolecularIL = float(input('Insert Molecular Mass of the new IL(g/mol): '))
    ConcentracionDisolucionIL = float(input('Insert concentration of the IL solution(mg/ml): '))

print('   ')#Imprime los datos finales de IL
print('IL dates:')
print('MolecularMass =',PesoMolecularIL,'g/mol')
print('Solution concentration =',ConcentracionDisolucionIL,'mg/ml')
print('   ')


PesoMolecularComplejo = float(input('Insert molecular mass of the complex: ')) #Pide la masamolecular del complejo a usar
ConcentracionComplejo = 20    #Supone que 20 sera la concentracion de complejo
CambiarConcentracion = input('The complex solution concentration is 20 mg/ml?(y/n): ')#Pregunta si quieres usar una concentracion diferente
if CambiarConcentracion == 'n':
    ConcentracionComplejo = float(input('Insert complex solution concentration: '))
  
print('   ')    #Imprime los datos del complejo
print('Complex dates:')
print('MolecularMass =',PesoMolecularComplejo,'g/mol')
print('Solution concentration =',ConcentracionComplejo,'mg/ml')
print('   ')


RatioCIL = float(input('Insert Ratio Complex:IL (Ex for 4:1 insert 4): ')) #Calcula los milimoles de complejo e IL
MMolesMlComplejo = ConcentracionComplejo/PesoMolecularComplejo
MMolesMlIL = MMolesMlComplejo/RatioCIL

print('   ')                 
#print('milimoles complex/ml =',MMolesMlComplejo,'mmol/ml')
#print('milimoles IL/ml =',MMolesMlIL,'mmol/ml')
#print('   ')

MasaComplejo = float(input('Insert amount Complex weight (mg): '))
TotalDisolucion = MasaComplejo/ConcentracionComplejo
MMolesIL = TotalDisolucion*MMolesMlIL
MgramosIL = MMolesIL*PesoMolecularIL
MlIL = MgramosIL/ConcentracionDisolucionIL
VolumenFalta = TotalDisolucion - MlIL


print('Total disolution =',TotalDisolucion,'ml')
print('Quantity of IL = ',MlIL,'ml (',MlIL*1000,'ul)')
print('Add',VolumenFalta,'ml Acetonitrile (',VolumenFalta*1000,'ul)')



