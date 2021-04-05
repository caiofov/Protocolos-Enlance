import sw_ruido as swr
import ../protocol as ptc
import time

def interferencia(physical_layer): #interferencia para testes
  physical_layer.pop()

physical_layer=[]

sender = swr.Sender()
receiver = swr.Receiver()

while True:
  msg = input("Mensagem: ")
  
  sender.from_network_layer(msg)
  sender.to_physical_layer(physical_layer)

  #interferencia(physical_layer)

  receiver.from_physical_layer(physical_layer)
  receiver.to_physical_layer(physical_layer)

  #time.sleep(10)

  #enquanto um quadro não for aceito ou o timer não expirar ou um quadro errado não chegar, o sender tentará buscar o quadro de confirmação correto
  while(sender.set_timer() and not sender.event == ptc.eventType.frame_arrival and not sender.event == ptc.eventType.cksum_err):
    sender.from_physical_layer(physical_layer)
    #se por acaso o quadro correto chegar (frame_arrival) ou o timer expirar (set_timer = False) ou chegar um quadro errado (cksum_err), irá sair do loop
  
  #caso o sender receba o quadro errado ou o timer expirar
  while (sender.event == ptc.eventType.cksum_err or sender.event == ptc.eventType.timeout):
    
    sender.to_physical_layer(physical_layer) #reenvia o último quadro
    
    receiver.from_physical_layer(physical_layer) #recebe
    receiver.to_physical_layer(physical_layer) #envia o quadro de confirmação
    
    # o mesmo loop anterior: espera até receber o quadro correto
    while(sender.set_timer() and not sender.event == ptc.eventType.frame_arrival and not sender.event == ptc.eventType.cksum_err): 
      sender.from_physical_layer(physical_layer)

  
  #neviar para a camada de rede caso o quadro tenha sido recebido com sucesso
  if(receiver.event == ptc.eventType.frame_arrival):
    receiver.to_network_layer()