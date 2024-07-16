.data	
	next_line: .asciiz "\n"
	inp_statement: .asciiz "Enter length of first sequence: "
	inp_h_statement: .asciiz "Enter the length of second sequence: "
	inp_int_statement: .asciiz "Enter starting address of first seqeunce(x) inputs(in decimal format): "
	inp_h_int_statement: .asciiz "Enter starting address of second seqeunce(h) inputs(in decimal format): "
	out_int_statement: .asciiz "Enter starting address of outputs (in decimal format): "
	enter_int: .asciiz "Enter the integer: "
	#.align 2
	#array: .space 12
	
.text

#x length input
jal print_inp_statement 
jal input_int 
move $t1,$t4

#x address input
jal print_inp_int_statement
jal input_int
move $t2,$t4

#x sequence numbers input
move $t8,$t2
move $s7,$zero	#i = 0
loop1:  beq $s7,$t1,loop1end
	jal print_enter_int
	jal input_int
	sw $t4,0($t2)
	addi $t2,$t2,4
      	addi $s7,$s7,1
        j loop1      
loop1end: move $t2,$t8 

#h length input
jal print_inp_h_statement
jal input_int
move $t3,$t4

#h address input
jal print_inp_h_int_statement
jal input_int
move $t5,$t4

#h sequence numbers input 
move $t8,$t5
move $s7,$zero	#i = 0
loop2:  beq $s7,$t3,loop1end1
	jal print_enter_int
	jal input_int
	sw $t4,0($t5)
	addi $t5,$t5,4
      	addi $s7,$s7,1
        j loop2
loop1end1: move $t5,$t8 

#y address input
jal print_out_int_statement
jal input_int
move $t6,$t4
#############################################################################################################################
# t1 -> length 1; t2 -> x input add; t3 -> length 2; t5 -> h input add; t6 -> output add;

addi $t0,$t2,0 #x
addi $t4,$t5,0 #h
addi $t9,$t6,0 #y
add $s1,$t1,$t3
subi $s1,$s1,1
addi $t7,$0,0 #n=0
addi $t8,$0,0 #k=0
sll $t9,$t7,2
add $t9,$t9,$t6
sw $0,0($t9)
	
nloop:
	slt $s2,$t7,$s1 #n<l
	beq $s2,$0,done
	slt $s2,$t8,$t1 #k<l1
	bne $s2,$0,kloop #k<l1 -> inner loop
	addi $t7,$t7,1 #n = n + 1
	addi $t8,$0,0 #reset k
	sll $t9,$t7,2 #n*4
	add $t9,$t9,$t6 #n*4 + base address
	sw $0,0($t9) #y[n] = 0
	j nloop

kloop:
	sub $s2,$t7,$t8 #n-k
	addi $s3,$t3,0 
	slt $s3,$s3,$s2 #length 2 < n-k
	slti $s4,$s2,-1 #n-k < -1
	or $s3,$s3,$s4 
	addi $sp,$sp,-4
	sw $s2,0($sp)
	beq $s3,$0,yupdate #if (n-k)<l2 and (n-k)>-1
	addi $t8,$t8,1 #k = k+1
	addi $sp,$sp,4
	j nloop
	
yupdate:
	lw $s2,0($sp)
	sll $s2,$s2,2 
	add $s2,$s2,$t4
	lw $s3,0($s2) #h[n-k]
	sll $s2,$t8,2 
	add $s2,$s2,$t0
	lw $s4,0($s2) #x[k]
	mult $s3,$s4 #h[n-k]*x[k]
	mflo $s3
	lw $s2,0($t9) #y[n]
	add $s3,$s2,$s3 #y[n]=y[n]+x[k]*h[n-k]
	sw $s3,0($t9)
	addi $t8,$t8,1 #k = k+1
	addi $sp,$sp,4
	j nloop

done:

###############################################################################################################################
add $t1,$t1,$t3
subi $t1,$t1,1
move $s7,$zero	#i = 0
loop: beq $s7,$t1,end
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

print_inp_int_statement: li $v0,4
		la $a0,inp_int_statement
		syscall 
		jr $ra

print_inp_statement: li $v0,4
		la $a0,inp_statement
		syscall 
		jr $ra
print_inp_h_statement: li $v0,4
		la $a0,inp_h_statement
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
