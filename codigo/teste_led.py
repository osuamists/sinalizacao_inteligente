#!/usr/bin/env python3

"""
Teste individual de LEDs - Seminário 4
Verifica funcionamento de cada LED separadamente
"""

import RPi.GPIO as GPIO
import time
import sys

# Pinos dos LEDs (BCM)
LEDS = {
    'VERMELHO': 17,
    'AMARELO': 27,
    'VERDE': 22,
    'AZUL': 23
}

def testar_led(nome, pino):
    """Testa um LED específico"""   
    print(f"\n[TESTE] {nome} no GPIO {pino}")
    print("O LED deve piscar 3 vezes...")
    
    try:
        GPIO.setup(pino, GPIO.OUT)
        
        for i in range(3):
            GPIO.output(pino, GPIO.HIGH)
            print(f"  ✓ Piscada {i+1}/3")
            time.sleep(0.5)
            GPIO.output(pino, GPIO.LOW)
            time.sleep(0.5)
        
        resposta = input("LED funcionou corretamente? (s/n): ")
        return resposta.lower() == 's'
        
    except Exception as e:
        print(f"  ✗ ERRO: {e}")
        return False

def main():
    """Função principal"""
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    
    todos_corretos = True # Variável de controle para verificar se todos os LEDs funcionam corretamente
    
    for nome, pino in LEDS.items():
        if not testar_led(nome, pino):
            todos_corretos = False
            
    if todos_corretos:
        print("\nTodos os LEDs funcionam corretamente!")
    else:
        print("\nAlguns LEDs não funcionam corretamente.")
        
    GPIO.cleanup()
    
if __name__ == "__main__":
    main()