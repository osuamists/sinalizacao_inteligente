# Sistema de Sinalização Inteligente

**Disciplina:** Sistemas Embarcados  
**Instituição:** [Nome da Instituição]  
**Data:** Janeiro 2026  
**Equipe:**

---

## 📋 Descrição do Projeto

Sistema embarcado baseado em **Raspberry Pi 4** rodando **Linux** que simula 
um semáforo inteligente com função de pedestre. O projeto demonstra controle 
de GPIO, máquina de estados e integração hardware-software.

## 🎯 Objetivos

- Implementar controle de GPIO em minicomputador
- Demonstrar diferença entre sistemas com OS vs bare-metal
- Integrar entrada digital (botão) e saídas digitais (LEDs)
- Aplicar boas práticas de desenvolvimento embarcado

## 🔧 Hardware Utilizado

| Componente | Quantidade | Especificação |
|------------|------------|---------------|
| Raspberry Pi 4 | 1 | 4GB RAM, ARM Cortex-A72 |
| LED Vermelho | 1 | 5mm, 2V @ 20mA |
| LED Amarelo | 1 | 5mm, 2V @ 20mA |
| LED Verde | 1 | 5mm, 2V @ 20mA |
| LED Azul | 1 | 5mm, 3.2V @ 20mA |
| Resistor 330Ω | 4 | 1/4W, 5% tolerância |
| Resistor 10kΩ | 1 | 1/4W, 5% tolerância |
| Push Button | 1 | Normalmente aberto |
| Protoboard | 1 | 830 pontos |
| Jumpers | 10 | Macho-Fêmea |

## 📐 Pinagem GPIO

- **GPIO 17 (pino 11)** → LED Vermelho
- **GPIO 27 (pino 13)** → LED Amarelo
- **GPIO 22 (pino 15)** → LED Verde
- **GPIO 23 (pino 16)** → LED Azul (Pedestre)
- **GPIO 24 (pino 18)** → Botão (com pull-down 10kΩ)

## 🚀 Como Executar

### Pré-requisitos

```bash
sudo apt update
sudo apt install python3 python3-pip python3-rpi.gpio -y
```

### Execução

```bash
cd codigo
sudo python3 semaforo.py
```

### Parar Sistema

Pressione `Ctrl+C` no terminal.

## 📊 Funcionalidades

### Modo Normal (Automático)
- **Verde:** 5 segundos
- **Amarelo:** 2 segundos
- **Vermelho:** 5 segundos
- Loop contínuo

### Modo Pedestre (Botão pressionado)
1. LED azul pisca 3x (confirmação)
2. Sistema completa ciclo atual
3. Vermelho permanece 8 segundos (tempo de travessia)
4. Retorna ao modo normal

## 📁 Estrutura do Repositório

```text
├── codigo/              # Scripts Python
├── hardware/            # Diagramas e fotos
├── documentacao/        # Relatório e apresentação
├── testes/              # Resultados e logs
└── referencias/         # Material de apoio
```

## 🧪 Testes Realizados

- [x] Teste individual de cada LED
- [x] Teste de leitura do botão
- [x] Ciclo automático (20 iterações)
- [x] Ciclo com pedestre (10 testes)
- [x] Teste de interrupção (Ctrl+C)
- [x] Teste de reboot do sistema

## 📚 Referências

- Raspberry Pi Foundation. GPIO Usage on Raspberry Pi. 2025.
- MONK, Simon. Programação com Arduino. Porto Alegre: Bookman, 2013.
- Sistemas Embarcados. Livro didático. 2018.
- ABNT NBR 14724:2024 - Trabalhos Acadêmicos.

## 📝 Licença

Este projeto é acadêmico e está sob licença MIT.
