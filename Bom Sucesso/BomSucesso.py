import sys
sys.path.append('C:/Users/melol/Documents/Projeto MVP/mvpowerboth/MVpowerBOTH/Bom Sucesso/Leitura')
sys.path.append('C:/Users/melol/Documents/Projeto MVP/mvpowerboth/MVpowerBOTH/Bom Sucesso/Envio')                
import LeituraDados
import EnvioInversores

id=1
inversorLinha1 = []
vetorInversores ={}

#vetorLinha1[j] = inversorLinha1 

inversorLinha1 = LeituraDados.run_sync_dados(id,'/dev/ttyUSB0',5000,76) 
vetorInversores.update(inversorLinha1)

EnvioInversores.envio_Inversores(vetorInversores)

