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


