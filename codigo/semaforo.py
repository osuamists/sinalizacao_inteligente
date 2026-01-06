#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
╔════════════════════════════════════════════════════════════╗
║  SEMINÁRIO 4 - SISTEMAS EMBARCADOS                         ║
║  Projeto: Sistema de Sinalização Inteligente               ║
║  Equipe: Suamí, Alexandre, Pedro                           ║
║  Hardware: Raspberry Pi 4 + GPIO                           ║
╚════════════════════════════════════════════════════════════╝
"""

import RPi.GPIO as GPIO
import time
import sys

# ═════════════════════════════════════════════════════════════
# CONFIGURAÇÃO DE HARDWARE
# ═════════════════════════════════════════════════════════════

# Pinos dos LEDs do semáforo (BCM)
LED_VERMELHO = 17  # Pino físico 11
LED_AMARELO = 27   # Pino físico 13
LED_VERDE = 22     # Pino físico 15
LED_PEDESTRE = 25  # Pino físico 16 (azul)

# Pino do botão de pedestre
BOTAO = 24         # Pino físico 18

# Tempos do semáforo (em segundos)
TEMPO_VERDE = 5
TEMPO_AMARELO = 2
TEMPO_VERMELHO = 5
TEMPO_VERMELHO_PEDESTRE = 8  # Tempo extra para travessia

# ═════════════════════════════════════════════════════════════
# INICIALIZAÇÃO DO GPIO
# ═════════════════════════════════════════════════════════════

def inicializar_gpio():
    """
    Configura os pinos GPIO do Raspberry Pi.
    
    Explicação técnica:
    - BCM: numeração dos pinos GPIO (não física)
    - OUT: pino configurado como saída (para LEDs)
    - IN: pino configurado como entrada (para botão)
    - pull_up_down: resistor interno de pull-down (evita leitura flutuante)
    """
    try:
        GPIO.setmode(GPIO.BCM)  # Usar numeração BCM
        GPIO.setwarnings(False)  # Desabilitar avisos de pinos já configurados
        
        # Configurar LEDs como saída
        GPIO.setup(LED_VERMELHO, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(LED_AMARELO, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(LED_VERDE, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(LED_PEDESTRE, GPIO.OUT, initial=GPIO.LOW)
        
        # Configurar botão como entrada com pull-down
        GPIO.setup(BOTAO, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        
        print("[OK] GPIO inicializado com sucesso")
        return True
        
    except Exception as e:
        print(f"[ERRO] Falha ao inicializar GPIO: {e}")
        return False

# ═════════════════════════════════════════════════════════════
# FUNÇÕES DE CONTROLE DOS LEDS
# ═════════════════════════════════════════════════════════════

def desligar_todos_leds():
    """Desliga todos os LEDs do sistema."""
    GPIO.output(LED_VERMELHO, GPIO.LOW)
    GPIO.output(LED_AMARELO, GPIO.LOW)
    GPIO.output(LED_VERDE, GPIO.LOW)
    GPIO.output(LED_PEDESTRE, GPIO.LOW)

def acender_led(led, tempo):
    """
    Acende um LED específico por determinado tempo.
    
    Args:
        led: número do GPIO do LED
        tempo: duração em segundos
    """
    desligar_todos_leds()
    GPIO.output(led, GPIO.HIGH)
    print(f"  → LED no GPIO {led} LIGADO por {tempo}s")
    time.sleep(tempo)

def piscar_led_pedestre():
    """
    Pisca LED azul 3 vezes para confirmar pedido do pedestre.
    
    Explicação: Feedback visual ao usuário indicando que
    o sistema registrou a solicitação de travessia.
    """
    print("  → Pedido de travessia registrado!")
    for i in range(3):
        GPIO.output(LED_PEDESTRE, GPIO.HIGH)
        time.sleep(0.3)
        GPIO.output(LED_PEDESTRE, GPIO.LOW)
        time.sleep(0.3)

# ═════════════════════════════════════════════════════════════
# FUNÇÃO PRINCIPAL DO SEMÁFORO
# ═════════════════════════════════════════════════════════════

def ciclo_semaforo_normal():
    """
    Executa um ciclo completo do semáforo no modo automático.
    
    Sequência: Verde → Amarelo → Vermelho
    """
    print("\n[CICLO NORMAL]")
    acender_led(LED_VERDE, TEMPO_VERDE)
    acender_led(LED_AMARELO, TEMPO_AMARELO)
    acender_led(LED_VERMELHO, TEMPO_VERMELHO)

def ciclo_semaforo_pedestre():
    """
    Executa ciclo especial quando pedestre solicita travessia.
    
    Diferença: Tempo de vermelho é estendido para permitir
    travessia segura do pedestre.
    """
    print("\n[CICLO PEDESTRE]")
    piscar_led_pedestre()
    acender_led(LED_VERDE, TEMPO_VERDE)
    acender_led(LED_AMARELO, TEMPO_AMARELO)
    acender_led(LED_VERMELHO, TEMPO_VERMELHO_PEDESTRE)
    GPIO.output(LED_PEDESTRE, GPIO.HIGH)  # Mantém LED azul aceso
    print("  → Pedestre pode atravessar!")
    time.sleep(TEMPO_VERMELHO_PEDESTRE)
    GPIO.output(LED_PEDESTRE, GPIO.LOW)

# ═════════════════════════════════════════════════════════════
# LOOP PRINCIPAL
# ═════════════════════════════════════════════════════════════

def main():
    """
    Função principal que gerencia o sistema embarcado.
    
    Lógica:
    1. Inicializa GPIO
    2. Loop infinito monitorando botão
    3. Executa ciclo apropriado (normal ou pedestre)
    4. Tratamento de interrupção (Ctrl+C)
    5. Limpeza de GPIO ao finalizar
    """
    
    # Banner de inicialização
    print("\n" + "═"*60)
    print("   SISTEMA DE SINALIZAÇÃO INTELIGENTE")
    print("   Raspberry Pi 4 - Linux Embarcado")
    print("═"*60)
    
    # Inicializar hardware
    if not inicializar_gpio():
        sys.exit(1)
    
    print("\n[SISTEMA ATIVO] Pressione Ctrl+C para encerrar")
    print("Aguardando solicitações de pedestre...\n")
    
    try:
        while True:
            # Verifica se botão foi pressionado
            if GPIO.input(BOTAO) == GPIO.HIGH:
                ciclo_semaforo_pedestre()
            else:
                ciclo_semaforo_normal()
                
    except KeyboardInterrupt:
        # Tratamento de interrupção pelo usuário
        print("\n\n[INFO] Sistema encerrado pelo usuário")
        
    except Exception as e:
        # Tratamento de erros inesperados
        print(f"\n[ERRO] Falha no sistema: {e}")
        
    finally:
        # Limpeza obrigatória do GPIO
        desligar_todos_leds()
        GPIO.cleanup()
        print("[OK] GPIO liberado. Sistema desligado com segurança.\n")

# ═════════════════════════════════════════════════════════════
# PONTO DE ENTRADA DO PROGRAMA
# ═════════════════════════════════════════════════════════════

if __name__ == "__main__":
    main()
