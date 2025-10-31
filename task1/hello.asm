; hello.asm — проста програма для DOS (.COM)
org 100h

section .text
    mov ah, 09h
    mov dx, msg
    int 21h

    mov ax, 4C00h
    int 21h

msg db 'Hello from NASM!', 13, 10, '$'
