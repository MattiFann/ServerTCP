#Piccolo server TCP multithreading

import socket
import threading
import sys

IP = '0.0.0.0'
PORT = 9998

def main():
    # Creazione del socket e setup iniziale
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        server.bind((IP, PORT)) #passo un indirizzo IP su cui voglio che il server sia in ascolto
        server.listen(5) #il server si mette in lista di contatti, accetta fino a un massimo di 5 connessioni
        
        print(f"--- SERVER DI [IL TUO NOME] ATTIVO ---")
        print(f'[*] In ascolto in {IP}:{PORT}')
        
        while True:
            client, address = server.accept() #appena un client si connette, immagazzina il socket client nella variabile client e i dettagli della connessione in address
            print(f'[+] Connessione riuscita | IP: {address[0]} Port: {address[1]}')
            
            client_handler = threading.Thread(target=handle_client, args=(client, address[0]))
            client_handler.start() #avvio il thread per occuparsi del dialogo con il client

    except KeyboardInterrupt:
        print("\n[!] Spegnimento del server...")
        server.close()
        sys.exit()

#questa funzione esegue recv() al suo interno e manda un messaggio di risposta al client
def handle_client(client_socket, ip_client):
    with client_socket as sock:
        try:
            request = sock.recv(1024)
            if request:
                messaggio = request.decode("utf-8")
                print(f'[*] Ricevuto da {ip_client}: {messaggio}')
                
                # Una risposta leggermente più completa dell'ACK standard
                sock.send(f"Ricevuto correttamente dal server di [IL TUO NOME]".encode("utf-8"))
        except Exception as e:
            print(f"[!] Errore durante la comunicazione: {e}")

if __name__ == '__main__':
    main()


#Autore: Mattia Fanni
#Scopo: progetto didattico per approfondire il networking in Python, nessuno scopo professionale
#Fonti: per lo sviluppo del codice mi sono aiutato con il libro BlackHat Python V2

#Come testarlo:
#1) Esegui il server: python nomeFile.py
#2) Utilizza un client (o uno strumento come netcat) per connetterti all'indirizzo 127.0.0.1 sulla porta 9998
#3) Il server stamperà il messaggio ricevuto e invierà una conferma personalizzata