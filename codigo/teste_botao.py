import RPi.GPIO as GPIO
import time

BOTAO = 24
LED_INDICADOR = 23  # LED azul como indicador visual

def main():
    print("="*60) 
    print("  TESTE DE BOTÃO")
    print("="*60)
    print("Pressione o botão para testar...")
    print("Ctrl+C para sair\n")
    
    GPIO.setmode(GPIO.BCM) # Configura o modo BCM(Broadcom)
    GPIO.setwarnings(False) # Desabilita alertas
    GPIO.setup(BOTAO, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(LED_INDICADOR, GPIO.OUT)
    
    contador = 0 # Contador de acionamentos
    estado_anterior = GPIO.LOW # Estado anterior do botão
    
    try:
        while True: 
            estado_atual = GPIO.input(BOTAO)
            
            # Detecta borda de subida (pressionado)
            if estado_atual == GPIO.HIGH and estado_anterior == GPIO.LOW:
                contador += 1
                GPIO.output(LED_INDICADOR, GPIO.HIGH)
                print(f"[{contador:03d}] Botão PRESSIONADO - GPIO leu: HIGH (3.3V)")
            
            # Detecta borda de descida (solto)
            elif estado_atual == GPIO.LOW and estado_anterior == GPIO.HIGH:
                GPIO.output(LED_INDICADOR, GPIO.LOW)
                print(f"      Botão SOLTO - GPIO leu: LOW (0V)")
            
            estado_anterior = estado_atual
            time.sleep(0.05)  # 50ms de polling
            
    except KeyboardInterrupt: 
        print(f"\n\nTotal de acionamentos: {contador}")
    
    finally: 
        GPIO.cleanup()
        print("[OK] GPIO limpo\n")

if __name__ == "__main__": 
    main()