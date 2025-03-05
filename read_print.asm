section .bss ; made by chatpgt
    num resb 10       ; Reserve space for the input number (up to 10 characters)

section .text
    global _start

_start:
    ; Read the number from stdin
    mov rsi, num      ; Address of the buffer to store the input
    mov rdx, 10       ; Maximum number of bytes to read
    mov rax, 0        ; syscall number for sys_read (0)
    mov rdi, 0        ; File descriptor for stdin
    syscall

    ; Print the number to stdout
    mov rsi, num      ; Address of the buffer with the input number
    mov rdx, 10       ; Maximum number of bytes to write
    mov rax, 1        ; syscall number for sys_write (1)
    mov rdi, 1        ; File descriptor for stdout
    syscall

    ; Exit the program
    mov rax, 60       ; syscall number for sys_exit (60)
    xor rdi, rdi      ; Exit code 0
    syscall
