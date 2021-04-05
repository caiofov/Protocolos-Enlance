import simplex as simp

physical_layer=[]

msg = input("Insira sua mensagem: ")

sender = simp.Sender()
receiver = simp.Receiver()

sender.from_network_layer(msg)
sender.to_physical_layer()

receiver.from_physical_layer(physical_layer)
receiver.to_network_layer()

print("Os quadros recebidos foram: ")
for pacote in receiver.network_layer:
  print(pacote.info)