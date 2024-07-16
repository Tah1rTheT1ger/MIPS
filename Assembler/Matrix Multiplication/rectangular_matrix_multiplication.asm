.data	
	next_line: .asciiz "\n"
	inp_st: .asciiz "Enter order of matrices m*n  p*q"
	inp_statement: .asciiz "Enter the value of m: "
	inp_n_statement: .asciiz "Enter the value of n: "
	inp_q_statement: .asciiz "Enter the value of q: "
	inp_p_statement: .asciiz "Enter the value of p: "
	out_statement: .asciiz "Matrices cannot be multiplied"
	inp_int_statement: .asciiz "Enter starting address of first matrix inputs(in decimal format): "
	inp_h_int_statement: .asciiz "Enter starting address of second matrix inputs(in decimal format): "
	out_int_statement: .asciiz "Enter starting address of output matrix (in decimal format): "
	enter_int: .asciiz "Enter the integer: "
	#.align 2
	#array: .space 12
	
.text
jal print_in_st
jal print_line

jal print_inp_statement
jal input_int 
move $t1,$t4 #t1 -> m

jal print_inp_n_statement
jal input_int 
move $s1,$t4 #s1 -> n

jal print_inp_p_statement
jal input_int 
move $s2,$t4 #s2 -> p

bne $s1,$s2,exit

jal print_inp_q_statement
jal input_int 
move $s2,$t4 #s2 -> q

jal print_inp_int_statement
jal input_int
move $t2,$t4 #t2 -> x1

move $t8,$t2
move $s7,$zero	#i = 0
mult $t1,$s1
mflo $t0
loop1:  beq $s7,$t0,loop1end
	jal print_enter_int
	jal input_int
	sw $t4,0($t2)
	addi $t2,$t2,4
      	addi $s7,$s7,1
        j loop1      
loop1end: move $t2,$t8 

jal print_inp_h_int_statement
jal input_int
move $t5,$t4 #t5 -> x2

move $t8,$t5
move $s7,$zero #i = 0
mult $s1,$s2
mflo $t0 
loop2:  beq $s7,$t0,loop1end1
	jal print_enter_int
	jal input_int
	sw $t4,0($t5)
	addi $t5,$t5,4
      	addi $s7,$s7,1
        j loop2
loop1end1: move $t5,$t8 

jal print_out_int_statement
jal input_int
move $t6,$t4 #t6 -> y
#############################################################################################################################################################################
# t1 -> m; t2 -> x1 add; t5 -> x2 add; t6 -> y add; s1 -> n; s2 -> q
addi $t0,$0,0 #i
addi $t3,$0,0 #j
addi $t4,$0,0 #k
mult $t0,$s2 #i*q
mflo $t9 
add $t9,$t9,$t3 #i*q+j
sll $t9,$t9,2 #(i*q+j)*4
add $t9,$t9,$t6 #(i*q+j)*4 + base address
sw $0,0($t9)
	
iloop:
	slt $t8,$t0,$t1 #i < m
	beq $t8,$0,done
	slt $t8,$t3,$s2 #j < q
	bne $t8,$0,jloop
	addi $t0,$t0,1
	addi $t3,$0,0
	j iloop
	
jloop:
	slt $t8,$t4,$s1 
	bne $t8,$0,kloop
	addi $t3,$t3,1
	mult $t0,$s2 #i*q
	mflo $t9 
	add $t9,$t9,$t3 #i*q+j
	sll $t9,$t9,2 #(i*q+j)*4
	add $t9,$t9,$t6 #(i*q+j)*4 + base address
	sw $0,0($t9)
	addi $t4,$0,0
	j iloop
	
kloop:
	mult $t0,$s1
	mflo $t8
	add $t8,$t8,$t4
	sll $t8,$t8,2
	add $t8,$t8,$t2
	lw $t8,0($t8)
	mult $t4,$s2
	mflo $t7
	add $t7,$t7,$t3
	sll $t7,$t7,2
	add $t7,$t7,$t5
	lw $t7,0($t7)
	mult $t7,$t8
	mflo $t8
	lw $t7,0($t9)
	add $t7,$t7,$t8
	sw $t7,0($t9)
	addi $t4,$t4,1
	j jloop
	
done:

#############################################################################################################################################################################
mult $t1,$s2
mflo $t0
move $s7,$zero	#i = 0
loop: beq $s7,$t0,end
      lw $t4,0($t6)
      jal print_int
      jal print_line
      addi $t6,$t6,4
      addi $s7,$s7,1
      j loop 
#end
end:  li $v0,10
      syscall

input_int: li $v0,5
	   syscall
	   move $t4,$v0
	   jr $ra

print_int: li $v0,1	
	   move $a0,$t4
	   syscall
	   jr $ra
#print nextline
print_line:li $v0,4
	   la $a0,next_line
	   syscall
	   jr $ra

print_in_st:li $v0,4
	   la $a0,inp_st
	   syscall
	   jr $ra

print_inp_int_statement: li $v0,4
		la $a0,inp_int_statement
		syscall 
		jr $ra

print_inp_statement: li $v0,4
		la $a0,inp_statement
		syscall 
		jr $ra

print_inp_n_statement: li $v0,4
		la $a0,inp_n_statement
		syscall 
		jr $ra

print_inp_q_statement: li $v0,4
		la $a0,inp_q_statement
		syscall 
		jr $ra

print_inp_p_statement: li $v0,4
		la $a0,inp_p_statement
		syscall 
		jr $ra

print_inp_h_int_statement: li $v0,4
		la $a0,inp_h_int_statement
		syscall 
		jr $ra

#print output address statement
print_out_int_statement: li $v0,4
		la $a0,out_int_statement
		syscall 
		jr $ra
#print enter integer statement
print_enter_int: li $v0,4
		la $a0,enter_int
		syscall 
		jr $ra

exit: 
	li $v0,4
	la $a0,out_statement
	syscall
	