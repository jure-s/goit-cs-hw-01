; calc.asm — проста програма для DOS (.COM)
; Обчислення суми двох однозначних чисел

org 100h

section .data
msg1 db 'Enter first digit (0-9): $'
msg2 db 13,10,'Enter second digit (0-9): $'
msg3 db 13,10,'Result = $'
newline db 13,10,'$'

section .text
start:
    ; --- Запит першого числа ---
    mov ah, 09h
    mov dx, msg1
    int 21h

    mov ah, 01h       ; зчитати символ з клавіатури
    int 21h
    sub al, '0'       ; перетворити ASCII в число (0–9)
    mov bl, al        ; зберегти перше число в BL

    ; --- Запит другого числа ---
    mov ah, 09h
    mov dx, msg2
    int 21h

    mov ah, 01h
    int 21h
    sub al, '0'
    add bl, al        ; BL = перше + друге
    mov bh, 0         ; очищаємо старший байт

    ; --- Вивід результату ---
    mov ah, 09h
    mov dx, msg3
    int 21h

    mov ax, bx
    add al, '0'       ; назад у ASCII
    mov dl, al
    mov ah, 02h       ; вивести символ у DL
    int 21h

    ; --- Перехід на новий рядок ---
    mov ah, 09h
    mov dx, newline
    int 21h

    ; --- Завершення програми ---
    mov ax, 4C00h
    int 21h
