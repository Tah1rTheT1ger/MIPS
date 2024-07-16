# t1 -> m; t2 -> x1 add; t5 -> x2 add; t6 -> y add; s1 -> n; s2 -> q

addi $t0,$0,0 #i
addi $t3,$0,0 #j
addi $t4,$0,0 #k
mult $t0,$s2 #i*q
mflo $t9 
add $t9,$t9,$t3 #i*q+j
sll $t9,$t9,2 #(i*q+j)*4
add $t9,$t9,$t6 #(i*q+j)*4 + base address
sw $0,0($t9) #c[i][j] = 0
	
iloop:
	slt $t8,$t0,$t1 #i < m
	beq $t8,$0,done
	slt $t8,$t3,$s2 #j < q
	bne $t8,$0,jloop
	addi $t0,$t0,1 #i = i + 1
	addi $t3,$0,0 #reset j
	j iloop
	
jloop:
	slt $t8,$t4,$s1 #k < n
	bne $t8,$0,kloop
	addi $t3,$t3,1 #j = j + 1
	mult $t0,$s2 #i*q 
	mflo $t9 
	add $t9,$t9,$t3 #i*q+j
	sll $t9,$t9,2 #(i*q+j)*4
	add $t9,$t9,$t6 #(i*q+j)*4 + base address
	sw $0,0($t9) #c[i][j] = 0
	addi $t4,$0,0 #resets k
	j iloop
	
kloop:
	mult $t0,$s1 #(i * n)
	mflo $t8
	add $t8,$t8,$t4 #(i*n)+k
	sll $t8,$t8,2 #(i*n+k)*4
	add $t8,$t8,$t2 #(i*n+k)*4 + base address of a
	lw $t8,0($t8) 
	mult $t4,$s2 #(k * q)
	mflo $t7 
	add $t7,$t7,$t3 #(k*q)+j
	sll $t7,$t7,2 #((k*q)+j)*4
	add $t7,$t7,$t5 #((k*q)+j)*4 + base address of b
	lw $t7,0($t7)
	mult $t7,$t8 #a[i][k]*b[k][j]
	mflo $t8
	lw $t7,0($t9) #c[i][j] retrieval
	add $t7,$t7,$t8 #c[i][j] = c[i][j]+a[i][k]*b[j][k]
	sw $t7,0($t9) #storing in memory
	addi $t4,$t4,1 #k = k+1
	j jloop
	
done:


